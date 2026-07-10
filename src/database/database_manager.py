"""
Database Manager for FaceAttend AI

This module is responsible for:
- Creating the SQLite database
- Creating required tables
- Managing the database connection
"""

import sqlite3
from pathlib import Path

from config import DATABASE_PATH


class DatabaseManager:
    """Handles all SQLite database operations."""

    def __init__(self):
        self.db_path = Path(DATABASE_PATH)

    def connect(self):
        """Create and return a database connection."""
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        """Create all required tables if they don't already exist."""

        connection = self.connect()
        cursor = connection.cursor()

        # Employees Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            designation TEXT,
            image_folder TEXT,
            embedding_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Attendance Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            date TEXT,
            check_in TEXT,
            confidence REAL,
            status TEXT
        )
        """)

        # Unknown Visitors
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS unknown_visitors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            detected_time TEXT,
            reason TEXT
        )
        """)

        connection.commit()
        connection.close()

        print("Database initialized successfully.")