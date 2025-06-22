# app/schemas/task.py

from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional


class CreateTask(BaseModel):
    name: str
    description: Optional[str]= None
    last_date: Optional[datetime]= None
    priority: Literal["high", "medium", "low"] = "medium"

class DisplayTask(BaseModel):
    id: int
    name: str
    description: str
    created_At: datetime
    last_day: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: str
    priority: str
    is_completed: bool

    class Config:
        orm_mode = True