from fastapi import Depends
from app.services.user_service import UserService
from app.dependencies.db_dependency import get_user_collection


def get_user_service(
        user_collection = Depends(get_user_collection)
):
    return UserService(user_collection)