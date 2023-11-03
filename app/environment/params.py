import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

# Database
SERVER = os.environ.get("SERVER")
DATABASE = os.environ.get("DATABASE")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
PORT = os.environ.get("PORT")

# MLOPS Paths
LOCAL_MLOPS_DIRECTORY = os.getenv("LOCAL_MLOPS_DIRECTORY") or ".mlops"
PIPELINE_DIRECTORY_HEART_ATTACK = os.path.join("pipelines", "heart-attack")
