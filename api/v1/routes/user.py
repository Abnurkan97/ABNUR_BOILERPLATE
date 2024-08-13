from fastapi import Depends, HTTPException, APIRouter, Request, Response, status
from jose import JWTError
from sqlalchemy.orm import Session
from api.utils.success_response import success_response
from api.v1.models.user import User
from api.v1.schemas.user import DeactivateUserSchema, UserBase,UserCreate
from api.db.database import get_db
from api.v1.services.user import user_service


user = APIRouter(prefix='/users', tags=['Users'])


