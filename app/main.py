from fastapi import FastAPI, Request
from app.routes.v1 import user_routes
from app.core.exceptions import AppException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.logging_middleware import logging_middleware

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

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exec: AppException):
    return JSONResponse(
        status_code=exec.status_code,
        content={
            'success': False,
            'message': exec.message
        }
    )

app.include_router(user_routes.router, prefix='/v1/users',tags=['User'])