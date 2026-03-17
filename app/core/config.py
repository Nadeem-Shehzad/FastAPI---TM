from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    
    MONGO_URI: str
    DB_NAME: str = 'TM'

    APP_NAME: str
    DEBUG: bool = True

    GEMINI_API_KEY:str

    class Config: 
        env_file = ".env"
        env_file_encoding = "utf-8"

# chache settings, so it loads only once
@lru_cache
def get_settings():
    return Settings()


settings = get_settings()