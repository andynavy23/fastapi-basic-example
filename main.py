from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config import settings
from databases.sqlite_db import get_db_session
# from models.user_sqlite import User
from schemas.user import User as UserSchema
from crud import get_users, craete_user

app = FastAPI()

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
    }

@app.get("/hello_world")
async def hello_world():
    return {
        "message": "Hello World"
    }

@app.get("/request_with_id/{request_id}")
async def request_with_id(request_id: int):
    return {
        "request_id": request_id
    }

@app.get('/get_all_user')
async def get_all_user(db: Session = Depends(get_db_session)):
    return get_users(db)

@app.post('/craete_user')
async def craete_new_user(data: UserSchema, db: Session = Depends(get_db_session)):
    craete_user(db=db, user_in=data)
    return {
        "message": "success"
    }
