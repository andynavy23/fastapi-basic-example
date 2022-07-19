from fastapi import FastAPI
from schemas.user import User

app = FastAPI()

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
