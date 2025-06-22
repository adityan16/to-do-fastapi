# task.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.task import CreateTask, DisplayTask
from app.models.user import User
from app.models.task import Task
from app.services.auth import get_current_user
from app.services.async_crud import AsyncCRUD


router = APIRouter(tags=["task"])

@router.post("/", response_model=CreateTask)
async def create_task(task: CreateTask, db: AsyncSession = Depends(get_db), 
                      current_user: User = Depends(get_current_user)):
    data = task.dict
    data["created_by"] = current_user.id
    return await AsyncCRUD.create(db, Task, data)
    