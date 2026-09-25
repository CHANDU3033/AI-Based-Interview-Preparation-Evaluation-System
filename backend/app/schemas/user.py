import sys, os
_backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _backend_dir not in sys.path: sys.path.insert(0, _backend_dir)
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    target_role: Optional[str] = None
    education: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    target_role: Optional[str] = None
    education: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None
    experience_years: Optional[float] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    target_role: Optional[str] = None
    education: Optional[str] = None
    college: Optional[str] = None
    branch: Optional[str] = None
    experience_years: Optional[float] = 0.0
    role: str
    created_at: Optional[datetime] = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
