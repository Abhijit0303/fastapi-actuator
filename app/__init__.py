from fastapi import FastAPI
from app.routes import router as actuator_router
from app.middleware import request_metrics_middleware
from app.core import actuator_state

def add_actuator(
        app: FastAPI,
        name: str = "app",
        version: str = "0.0.1",
        environment: str = "development",
    ):

    actuator_state.name = name
    actuator_state.version = version
    actuator_state.environment = environment

    app.include_router(actuator_router)
    app.middleware("http")(request_metrics_middleware)