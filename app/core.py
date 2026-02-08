import time
from threading import Lock


class ActuatorState:
    def __init__(self):
        self.start_time = time.monotonic()
        self.total_requests = 0
        self.in_flight_requests = 0
        self.total_latency = 0.0
        self.lock = Lock()

    def record_reuest_start(self):
        with self.lock:
            self.total_requests += 1
            self.in_flight_requests += 1

    def record_request_end(self, latency: float):
        with self.lock:
            self.in_flight_requests -= 1
            self.total_latency += latency

    def uptime(self):
        return time.monotonic() - self.start_time

    def average_latency(self):
        with self.lock:
            if self.total_requests == 0:
                return 0.0
            return self.total_latency / self.total_requests

actuator_state = ActuatorState()