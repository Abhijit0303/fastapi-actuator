from fastapi import APIRouter
from app.core import actuator_state
from app.system import get_system_info
import platform

router = APIRouter(prefix="/actuator")

@router.get("/health")
async def health():
    return {"status": "UP"}

@router.get("/info")
async def info():
    return {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "processor": platform.processor()
    }

@router.get("/metrics")
async def metrics():

    base_metrices = {
        "uptime_seconds": actuator_state.uptime(),
        "total_requests": actuator_state.total_requests,
        "in_flight_requests": actuator_state.in_flight_requests,
        "average_latency_seconds": actuator_state.average_latency()
    }

    return {
        **base_metrices,
        **get_system_info()
    }