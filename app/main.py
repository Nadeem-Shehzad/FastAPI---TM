from fastapi import FastAPI
from app.routes.v1 import user_routes

app = FastAPI()

app.include_router(user_routes.router, prefix='/v1/users',tags=['User'])