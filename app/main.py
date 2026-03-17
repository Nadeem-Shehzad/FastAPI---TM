from fastapi import FastAPI, Request
from app.routes.v1 import user_routes
from app.core.exceptions import AppException
from fastapi.responses import JSONResponse


app = FastAPI()

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