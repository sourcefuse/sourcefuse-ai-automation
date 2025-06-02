# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gemini_api_key: str
    base_url: str = "https://www.saucedemo.com/"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()