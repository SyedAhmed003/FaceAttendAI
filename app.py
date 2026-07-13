"""
FaceAttend AI
Main Application
"""

from src.database.database_manager import DatabaseManager
from src.registration.registration_service import RegistrationService


def view_employees():

    db = DatabaseManager()

    employees = db.get_all_employees()

    print("\n========== Registered Employees ==========\n")

    if not employees:
        print("No employees found.\n")
        return

    for emp in employees:

        print(f"Employee ID : {emp[0]}")
        print(f"Name        : {emp[1]}")
        print(f"Department  : {emp[2]}")
        print(f"Designation : {emp[3]}")
        print("--------------------------------------")


def main():

    db = DatabaseManager()
    db.create_tables()

    registration = RegistrationService()

    while True:

        print("\n===================================")
        print("          FaceAttend AI")
        print("===================================")
        print("1. Register Employee")
        print("2. View Employees")
        print("3. Exit")
        print("===================================")

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":

            registration.register_employee()

        elif choice == "2":

            view_employees()

        elif choice == "3":

            print("\nThank You!")

            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()