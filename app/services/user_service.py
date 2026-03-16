from app.models.user_model import UserCreate
from app.core.database import user_collection

class UserService:

    async def getUser(self):
        users = []
        async for user in user_collection.find():
            user["id"] = str(user["_id"])
            users.append(user)
        return users

    async def createUser(self, user:UserCreate):
        user_dict = user.model_dump()
        result = await user_collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)  # convert ObjectId to string
        return user_dict

user_service = UserService()    