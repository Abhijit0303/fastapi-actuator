import socket
from fastapi import APIRouter, FastAPI
from app.core import actuator_state
from app.system import get_system_info
import platform
from fastapi.routing import APIRoute

def get_router(app: FastAPI):

    router = APIRouter(prefix="/actuator")

    #---------------------INDEX----------------------------

    @router.get("")
    async def index():
        return {
            "endpoints": [
                "/actuator/health/live",
                "/actuator/health/ready",
                "/actuator/info",
                "/actuator/platform",
                "/actuator/metrics",
                "/actuator/mappings",
            ],
            "count": 6,
        }

    #---------------------HEALTH----------------------------

    @router.get("/health/live")
    async def liveness():
        return {"status": "UP"}

    @router.get("/health/ready")
    async def readiness():
        if not actuator_state.readiness_checks:
            return {"status": "READY", "checks": {}}

        results = {}
        overall = True

        for name, check in actuator_state.readiness_checks.items():
            try:
                result = await check()
                results[name] = "UP" if result else "DOWN"
                if not result:
                    overall = False
            except Exception as e:
                results[name] = f"ERROR: {str(e)}"
                overall = False

        return {
            "status": "READY" if overall else "NOT READY",
            "checks": results,
        }

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

    #---------------------MAPPINGS----------------------------

    @router.get("/mappings")
    async def mappings():
        result = []

        for route in app.routes:
            if not isinstance(route, APIRoute):
                continue

            if route.path.startswith("/actuator") or \
            route.path.startswith("/docs") or \
            route.path.startswith("/openapi"):
                continue

            result.append({
                "path": route.path,
                "methods": list(route.methods),
            })

        return {
            "routes": result,
            "count": len(result),
        }

    return router