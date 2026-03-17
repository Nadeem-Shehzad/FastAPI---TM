from pydantic import BaseModel
from typing import List

class UserAI(BaseModel):
    id: str
    name: str
    email: str
    role: str
    skills: List[str]

class UserQuery(BaseModel):
    query: str