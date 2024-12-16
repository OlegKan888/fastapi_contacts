from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.database import get_db
from app.services.crud import get_contacts, create_contact, get_contact, delete_contact
from app.services.schemas import ContactBase, ContactCreate
from typing import List

router = APIRouter()

@router.get("/contacts", response_model=List[ContactBase])
def read_contacts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_contacts(db, skip=skip, limit=limit)

@router.post("/contacts", response_model=ContactBase)
def add_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db, contact, user_id=1)  # Замість user_id можна додати авторизацію

@router.delete("/contacts/{contact_id}")
def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    return delete_contact(db, contact_id)
