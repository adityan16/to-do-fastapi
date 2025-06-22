# __init__.py

from fastapi import FastAPI, APIRouter

from app.api import test
from app.api import auth
from app.api import task
from app.api import user

api_router = APIRouter()

api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(task.router, prefix="/task", tags=["task"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
