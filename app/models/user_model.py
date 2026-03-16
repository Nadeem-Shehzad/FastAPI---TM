from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class UserRole(str, Enum):
    admin = 'admin',
    user = 'user'

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    role: UserRole

    class Config:
        extra = 'forbid'

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: UserRole  