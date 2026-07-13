"""
Database Manager for FaceAttend AI

This module is responsible for:
- Creating the SQLite database
- Creating required tables
- Managing the database connection
- Employee database operations
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

    # ======================================================
    # Employee Operations
    # ======================================================

    def add_employee(self, employee):
        """
        Add a new employee to the database.
        """

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO employees(
            employee_id,
            name,
            department,
            designation,
            image_folder,
            embedding_path
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            employee.employee_id,
            employee.name,
            employee.department,
            employee.designation,
            f"dataset/employees/{employee.employee_id}",
            None
        ))

        connection.commit()
        connection.close()

    def employee_exists(self, employee_id):
        """
        Check if an employee already exists.
        """

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT employee_id FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        result = cursor.fetchone()

        connection.close()

        return result is not None

    def get_employee(self, employee_id):
        """
        Get one employee by ID.
        """

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        WHERE employee_id = ?
        """, (employee_id,))

        employee = cursor.fetchone()

        connection.close()

        return employee

    def get_all_employees(self):
        """
        Return all registered employees.
        """

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT
            employee_id,
            name,
            department,
            designation
        FROM employees
        ORDER BY employee_id
        """)

        employees = cursor.fetchall()

        connection.close()

        return employees