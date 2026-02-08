# FastAPI Actuator Lite

A lightweight, production‑friendly actuator extension for FastAPI
applications.

It adds plug‑and‑play endpoints for runtime visibility such as health,
basic service info, request counters, in‑flight tracking, uptime, and
latency aggregation. Built using middleware instrumentation and designed
to stay minimal, fast, and extensible.

## Features

- Health endpoint
- Service/runtime info
- Total request counter
- In‑flight request tracking
- Uptime measurement
- Average latency
- Zero heavy dependencies
- Works with async workloads

## Install (using uv)

```bash
uv add fastapi-actuator-lite
```

or if using from source:

```bash
uv pip install -e .
```

## Usage

```python
from fastapi import FastAPI
from fastapi_actuator import add_actuator

app = FastAPI()
add_actuator(app)
```

## Exposed Endpoints

- `/actuator/health`
- `/actuator/info`
- `/actuator/metrics`

## Why

Modern services need observability from day one. This project brings
Spring‑style actuator capabilities to FastAPI in a simple and pythonic
way, without forcing teams into large monitoring stacks.

## Future Scope

- Prometheus exporter
- Custom health contributors
- DB & cache readiness
- Auth protected endpoints
- OpenTelemetry integration

---

If this project helps you, consider giving it a ⭐.
