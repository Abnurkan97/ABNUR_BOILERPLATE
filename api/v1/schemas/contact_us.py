from cgitb import text
from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Any, Optional
from uuid_extensions import uuid7
import re



class ContactUsMsg(BaseModel):
    '''Schema for getting contact us msg'''

    full_name: str    
    email: EmailStr
    title: str
    message: str

class ContactUsMsgResponse(BaseModel):
    '''Schema for displaying contact us msg'''

    full_name: str    
    email: EmailStr
    title: str
    message:str
    class Config:
        from_attributes = True