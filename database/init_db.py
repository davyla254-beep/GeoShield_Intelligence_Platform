import sqlite3
from pathlib import Path

# Database path
DB_PATH = Path(__file__).parent / "geoshield.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ============================
# Infrastructure Table
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS infrastructure (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    category TEXT NOT NULL,

    county TEXT,

    latitude REAL,

    longitude REAL,

    capacity INTEGER,

    status TEXT,

    contact TEXT

)
""")

# ============================
# Disaster Alerts
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    disaster_type TEXT,

    county TEXT,

    latitude REAL,

    longitude REAL,

    severity TEXT,

    status TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ============================
# Cyber Security Logs
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS cyber_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ip_address TEXT,

    country TEXT,

    city TEXT,

    attack_type TEXT,

    target TEXT,

    status TEXT,

    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()
conn.close()

print("✅ GeoShield database created successfully!")
print(DB_PATH)