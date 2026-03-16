from fastapi import APIRouter, Depends
from app.services.user_service import user_service, UserService
from app.dependencies.user_dependency import get_user_service
from app.models.user_model import UserCreate, UserResponse

router = APIRouter(prefix='/users',tags=['User'])


@router.get('/', response_model=list[UserResponse], status_code=200)
async def getUsers(
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.getUser()


@router.post('/', response_model=UserResponse, status_code=201)
async def createUser(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.createUser(user)