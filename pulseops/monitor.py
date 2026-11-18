import psutil
from datetime import datetime, timezone
import time

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Returns the current memory usage percentage."""
    return psutil.virtual_memory().percent

def get_disk_usage():
    """Returns the current disk usage percentage."""
    return psutil.disk_usage('C:\\').percent

def get_cpu_cores():
    """Returns the number of CPU cores."""
    return psutil.cpu_count(logical=True)

def get_timestamp():
    """Returns the current timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()  

def collect_metrics():
    """Collects and returns system metrics as a dictionary."""
    metrics = {
        "timestamp": get_timestamp(),
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "cpu_cores": get_cpu_cores()
    }
    return metrics

def start_monitoring(interval=5):
    """Continuously collects sytem metrics"""
    if interval <= 0:
        raise ValueError("Monitoring interval must be greater than zero")
    try:
        while True:
            system_metrics = collect_metrics()
            print (system_metrics)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Program stopped by user.")

if __name__ == "__main__":
    start_monitoring()