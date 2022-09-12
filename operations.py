from pyexpat import model
from sqlalchemy.orm import Session

import models, schemas
import logging

class ItemRepo:
    async def create(db: Session, item: schemas.ItemCreate):
            db_item = models.Item(
                username = item.username, prop_name= item.prop_name,
                prop_value = item.prop_value, tag_name = item.tag_name
            )
            db.add(db_item)
            db.commit()
            logging.info("Entry added into DB")
            db.refresh(db_item)
            return db_item
    
    def fetch_by_name_prop_key(db: Session,username, prop_name):
        return db.query(models.Item).filter(models.Item.username == username, models.Item.prop_name == prop_name).first()
    
    def fetch_user_matrics(db: Session, username):
        return db.query(models.Item).filter(models.Item.username == username).all()
    
    def fetch_records_by_tags(db: Session, tag_name):
        return db.query(models.Item).filter(models.Item.tag_name == tag_name).all()
    
    async def delete(db: Session,username, prop_name):
        db_item= db.query(models.Item).filter_by(username=username, prop_name= prop_name).first()
        db.delete(db_item)
        logging.info("Records Deleted Successfully")
        db.commit()
        
    async def update(db: Session,item_data):
        print(item_data)
        updated_item = db.merge(item_data)
        db.commit()
        logging.warning("Record updated successfully")
        return updated_item
