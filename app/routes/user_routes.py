from fastapi import APIRouter


router = APIRouter(prefix='/users',tags=['User'])

@router.get('/')
def getUsers():
    return {
        'name': 'Nadeem',
        'age': 24
    }