"""
Database Manager for FaceAttend AI
"""

import sqlite3
from pathlib import Path

from config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):
        self.db_path = Path(DATABASE_PATH)

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):

        connection = self.connect()
        cursor = connection.cursor()

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

    # --------------------------
    # Employee
    # --------------------------

    def add_employee(self, employee):

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

    def get_employee(self, employee_id):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT
            employee_id,
            name,
            department,
            designation
        FROM employees
        WHERE employee_id = ?
        """, (employee_id,))

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return {
            "employee_id": row[0],
            "name": row[1],
            "department": row[2],
            "designation": row[3]
        }

    def get_all_employees(self):

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

    # --------------------------
    # Attendance
    # --------------------------

    def attendance_exists(self, employee_id, date):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id
        FROM attendance
        WHERE employee_id = ?
        AND date = ?
        """, (
            employee_id,
            date
        ))

        result = cursor.fetchone()

        connection.close()

        return result is not None

    def mark_attendance(
        self,
        employee_id,
        date,
        check_in,
        confidence
    ):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO attendance(
            employee_id,
            date,
            check_in,
            confidence,
            status
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            employee_id,
            date,
            check_in,
            confidence,
            "Present"
        ))

        connection.commit()
        connection.close()