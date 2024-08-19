from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Any, Optional
from uuid_extensions import uuid7
import re

class UserBase(BaseModel):
    '''Base user schema'''

    id: str
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    created_at: datetime

class UserCreate(BaseModel):
    '''Schema to create a user'''
    
    email: EmailStr
    password: str
    

    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    '''Schema to structure token data'''
    
    id: Optional[Any]



class DeactivateUserSchema(BaseModel):
    '''Schema for deactivating a user'''

    reason: Optional[str] = None
    confirmation: bool

