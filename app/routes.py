import socket
from fastapi import APIRouter
from app.core import actuator_state
from app.system import get_system_info
import platform

router = APIRouter(prefix="/actuator")

#---------------------HEALTH----------------------------

@router.get("/health/live")
async def liveness():
    return {"status": "UP"}

@router.get("/health/ready")
async def readiness():
    return {"status": "READY"}

#---------------------INFO----------------------------

@router.get("/info")
async def info():
    return {
        "name": actuator_state.name,
        "version": actuator_state.version,
        "environment": actuator_state.environment,
        "started_at": actuator_state.started_at,
    }

#---------------------PLATFORM----------------------------

@router.get("/platform")
async def platform_info():
    return {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "hostname": socket.gethostname(),
    }

#---------------------METRICS----------------------------

@router.get("/metrics")
async def metrics():

    base_metrices = {
        "uptime_seconds": actuator_state.uptime(),
        "total_requests": actuator_state.total_requests,
        "in_flight_requests": actuator_state.in_flight_requests,
        "average_latency_seconds": actuator_state.average_latency(),
        "status_codes": actuator_state.status_codes,
    }

    return {
        **base_metrices,
        **get_system_info()
    }