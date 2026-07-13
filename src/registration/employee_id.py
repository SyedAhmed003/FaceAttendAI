"""
Employee ID Generator
---------------------

Generates unique employee IDs for FaceAttend AI.
"""

import sqlite3
from config import DATABASE_PATH


class EmployeeIDGenerator:
    """
    Generates employee IDs in the format:

    EMP001
    EMP002
    EMP003
    """

    PREFIX = "EMP"

    @staticmethod
    def generate():

        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT employee_id
            FROM employees
            ORDER BY employee_id DESC
            LIMIT 1
        """)

        result = cursor.fetchone()

        connection.close()

        if result is None:
            return "EMP001"

        last_id = result[0]

        number = int(last_id.replace(EmployeeIDGenerator.PREFIX, ""))

        number += 1

        return f"{EmployeeIDGenerator.PREFIX}{number:03d}"