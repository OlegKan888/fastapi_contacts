from app.auth.jwt_handler import create_access_token
from app.services.models import User  # Імпорт моделі користувача
from datetime import timedelta
from fastapi import HTTPException
from app.services.crud import get_user_by_email

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_user(db, user_data):
    user = get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(**user_data.dict())
    db.add(new_user)
    db.commit()
    return new_user

def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not user.verify_password(password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": user.email}, access_token_expires)
    return access_token
