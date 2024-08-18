from fastapi import Depends, status, APIRouter, Response, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, relationship
from api.utils.success_response import success_response
from api.v1.models import User
from typing import Annotated
from datetime import datetime, timedelta

from api.v1.schemas.user import UserCreate
from api.db.database import get_db
from api.v1.services.user import user_service

reg = APIRouter(prefix="/re", tags=["registration"])

@reg.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_schema: UserCreate, db: Session = Depends(get_db)):
    '''Endpoint for a user to register their account'''

    #check if email exist
    check_email = db.query(User).filter(User.email == user_schema.email).first()
    
    if check_email:
        raise HTTPException(status_code=400,detail="Email already exist")
    
    hashed_password = user_service.hash_password(user_schema.password)
    user_schema.password = hashed_password

    new_user = User(**user_schema.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "registered succesfully"}
