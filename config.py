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
MODELS_DIR = BASE_DIR / "models"
LOGS_DIR = BASE_DIR / "logs"
ATTENDANCE_DIR = BASE_DIR / "attendance"

# =====================================================
# DATABASE
# =====================================================

DATABASE_PATH = DATABASE_DIR / "employees.db"

# =====================================================
# DATASET
# =====================================================

EMPLOYEE_DATASET = DATASET_DIR / "employees"
UNKNOWN_DATASET = DATASET_DIR / "unknown"

# =====================================================
# MODELS
# =====================================================

EMBEDDINGS_PATH = MODELS_DIR / "embeddings"

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

# InsightFace Model
INSIGHTFACE_MODEL = "buffalo_l"

# Detection Size
DETECTION_SIZE = (640, 640)

# =====================================================
# ANTI SPOOF
# =====================================================

LIVENESS_THRESHOLD = 0.80

# =====================================================
# ATTENDANCE
# =====================================================

ATTENDANCE_FILE = ATTENDANCE_DIR / "attendance.csv"

# =====================================================
# CREATE REQUIRED DIRECTORIES
# =====================================================

DATABASE_DIR.mkdir(parents=True, exist_ok=True)
DATASET_DIR.mkdir(parents=True, exist_ok=True)
EMPLOYEE_DATASET.mkdir(parents=True, exist_ok=True)
UNKNOWN_DATASET.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)
EMBEDDINGS_PATH.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
ATTENDANCE_DIR.mkdir(parents=True, exist_ok=True)