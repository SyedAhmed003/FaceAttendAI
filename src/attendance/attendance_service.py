"""
Attendance Service

Handles attendance marking for recognized employees.
"""

from datetime import datetime

from src.database.database_manager import DatabaseManager


class AttendanceService:

    def __init__(self):

        self.db = DatabaseManager()

    def mark(self, employee_id, confidence):
        """
        Mark attendance for an employee.

        Returns:
            (success, message)
        """

        today = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        # Check if attendance already exists
        if self.db.attendance_exists(employee_id, today):

            return (
                False,
                "Attendance Already Marked"
            )

        # Mark attendance
        self.db.mark_attendance(
            employee_id=employee_id,
            date=today,
            check_in=current_time,
            confidence=confidence
        )

        return (
            True,
            "Attendance Marked Successfully"
        )