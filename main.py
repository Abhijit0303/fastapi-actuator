from fastapi import FastAPI
from app import add_actuator

app = FastAPI()

add_actuator(app)

@app.get("/")
async def root():
    return {"message": "Hello World for the actuator app"}

