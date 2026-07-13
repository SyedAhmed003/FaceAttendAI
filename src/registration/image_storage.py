"""
Image Storage Module
--------------------

Creates employee folders and saves captured images.
"""

from pathlib import Path
import cv2

from config import DATASET_DIR


class ImageStorage:
    """
    Handles image storage operations.
    """

    def __init__(self):

        self.employee_root = DATASET_DIR / "employees"

        self.employee_root.mkdir(parents=True, exist_ok=True)

    def create_employee_folder(self, employee_id: str) -> Path:
        """
        Create folder for an employee.
        """

        employee_folder = self.employee_root / employee_id

        employee_folder.mkdir(parents=True, exist_ok=True)

        return employee_folder

    def save_image(self, frame, folder: Path, image_number: int):
        """
        Save one captured image.
        """

        image_name = f"image_{image_number:03d}.jpg"

        image_path = folder / image_name

        cv2.imwrite(str(image_path), frame)

        return image_path

    def save_profile_image(self, frame, folder: Path):
        """
        Save profile image.
        """

        profile_path = folder / "profile.jpg"

        cv2.imwrite(str(profile_path), frame)

        return profile_path