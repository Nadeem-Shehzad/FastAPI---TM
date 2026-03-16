from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient

#load settings from .env
class Settings(BaseSettings):
    MONGO_URI: str

    class Config:
        env_file = ".env"

settings = Settings()

#connect to MongoDB

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client["TM"] # db defined in uri
user_collection = database.get_collection('users')