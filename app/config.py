import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", "app/database/database.db")