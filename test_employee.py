"""
Temporary Test File
Delete after testing
"""

from src.registration.image_capture import ImageCapture
from src.registration.image_storage import ImageStorage


def main():

    storage = ImageStorage()

    folder = storage.create_employee_folder("EMP_TEST")

    capture = ImageCapture(storage)

    success = capture.capture_images(folder)

    if success:
        print("\n✅ Capture Successful")
    else:
        print("\n❌ Capture Cancelled")


if __name__ == "__main__":
    main()