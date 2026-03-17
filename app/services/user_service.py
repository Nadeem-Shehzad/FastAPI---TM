from app.models.user_model import UserCreate, UpdateUser
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from app.core.exceptions import AppException


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


    async def getOneUser(self, id: str):
        try:
            user = await self.user_collection.find_one({'_id': ObjectId(id)})
        except Exception:
            raise AppException("Invalid user ID", 400)

        if not user:
            raise AppException('User Not Found', 404)

        user['id'] = str(user['_id'])

        return user  


    async def updateUser(self, user_id:str, user_data: UpdateUser):
        if not ObjectId.is_valid(user_id):
            raise AppException('Invalid User ID', 400)
        
        update_dict = {k: v for k, v in user_data.dict(exclude_unset=True).items()}

        if not update_dict:
            raise AppException("No fields provided for update", 400)
        
        result = await self.user_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_dict}
        )

        if result.matched_count == 0:
            raise AppException('User not Found', 404)
        
        user = await self.user_collection.find_one({"_id": ObjectId(user_id)})
        user['id'] = str(user['_id'])
        return user
    

    async def deleteUser(self, user_id: str):
        if not ObjectId.is_valid(user_id):
            raise AppException('Invalid User ID', 400)
        
        result = await self.user_collection.delete_one({'_id': ObjectId(user_id)})

        if result.deleted_count == 0:
            raise AppException('User Not Deleted', 500)
        
        return {"message": "User deleted successfully", "user_id": user_id}