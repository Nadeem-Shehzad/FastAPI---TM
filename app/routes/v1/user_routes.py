from fastapi import APIRouter, Depends
from app.models.user_model import UserCreate, UserResponse, UpdateUser
from app.services.user_service import UserService
from app.dependencies.user_dependency import get_user_service
from app.core.exceptions import AppException


router = APIRouter()

# create user
@router.post('/', response_model=UserResponse, status_code=201)
async def createUser(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    return await user_service.createUser(user)


# get users
@router.get('/', response_model=list[UserResponse], status_code=200)
async def getUsers(user_service: UserService = Depends(get_user_service)):
    return await user_service.getUser()


# get user
@router.get('/{id}', response_model=UserResponse, status_code=200)
async def getOneUser(id: str, user_service: UserService = Depends(get_user_service)):
    user = await user_service.getOneUser(id)
    return user


# update user
@router.patch('/{user_id}', response_model= UserResponse, status_code= 200)
async def updateUser(user_id: str, user_data: UpdateUser, user_service: UserService = Depends(get_user_service)):
    updated_user = await user_service.updateUser(user_id, user_data)
    return updated_user


# delete user
@router.delete('/{user_id}')
async def deleteUser(user_id: str, user_service: UserService = Depends(get_user_service)):
    deleted = await user_service.deleteUser(user_id)

    return deleted