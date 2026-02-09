from datetime import datetime
import time
from threading import Lock


class ActuatorState:
    def __init__(self):
        self.start_time = time.monotonic()
        self.started_at = datetime.now().isoformat()

        self.total_requests = 0
        self.in_flight_requests = 0
        self.total_latency = 0.0
        self.status_codes = {}

        self.name = "FastAPI Actuator"
        self.version = "0.0.1"
        self.environment = "development"

        self.lock = Lock()

    def record_reuest_start(self):
        with self.lock:
            self.total_requests += 1
            self.in_flight_requests += 1

    def record_request_end(self, latency: float, status_code: int):
        with self.lock:
            self.in_flight_requests -= 1
            self.total_latency += latency
            self.status_codes[status_code] = (
                self.status_codes.get(status_code, 0) + 1
            )

    def uptime(self):
        return round(time.monotonic() - self.start_time, 2)

    def average_latency(self):
        with self.lock:
            if self.total_requests == 0:
                return 0.0
            return round(self.total_latency / self.total_requests, 4)

actuator_state = ActuatorState()