from fastapi import Depends, FastAPI, HTTPException, Query, File, UploadFile
from fastapi.responses import JSONResponse
import models
from db import engine
import  models
import schemas
from operations import ItemRepo
from sqlalchemy.orm import Session
from typing import List, Union
import logging
import pandas as pd
from dependencies import get_db, is_database_online
from fastapi_health import health

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# DB healthcheck end point
app.add_api_route('/health', health([is_database_online]))

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.post('/items', tags=["Item"],response_model=schemas.Item,status_code=201)
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Add Metrics to a user. 
    """
    db_item = ItemRepo.fetch_by_name_prop_key(db, username=item_request.username, prop_name= item_request.prop_name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await ItemRepo.create(db=db, item=item_request)

@app.get('/items/{username}', tags=["Item"])
def get_user_matrics(username: str, db: Session = Depends(get_db)):
    """
    Get all the metrics of a user
    """
    rec = ItemRepo.fetch_user_matrics(db = db, username = username) 
    if rec:
        return {
            "resp": rec
        }
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")

@app.put('/items/{username}/{prop_name}', tags=["Item"])
async def update_item(username: str, prop_name: str, item_request: schemas.ItemUpdate, db: Session = Depends(get_db)):
    """
    Update a metric of a user.
    """
    db_item = ItemRepo.fetch_by_name_prop_key(db= db, username= username, prop_name =prop_name)
    if db_item:
        db_item.prop_value = item_request.prop_value
        return await ItemRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")
    
@app.delete('/items/{username}/{prop_name}', tags=["Item"])
async def delete_item(username: str, prop_name: str, db: Session = Depends(get_db)):
    """
    Delete a particular metric of a user
    """
    db_item = ItemRepo.fetch_by_name_prop_key(db= db, username= username, prop_name =prop_name)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    await ItemRepo.delete(db, username, prop_name)
    return "Item deleted successfully!"

# @app.get('/items/tags/{tag_name}', tags=['Item']) # For single tag filter

# It will filter records as per multiple tags
# Params are passed as list of strings, each string represent an specific tag
@app.get('/items/tags/', tags=['Item'])
def get_all_records_by_tags(tags_name: Union[List[str],None] =  Query(default=None), db: Session = Depends(get_db)):
    """
    Get metrics of all the users
    """
    filtered_records = []
    for tag in tags_name:
        records = ItemRepo.fetch_records_by_tags(db = db, tag_name= tag)
        if records:
            for rec in records:
                filtered_records.append(rec) 
        else:
            logging.warning("Not present for " + tag)
    return {"resp": filtered_records}



# BULK write operation with CSV
@app.post('/items/bulk-write', tags=['Item'])
async def create_items_using_csv(csv_file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    # Reading file using pandas
    df = pd.read_csv(csv_file.file,  encoding= 'unicode_escape')
    
    for row in df.itertuples():
        db_item = ItemRepo.fetch_by_name_prop_key(db, username=row[1], prop_name= row[2])
        if db_item:
            logging.warning("Record already exist")
        else:
            try:
                db_item = models.Item(
                    username = row[1], prop_name= row[2],
                    prop_value = row[3], tag_name = row[4]
                )
                db.add(db_item)
                db.commit()
                logging.info("Entry added into DB")
                db.refresh(db_item)
            except:
                logging.error("Something wrong on DB side")
                pass
            
    return {"resp": "records added successfully"}
