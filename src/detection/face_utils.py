"""
Utility functions for face visualization.
"""

import cv2


def draw_face(frame, face):

    cv2.rectangle(
        frame,
        (face.x, face.y),
        (face.x + face.width, face.y + face.height),
        (0, 255, 0),
        2,
    )

    confidence = f"{face.confidence * 100:.1f}%"

    cv2.putText(
        frame,
        confidence,
        (face.x, face.y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

    return frame