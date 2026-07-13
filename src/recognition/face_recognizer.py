"""
Face Recognizer

Loads all employee embeddings and performs
face recognition using cosine similarity.
"""

from pathlib import Path

import numpy as np


class FaceRecognizer:
    """
    Handles face recognition using saved embeddings.
    """

    def __init__(self):

        self.embeddings = {}

        self.load_embeddings()

    def load_embeddings(self):
        """
        Load all employee embeddings.
        """

        embedding_folder = Path("models/embeddings")

        if not embedding_folder.exists():
            print("Embedding folder not found.")
            return

        embedding_files = embedding_folder.glob("*.npy")

        count = 0

        for file in embedding_files:

            employee_id = file.stem

            embedding = np.load(file)

            self.embeddings[employee_id] = embedding

            count += 1

        print(f"{count} employee embeddings loaded.")

    def cosine_similarity(self, emb1, emb2):
        """
        Compute cosine similarity.
        """

        return np.dot(emb1, emb2) / (
            np.linalg.norm(emb1) *
            np.linalg.norm(emb2)
        )

    def recognize(self, live_embedding, threshold=0.55):
        """
        Compare live embedding against all employees.
        """

        best_employee = None
        best_score = -1

        for employee_id, stored_embedding in self.embeddings.items():

            score = self.cosine_similarity(
                live_embedding,
                stored_embedding
            )

            if score > best_score:
                best_score = score
                best_employee = employee_id

        if best_score >= threshold:

            return {
                "recognized": True,
                "employee_id": best_employee,
                "confidence": round(float(best_score), 4)
            }

        return {
            "recognized": False,
            "employee_id": None,
            "confidence": round(float(best_score), 4)
        }