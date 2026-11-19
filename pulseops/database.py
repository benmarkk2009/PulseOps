import sqlite3
from pulseops.monitor import collect_metrics

def initialize_database():
    """Create and initialize the PulseOps database."""
    connection = sqlite3.connect("pulseops.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            memory_usage REAL NOT NULL,
            disk_usage REAL NOT NULL,
            cpu_cores INTEGER
        );
    """)

    connection.commit()

    print("Database connection successful!")
    connection.close()

def insert_metrics(metrics):
    """Insert a system metrics dictionary into the database."""
    connection = sqlite3.connect("pulseops.db")

    connection.execute("""
        INSERT INTO metrics (
            timestamp,
            cpu_usage,
            memory_usage,
            disk_usage,
            cpu_cores
        )
        VALUES (?, ?, ?, ?, ?)
    """,(
        metrics["timestamp"],
        metrics["cpu_usage"],
        metrics["memory_usage"],
        metrics["disk_usage"],
        metrics["cpu_cores"]
    ))

    connection.commit()
    connection.close()

def get_recent_metrics(limit=5):
    """Retrieve the most recent system measurements"""
    connection = sqlite3.connect("pulseops.db")

    rows = connection.execute("""
        SELECT *
        FROM metrics
        ORDER BY timestamp DESC
        LIMIT ?
    """,(limit,)).fetchall()

    connection.close()
    return(rows)

if __name__ == "__main__":
    initialize_database()
    system_metrics = collect_metrics()
    insert_metrics(system_metrics)
    print("Metrics saved successfully!")
    recent_metrics = get_recent_metrics(limit=5)
    print(recent_metrics)