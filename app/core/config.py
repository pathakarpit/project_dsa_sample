import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PPROJECT_NAME: str = "wine_me__up"
    API_KEY: str = os.getenv("API_KEY", "safe-default-key")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "safe-default-secret")
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = os.getenv("REDIS_URLL", "redis://localhost:6379/0")

    MODEL_DIR: str = "app/models"
    MODEL_NAME: str = "default_model.joblib"
    MODEL_PATH: str = os.path.join(MODEL_DIR, MODEL_NAME)

    ENV: str = os.getenv("ENV", "development")

    @classmethod
    def set_model_name(cls, name: str) -> None:
        cls.MODEL_NAME = name
        cls.MODEL_PATH = os.path.join(cls.MODEL_DIR, cls.MODEL_NAME)

settings = Settings()
