from fastapi import APIRouter
from app.ai.schemas.user_ai_schema import UserAI, UserQuery
from app.ai.services.user_ai_service import add_user_embedding, find_similar_users

router = APIRouter(prefix="/ai/users", tags=["AI Users"])

@router.post("/add")
def add_user(user: UserAI):
    add_user_embedding(user.dict())
    return {"message": "User embedded successfully"}

@router.post("/similar")
def similar_users(query: UserQuery):
    results = find_similar_users(query.query)
    return {"similar_users": results}