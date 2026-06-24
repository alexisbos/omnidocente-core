import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_key")
    DB_PATH = os.getenv("DB_PATH", "data/lms.db")