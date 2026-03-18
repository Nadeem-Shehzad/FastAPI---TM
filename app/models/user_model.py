from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from typing import Optional, List


class UserRole(str, Enum):
    admin = 'admin',
    user = 'user'


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    role: UserRole
    skills: List[str] = []

    class Config:
        extra = 'forbid'


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: UserRole  


class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None


class UserSearchRequest(BaseModel):
    query: str
    domain: Optional[str] = None 
    n_results: int = 5  


class SimilarUserQuery(BaseModel):
    query: str
    n_results: int = 5     