from pydantic import BaseModel, Extra

class User(BaseModel):
    name: str
    age: int

    class Config:
        extra = 'forbid'