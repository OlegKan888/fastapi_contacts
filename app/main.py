import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from app.routers import contacts, users, avatar

app = FastAPI()

# Підключення маршрутів
app.include_router(contacts.router, prefix="/contacts", tags=["Contacts"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(avatar.router, prefix="/avatar", tags=["Avatar"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Contacts API"}
