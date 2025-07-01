# api/auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import UserRegister, UserLogin
from app.services.user import create_user, get_user_by_email, get_user_by_username
from app.db.database import get_db

router = APIRouter(tags=["auth"])

@router.post("/register")
async def register_user(user: UserRegister, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_username(db, user.user_name)
    if existing_user:
        raise HTTPException(status_code=400, detail="User Name already exists.")
    new_user = await create_user(db, user)
    return {"message": "User registered successfully", "username": new_user.user_name}