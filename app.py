"""
FaceAttend AI
Main Application
"""

from src.database.database_manager import DatabaseManager
from src.registration.registration_service import RegistrationService
from src.recognition.recognition_service import RecognitionService


def view_employees():
    """
    Display all registered employees.
    """

    db = DatabaseManager()

    employees = db.get_all_employees()

    print("\n===================================")
    print("     Registered Employees")
    print("===================================")

    if not employees:
        print("No employees found.\n")
        return

    for employee in employees:

        print(f"Employee ID : {employee[0]}")
        print(f"Name        : {employee[1]}")
        print(f"Department  : {employee[2]}")
        print(f"Designation : {employee[3]}")
        print("-----------------------------------")


def main():

    # Initialize Database
    db = DatabaseManager()
    db.create_tables()

    # Services
    registration = RegistrationService()
    recognition = RecognitionService()

    while True:

        print("\n===================================")
        print("          FaceAttend AI")
        print("===================================")
        print("1. Register Employee")
        print("2. Start Attendance")
        print("3. View Employees")
        print("4. Exit")
        print("===================================")

        choice = input("Enter Choice : ").strip()

        if choice == "1":

            registration.register_employee()

        elif choice == "2":

            recognition.start_recognition()

        elif choice == "3":

            view_employees()

        elif choice == "4":

            print("\nThank you for using FaceAttend AI.")
            break

        else:

            print("\nInvalid Choice. Please try again.")


if __name__ == "__main__":
    main()