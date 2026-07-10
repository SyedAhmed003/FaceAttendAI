"""
Camera Manager
--------------

Handles webcam initialization, frame capture,
camera configuration and cleanup.
"""

import cv2

from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT


class CameraManager:
    """Manages webcam operations."""

    def __init__(self):
        self.cap = None

    def start_camera(self):
        """Initialize webcam."""

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():
            raise RuntimeError("Unable to access webcam.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    def read_frame(self):
        """Read one frame from webcam."""

        if self.cap is None:
            raise RuntimeError("Camera has not been started.")

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def stop_camera(self):
        """Release webcam."""

        if self.cap is not None:
            self.cap.release()

        cv2.destroyAllWindows()