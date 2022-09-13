from logging import NullHandler
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from db import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key = True, index= True)
    username = Column(String(30), nullable= False)
    prop_name = Column(String(50), nullable = False)
    prop_value = Column(String(70), nullable = False)
    tag_name = Column(String(50), nullable= False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    
    
    def __repr__(self):
        return 'ItemModel(username=%s, prop_name=%s, prop_value=%s, tag_name=%s, created_at=%s, updated_at=%s)' % (self.username, self.prop_name, self.prop_value, self.tag_name, self.created_at, self.updated_at)
            
            
    
    