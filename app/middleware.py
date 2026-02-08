import time
from fastapi import Request
from app.core import actuator_state

async def request_metrics_middleware(request: Request, call_next):
    start = time.monotonic()
    actuator_state.record_reuest_start()
    try:
        response = await call_next(request)
        return response
    finally:
        latency = time.monotonic() - start
        actuator_state.record_request_end(latency)