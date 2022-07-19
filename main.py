from fastapi import FastAPI
from config import settings
from schemas.user import User

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

@app.post("/create_user/")
async def create_user(user: User):
    return user
