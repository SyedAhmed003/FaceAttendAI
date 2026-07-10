"""
Face Detection Module
---------------------

Uses MediaPipe Face Detection to detect faces
and returns structured face information.
"""

from dataclasses import dataclass
from typing import List

import cv2
import mediapipe as mp


@dataclass
class Face:
    """
    Represents one detected face.
    """

    x: int
    y: int
    width: int
    height: int
    confidence: float


class FaceDetector:
    """
    MediaPipe Face Detector.
    """

    def __init__(self, confidence: float = 0.7):

        self.mp_face_detection = mp.solutions.face_detection

        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=1,
            min_detection_confidence=confidence
        )

    def detect(self, frame) -> List[Face]:
        """
        Detect faces in a frame.

        Returns
        -------
        List[Face]
        """

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.detector.process(rgb)

        faces = []

        if not results.detections:
            return faces

        h, w, _ = frame.shape

        for detection in results.detections:

            bbox = detection.location_data.relative_bounding_box

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            bw = int(bbox.width * w)
            bh = int(bbox.height * h)

            confidence = detection.score[0]

            faces.append(
                Face(
                    x=x,
                    y=y,
                    width=bw,
                    height=bh,
                    confidence=confidence
                )
            )

        return faces