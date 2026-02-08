from fastapi import APIRouter
from app.core import actuator_state
import platform

router = APIRouter(prefix="/actuator")

@router.get("/health")
async def health():
    return {"status": "UP"}

@router.get("/info")
async def info():
    return {
        "python_version": platform.python_version()
    }

@router.get("/metrics")
async def metrics():
    return {
        "uptime_seconds": actuator_state.uptime(),
        "total_requests": actuator_state.total_requests,
        "in_flight_requests": actuator_state.in_flight_requests,
        "average_latency_seconds": actuator_state.average_latency()
    }