"""
Registration Service

Handles the complete employee registration workflow.
"""

from src.database.database_manager import DatabaseManager
from src.registration.employee_id import EmployeeIDGenerator
from src.registration.employee_registration import Employee
from src.registration.image_storage import ImageStorage
from src.registration.image_capture import ImageCapture


class RegistrationService:
    """
    Handles complete employee registration.
    """

    def __init__(self):

        self.db = DatabaseManager()
        self.storage = ImageStorage()
        self.capture = ImageCapture(self.storage)

    def register_employee(self):

        print("\n========== Employee Registration ==========\n")

        # Generate Employee ID
        employee_id = EmployeeIDGenerator.generate()

        print(f"Generated Employee ID : {employee_id}\n")

        # Employee Details
        name = input("Employee Name      : ").strip()
        department = input("Department         : ").strip()
        designation = input("Designation        : ").strip()

        # Create Employee Object
        employee = Employee(
            employee_id=employee_id,
            name=name,
            department=department,
            designation=designation,
        )

        # Create Employee Folder
        employee_folder = self.storage.create_employee_folder(employee.employee_id)

        print("\nOpening camera...")
        print("Capture 20 images to complete registration.\n")

        # Capture Images
        success = self.capture.capture_images(employee_folder)

        if not success:
            print("\n❌ Registration cancelled.")
            return

        # Save Employee
        self.db.add_employee(employee)

        print("\n===================================")
        print("Employee Registered Successfully")
        print("===================================")

        print(f"Employee ID : {employee.employee_id}")
        print(f"Name        : {employee.name}")
        print(f"Department  : {employee.department}")
        print(f"Designation : {employee.designation}")

        print("\nImages Saved Successfully")
        print("Employee Saved to Database")
        print("===================================\n")