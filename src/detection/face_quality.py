"""
Face Quality Assessment Module
"""

from dataclasses import dataclass
import cv2
import numpy as np


@dataclass
class QualityResult:
    """
    Stores the result of quality validation.
    """

    is_valid: bool
    message: str


class FaceQuality:

    # ---------- Thresholds ----------
    MIN_FACE_WIDTH = 180
    MAX_FACE_WIDTH = 500

    MIN_BRIGHTNESS = 70
    MAX_BRIGHTNESS = 200

    MIN_BLUR_SCORE = 100

    CENTER_TOLERANCE = 100

    @staticmethod
    def is_valid(frame, faces):
        """
        Validate whether the current frame is suitable
        for registration.
        """

        # --------------------------------------------------
        # Exactly one face
        # --------------------------------------------------
        if len(faces) == 0:
            return QualityResult(False, "No face detected")

        if len(faces) > 1:
            return QualityResult(False, "Multiple faces detected")

        face = faces[0]

        h, w, _ = frame.shape

        # --------------------------------------------------
        # Face Size
        # --------------------------------------------------
        if face.width < FaceQuality.MIN_FACE_WIDTH:
            return QualityResult(False, "Move Closer")

        if face.width > FaceQuality.MAX_FACE_WIDTH:
            return QualityResult(False, "Move Back")

        # --------------------------------------------------
        # Face Center
        # --------------------------------------------------
        face_center_x = face.x + face.width // 2
        frame_center_x = w // 2

        if abs(face_center_x - frame_center_x) > FaceQuality.CENTER_TOLERANCE:
            return QualityResult(False, "Center Your Face")

        # --------------------------------------------------
        # Brightness
        # --------------------------------------------------
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        brightness = np.mean(gray)

        if brightness < FaceQuality.MIN_BRIGHTNESS:
            return QualityResult(False, "Increase Lighting")

        if brightness > FaceQuality.MAX_BRIGHTNESS:
            return QualityResult(False, "Reduce Lighting")

        # --------------------------------------------------
        # Blur Detection
        # --------------------------------------------------
        blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

        if blur_score < FaceQuality.MIN_BLUR_SCORE:
            return QualityResult(False, "Hold Still")

        return QualityResult(True, "Good Quality")