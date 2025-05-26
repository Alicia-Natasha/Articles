# setup_db.py

import sqlite3
import os

DB_PATH = "code-challenge/lib/db/database.db"
SCHEMA_PATH = "code-challenge/lib/db/schema.sql"

def create_schema():
    # Ensure database directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        with open(SCHEMA_PATH, "r") as schema_file:
            cursor.executescript(schema_file.read())
        conn.commit()
        print("Database schema created successfully.")
    except Exception as e:
        print(f"Error creating schema: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_schema()
