from fastapi import FastAPI
from app import add_actuator

app = FastAPI()

add_actuator(app, name="Simple Hello world to check", version="3.2.3", environment="development")

@app.get("/")
async def root():
    return {"message": "Hello World for the actuator app"}

