"""
Project Configuration
FaceAttend AI
"""

from pathlib import Path

# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATASET_DIR = BASE_DIR / "dataset"
EMBEDDINGS_DIR = BASE_DIR / "embeddings"
ATTENDANCE_DIR = BASE_DIR / "attendance"
LOGS_DIR = BASE_DIR / "logs"
MODELS_DIR = BASE_DIR / "models"

# =====================================================
# DATABASE
# =====================================================

DATABASE_PATH = DATABASE_DIR / "employees.db"

# =====================================================
# CAMERA
# =====================================================

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# =====================================================
# REGISTRATION
# =====================================================

IMAGES_PER_EMPLOYEE = 20

# =====================================================
# FACE RECOGNITION
# =====================================================

SIMILARITY_THRESHOLD = 0.65

# =====================================================
# ANTI SPOOF
# =====================================================

LIVENESS_THRESHOLD = 0.80

# =====================================================
# ATTENDANCE
# =====================================================

ATTENDANCE_FILE = ATTENDANCE_DIR / "attendance.csv"