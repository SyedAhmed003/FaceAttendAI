"""
Image Capture Module

Captures employee face images for registration.
"""

import cv2

from src.camera.camera_manager import CameraManager
from src.detection.face_detector import FaceDetector
from src.detection.face_quality import FaceQuality
from src.detection.face_utils import draw_face


class ImageCapture:
    """
    Handles employee image capture.
    """

    def __init__(self, storage):

        self.storage = storage

        self.camera = CameraManager()
        self.detector = FaceDetector()

        # Capture Instructions
        self.instructions = [
            "Look Straight",
            "Turn Left",
            "Turn Right",
            "Look Up"
        ]

    def get_instruction(self, captured):
        """
        Returns instruction based on image count.
        """

        if captured < 5:
            return self.instructions[0]

        elif captured < 10:
            return self.instructions[1]

        elif captured < 15:
            return self.instructions[2]

        else:
            return self.instructions[3]

    def capture_images(self, employee_folder, total_images=20):
        """
        Capture employee images.
        """

        self.camera.start_camera()

        captured = 0

        print("\n===================================")
        print("Starting Face Registration")
        print("Press 'C' to Capture")
        print("Press 'Q' to Cancel")
        print("===================================\n")

        while True:

            frame = self.camera.read_frame()

            if frame is None:
                break

            faces = self.detector.detect(frame)

            quality = FaceQuality.is_valid(frame, faces)

            # Draw face
            if len(faces) == 1:
                draw_face(frame, faces[0])

            instruction = self.get_instruction(captured)

            # -----------------------------
            # Display Information
            # -----------------------------

            cv2.putText(
                frame,
                f"Instruction : {instruction}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            color = (0, 255, 0) if quality.is_valid else (0, 0, 255)

            cv2.putText(
                frame,
                f"Quality : {quality.message}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            cv2.putText(
                frame,
                f"Captured : {captured}/{total_images}",
                (20, 105),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                "Press C = Capture | Q = Quit",
                (20, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            cv2.imshow("FaceAttend AI - Registration", frame)

            key = cv2.waitKey(1) & 0xFF
                        # -----------------------------
            # Quit Registration
            # -----------------------------
            if key == ord("q"):
                print("\nRegistration cancelled.")
                break

            # -----------------------------
            # Capture Image
            # -----------------------------
            if key == ord("c"):

                # Allow capture only if quality is good
                if not quality.is_valid:
                    print(f"Cannot Capture: {quality.message}")
                    continue

                captured += 1

                # Save image
                self.storage.save_image(
                    frame,
                    employee_folder,
                    captured
                )

                print(f"Image {captured} saved.")

                # First image becomes profile picture
                if captured == 1:
                    self.storage.save_profile_image(
                        frame,
                        employee_folder
                    )

                # Finish after required images
                if captured >= total_images:
                    print("\nAll images captured successfully!")
                    break

        # -----------------------------
        # Cleanup
        # -----------------------------
        self.camera.stop_camera()

        cv2.destroyAllWindows()

        if captured == total_images:
            return True

        return False