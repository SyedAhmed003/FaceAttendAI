"""
Recognition Service

Handles real-time face recognition using:
- Camera
- InsightFace
- FaceRecognizer
"""

from datetime import datetime

import cv2
from insightface.app import FaceAnalysis

from config import (
    INSIGHTFACE_MODEL,
    DETECTION_SIZE,
    SIMILARITY_THRESHOLD,
)

from src.camera.camera_manager import CameraManager
from src.database.database_manager import DatabaseManager
from src.recognition.face_recognizer import FaceRecognizer


class RecognitionService:

    def __init__(self):

        self.camera = CameraManager()
        self.recognizer = FaceRecognizer()
        self.db = DatabaseManager()

        self.face_app = FaceAnalysis(
            name=INSIGHTFACE_MODEL,
            providers=["CPUExecutionProvider"]
        )

        self.face_app.prepare(
            ctx_id=0,
            det_size=DETECTION_SIZE
        )

    def mark_attendance(self, employee_id, confidence):

        today = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        if self.db.attendance_exists(employee_id, today):
            return "Attendance Already Marked"

        self.db.mark_attendance(
            employee_id,
            today,
            current_time,
            confidence
        )

        return "Attendance Marked"

    def get_employee(self, employee_id):

        return self.db.get_employee(employee_id)

    def start_recognition(self):

        self.camera.start_camera()

        print("\nStarting Face Recognition...")
        print("Press Q to Exit\n")

        while True:

            frame = self.camera.read_frame()

            if frame is None:
                break

            faces = self.face_app.get(frame)

            for face in faces:

                embedding = face.embedding

                result = self.recognizer.recognize(
                    embedding,
                    threshold=SIMILARITY_THRESHOLD
                )

                x1, y1, x2, y2 = map(int, face.bbox)

                if result["recognized"]:

                    employee = self.get_employee(
                        result["employee_id"]
                    )

                    attendance = self.mark_attendance(
                        result["employee_id"],
                        result["confidence"]
                    )

                    color = (0, 255, 0)

                    if employee:

                        label = employee["name"]

                        cv2.putText(
                            frame,
                            employee["department"],
                            (x1, y2 + 25),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            color,
                            2
                        )

                        cv2.putText(
                            frame,
                            attendance,
                            (x1, y2 + 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            color,
                            2
                        )

                    else:

                        label = result["employee_id"]

                else:

                    color = (0, 0, 255)
                    label = "Unknown"

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    color,
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )

            cv2.imshow(
                "FaceAttend AI - Recognition",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        self.camera.stop_camera()
        cv2.destroyAllWindows()