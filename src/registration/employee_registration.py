"""
Employee Registration Model
"""

from dataclasses import dataclass


@dataclass
class Employee:
    """
    Employee information used during registration.
    """

    employee_id: str
    name: str
    department: str
    designation: str

    def to_dict(self):
        """Convert employee object to dictionary."""

        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
        }