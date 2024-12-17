from fastapi import FastAPI, HTTPException
from models.user import User


app = FastAPI()

@app.get("/")
async def hello():
    return {"hellow": "Hello World"}

@app.post("/users/")
async def create_user(user: User):
    try:
        return {'name': user.name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
