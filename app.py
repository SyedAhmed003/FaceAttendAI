"""
FaceAttend AI
Main Application
"""

import cv2

from src.camera.camera_manager import CameraManager
from src.database.database_manager import DatabaseManager
from src.detection.face_detector import FaceDetector
from src.detection.face_quality import FaceQuality
from src.detection.face_utils import draw_face


def main():
    """
    Main application entry point.
    """

    # ---------------------------------
    # Initialize Database
    # ---------------------------------
    db = DatabaseManager()
    db.create_tables()

    # ---------------------------------
    # Initialize Camera
    # ---------------------------------
    camera = CameraManager()
    camera.start_camera()

    # ---------------------------------
    # Initialize Face Detector
    # ---------------------------------
    detector = FaceDetector()

    print("FaceAttend AI Started")
    print("Press 'Q' to Quit")

    while True:

        # Read frame
        frame = camera.read_frame()

        if frame is None:
            break

        # Detect faces
        faces = detector.detect(frame)

        # Evaluate frame quality
        quality = FaceQuality.is_valid(frame, faces)

        # Draw detected face
        if len(faces) == 1:
            frame = draw_face(frame, faces[0])

        # Status Color
        color = (0, 255, 0) if quality.is_valid else (0, 0, 255)

        # Display Quality Message
        cv2.putText(
            frame,
            quality.message,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2,
        )

        # Show Number of Faces
        cv2.putText(
            frame,
            f"Faces Detected : {len(faces)}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        # Display Window
        cv2.imshow("FaceAttend AI", frame)

        # Quit
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    # Cleanup
    camera.stop_camera()

    print("Application Closed")


if __name__ == "__main__":
    main()