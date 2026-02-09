import os
import psutil

_process = psutil.Process(os.getpid())

def get_system_info():

    memory = _process.memory_info()
    cpu = _process.cpu_percent(interval=0.0)

    return {
        'cpu_percent': cpu,
        'memory_percent': _process.memory_percent(),
        "memory_used_mb": round(memory.rss / (1024 * 1024), 2),
        'memory_info': memory._asdict(),
        'threads': _process.num_threads(),
    }