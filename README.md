# FastAPI Actuator

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.12+-green?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-orange?style=flat-square)
![Author](https://img.shields.io/badge/author-Abhijit-purple?style=flat-square)

A lightweight, production‑friendly actuator extension for FastAPI applications.

Adds plug‑and‑play endpoints for runtime visibility: health probes, service info, request metrics, system stats, and route discovery. Built with middleware instrumentation—minimal, fast, and extensible.

---

## ✨ Features

| Category           | Feature                                              |
| ------------------ | ---------------------------------------------------- |
| 🩺 **Health**      | Liveness probe (`/health/live`)                      |
|                    | Readiness probe with custom checks (`/health/ready`) |
|                    | Pluggable `register_readiness_check()` for DB        |
| 📋 **Info**        | App name, version, environment, start time           |
| 🖥️ **Platform**    | Python version, OS platform, hostname                |
| 📊 **Metrics**     | Total requests, in‑flight requests, avg latency      |
|                    | Status code distribution                             |
|                    | Uptime tracking                                      |
| 🧠 **System**      | CPU %, memory %, memory used (MB), thread count      |
| 🗺️ **Mappings**    | Auto‑discovered route list (excludes internals)      |
| ⚡ **Performance** | Async‑first, thread‑safe state, zero blocking        |

---

## 📦 Installation

**Using uv:**

```bash
uv add fastapi-actuator
```

**From source:**

```bash
uv pip install -e .
```

---

## 🚀 Quick Start

```python
from fastapi import FastAPI
from app import add_actuator, register_readiness_check

app = FastAPI()

# Basic setup
add_actuator(app, name="MyService", version="1.0.0", environment="production")

# Optional: register a custom readiness check (e.g., database)
async def db_check():
    # return True if healthy
    return True

register_readiness_check("database", db_check)
```

---

## 🔗 Endpoints

| Endpoint                     | Description                                |
| ---------------------------- | ------------------------------------------ |
| `GET /actuator`              | Index of all actuator endpoints            |
| `GET /actuator/health/live`  | Liveness probe → `{"status": "UP"}`        |
| `GET /actuator/health/ready` | Readiness probe with registered checks     |
| `GET /actuator/info`         | App name, version, environment, started_at |
| `GET /actuator/platform`     | Python version, OS, hostname               |
| `GET /actuator/metrics`      | Request stats + system metrics             |
| `GET /actuator/mappings`     | Discovered application routes              |

---

## 🧪 Testing the Actuator

A sample `main.py` is provided to test the SDK:

```bash
fastapi dev main.py
```

Then visit:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/actuator
- http://127.0.0.1:8000/actuator/health/ready

---

## 💡 Why?

Modern services need observability from day one. This project brings Spring Boot Actuator‑style capabilities to FastAPI in a simple, Pythonic way—without heavy monitoring stacks.

---

## 🔮 Roadmap

- [ ] Prometheus metrics exporter
- [ ] Auth‑protected endpoints
- [ ] OpenTelemetry integration
- [ ] Configurable endpoint prefix

---

## 📄 License

Apache License

---

If this project helps you, consider giving it a ⭐
