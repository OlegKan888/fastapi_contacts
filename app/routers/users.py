from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.auth.auth import create_user, authenticate_user
from app.services.schemas import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)

@router.post("/login")
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user_data.email, user_data.password)
