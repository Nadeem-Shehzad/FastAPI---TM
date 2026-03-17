from fastapi import FastAPI, Request
from app.routes.v1 import user_routes
from app.core.exceptions import AppException, register_exception_handlers
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.logging_middleware import logging_middleware
from app.ai.routes.user_ai_routes import router as user_ai_router

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.middleware('http')(logging_middleware)

register_exception_handlers(app)

app.include_router(user_routes.router, prefix='/v1/users',tags=['User'])
app.include_router(user_ai_router)