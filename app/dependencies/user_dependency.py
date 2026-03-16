from fastapi import Depends
from app.services.user_service import UserService
from app.dependencies.db_dependency import get_user_collection
from motor.motor_asyncio import AsyncIOMotorCollection


def get_user_service(user_collection: AsyncIOMotorCollection = Depends(get_user_collection)):
    return UserService(user_collection)