import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

class Settings(BaseSettings):
    PROJECT_NAME: str = "VoxSync API"
    ENVIRONMENT: str = os.environ["ENVIRONMENT"]
    BASE_URL: str = os.environ["BASE_URL"]
    ALLOWED_ORIGINS:str = os.environ["ALLOWED_ORIGINS"]

    # Database
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    DATABASE_POOL_SIZE: int = os.environ["DATABASE_POOL_SIZE"]
    DATABASE_MAX_OVERFLOW: int = os.environ["DATABASE_MAX_OVERFLOW"]

    # JWT & Auth
    JWT_SECRET_KEY: str = os.environ["JWT_SECRET_KEY"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    ALGORITHM: str = "HS256"

    # Other keys
    

    class Config:
        case_sensitive = True
        

settings = Settings()