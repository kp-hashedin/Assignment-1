from datetime import datetime
from pydantic import BaseModel

class ItemBase(BaseModel):
    username: str
    prop_name: str
    prop_value: str
    tag_name: str


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
        
class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    prop_value:str

