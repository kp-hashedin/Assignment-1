from db import SessionLocal
from fastapi import Depends

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Database Health Check
def is_database_online(session: bool = Depends(get_db)):
    if session:
        return {
            "message": "OK"
        }
    else:
        return {
            "message": "NOT OK"
        }