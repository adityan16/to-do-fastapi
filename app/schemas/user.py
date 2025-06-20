# user.py

from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True
        