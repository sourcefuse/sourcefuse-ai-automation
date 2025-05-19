# config.py
# import os
# from pydantic_settings import BaseSettings  # Updated import
#
# class Settings(BaseSettings):
#     gemini_api_key: str = os.getenv("Gemini_API_Key", "AIzaSyBl4tr07rY2AvmKGhbvspwXaX9x430zlbA")
#     base_url: str = "https://www.saucedemo.com/"
#
# settings = Settings()

# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gemini_api_key: str
    base_url: str = "https://www.saucedemo.com/"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()