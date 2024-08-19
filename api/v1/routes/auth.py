from fastapi import Depends, status, APIRouter, Response, Request,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, relationship
from api.utils.success_response import success_response
from api.v1.models import User
from typing import Annotated
from datetime import datetime, timedelta

from api.v1.schemas.user import UserCreate
from api.utils.email_service import send_mail
from api.db.database import get_db
from api.v1.services.user import user_service

auth = APIRouter(prefix="/auth", tags=["Authentication"])

  
@auth.post("/login", status_code=status.HTTP_200_OK)
def login(login_form:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    #getting username and passwword from form
    username = login_form.username
    password =login_form.password

    #here we authenticate user
    user = user_service.authenticate_user(db,username,password)

    access_token =user_service.create_access_token(user.id)
    refresh_token = user_service.create_refresh_token(user.id)

    response ={"message":"login succesful",
               "access token":access_token,
               "refresh_token": refresh_token}
    return response


