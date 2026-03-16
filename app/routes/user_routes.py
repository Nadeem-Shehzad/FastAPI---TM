from fastapi import APIRouter
from app.services.user_service import user_service
from app.models.user_model import User


router = APIRouter(prefix='/users',tags=['User'])

@router.get('/')
def getUsers():
    return user_service.getUser()


@router.post('/')
def createUser(user: User):
    return user_service.createUser(user)