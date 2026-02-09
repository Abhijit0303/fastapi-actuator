import time
from fastapi import Request, Response
from typing import Optional
from app.core import actuator_state

async def request_metrics_middleware(request: Request, call_next):
    start = time.monotonic()
    actuator_state.record_reuest_start()

    response: Optional[Response] = None

    try:
        response = await call_next(request)
        return response
    finally:
        latency = time.monotonic() - start
        status_code = response.status_code if response else 500
        actuator_state.record_request_end(latency, status_code)