from app.models.user_model import UserCreate, UpdateUser, UserSearchRequest
from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from app.core.exceptions import AppException
from app.ai.services.user_ai_service import add_user_embedding
from app.ai.embeddings.gemini_embed import get_embedding
from app.ai.db.chroma_client import users_collection


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

        print("🔥 Calling add_user_embedding")  # DEBUG

        # 🔹 Add embedding to vector DB AFTER storing in MongoDB
        add_user_embedding(user_dict)

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
    

    async def searchUser(self, search: UserSearchRequest):
        query_embedding = get_embedding(search.query)
        where_filter = {"domain": search.domain} if search.domain else None

        results = users_collection.query(
            query_embeddings=[query_embedding],
            n_results=search.n_results,
            where=where_filter
        )

        # return document (user text) or metadata
        users = []
         # 🔥 ADD THRESHOLD FILTER
        THRESHOLD = 0.6   # tune this (0.2 strict, 0.4 loose)

        for doc, meta, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            if distance <= THRESHOLD:   # ✅ ONLY relevant users
                users.append({
                    "user_text": doc,
                    "email": meta.get("email"),
                    "role": meta.get("role"),
                    "skills": meta.get("skills"),
                    "score": distance   # helpful for debugging
                })

                print("Distances:", results["distances"][0])    

        return {"results": users}
    