from fastapi import FastAPI
from app import add_actuator, register_readiness_check
import sqlite3
from datetime import datetime

app = FastAPI()

add_actuator(app, name="Simple Hello world to check", version="3.2.3", environment="development")

# Initialize a simple SQLite database on startup
@app.on_event("startup")
async def init_db():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Readiness check that verifies we can connect and run a trivial query
async def sqlite_readiness_check():
    try:
        conn = sqlite3.connect("app.db", timeout=1)
        cur = conn.cursor()
        cur.execute("SELECT 1")
        conn.close()
        return True
    except Exception:
        return False

# Register the database readiness check with the actuator
register_readiness_check("sqlite", sqlite_readiness_check)

@app.get("/")
async def root():
    return {"message": "Hello World for the actuator app"}

# Simple endpoint that uses the DB so the app truly depends on it
@app.post("/ping")
async def create_ping():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ping (created_at) VALUES (?)",
        (datetime.now().isoformat(),),
    )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM ping").fetchone()[0]
    conn.close()
    return {"pings": count}

