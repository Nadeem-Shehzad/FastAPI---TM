from app.models.user_model import User


class UserService:

    def getUser(self):
        return {
        'name': 'Nadeem',
        'age': 24
    }

    def createUser(self, user:User):
        user_dict = user.model_dump()
        return {
            "message": "User created",
            "user": user_dict
        }

user_service = UserService()    