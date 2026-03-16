from app.models.user_model import UserCreate
from motor.motor_asyncio import AsyncIOMotorCollection

class UserService:

    def __init__(self, user_collection: AsyncIOMotorCollection):
        self.user_collection = user_collection

    async def getUser(self):
        users = []
        async for user in self.user_collection.find():
            user["id"] = str(user["_id"])
            users.append(user)
        return users

    async def createUser(self, user:UserCreate):
        user_dict = user.model_dump()
        result = await self.user_collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)  
        return user_dict