# auth.py
from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    user_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"

class TokenData(BaseModel):
    user_name: str | None = None