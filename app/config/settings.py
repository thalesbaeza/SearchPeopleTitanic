import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    APP_ENV: str = os.getenv("APP_ENV", "production")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "false").lower() == "true"

settings = Settings()