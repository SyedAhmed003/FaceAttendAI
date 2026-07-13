"""
Embedding Generator

Generates a single face embedding for each employee
using all registered images.
"""

from pathlib import Path

import cv2
import numpy as np
from insightface.app import FaceAnalysis


class EmbeddingGenerator:
    """
    Generates and saves employee face embeddings.
    """

    def __init__(self):

        # Load InsightFace model
        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def generate_embedding(self, employee_folder, employee_id):
        """
        Generate average embedding for one employee.
        """

        employee_folder = Path(employee_folder)

        image_files = sorted(employee_folder.glob("*.jpg"))

        if len(image_files) == 0:
            print("No images found.")
            return False

        embeddings = []

        print(f"\nProcessing {len(image_files)} images...\n")

        for image_path in image_files:

            image = cv2.imread(str(image_path))

            if image is None:
                continue

            faces = self.app.get(image)

            if len(faces) == 0:
                continue

            embedding = faces[0].embedding

            embeddings.append(embedding)

            print(f"Processed : {image_path.name}")

        if len(embeddings) == 0:

            print("No valid faces detected.")

            return False

        # Average embedding
        average_embedding = np.mean(embeddings, axis=0)

        # Normalize
        average_embedding = average_embedding / np.linalg.norm(
            average_embedding
        )

        # Save
        save_folder = Path("models/embeddings")
        save_folder.mkdir(parents=True, exist_ok=True)

        save_path = save_folder / f"{employee_id}.npy"

        np.save(save_path, average_embedding)

        print("\nEmbedding Generated Successfully")
        print(save_path)

        return True