from fastapi import FastAPI
from app.routes import router as actuator_router
from app.middleware import request_metrics_middleware

def add_actuator(app: FastAPI):
    app.include_router(actuator_router)
    app.middleware("http")(request_metrics_middleware)