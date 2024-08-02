from fastapi import Depends, HTTPException, APIRouter, Request, Response, status
from jose import JWTError
from sqlalchemy.orm import Session
from api.utils.success_response import success_response
from api.v1.models.user import User
from api.v1.schemas.contact_us import ContactUsMsg,ContactUsMsgResponse
from api.v1.models.contact_us import ContactUs
from api.v1.services.user import user_service
from api.db.database import get_db

all_contact_msg_id= APIRouter(tags=['Contact-us'])


'''Endpoint to register_specific_contact'''

@all_contact_msg_id.post('/contact-us/messages/',status_code=status.HTTP_200_OK, response_model=ContactUsMsgResponse)
def register_specific_contact_msg(schema: ContactUsMsg,db: Session = Depends(get_db),current_user: User = Depends(user_service.get_current_user)
):
    if not current_user.is_super_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )
    new_contact_msg = ContactUs(**schema.model_dump())
    db.add(new_contact_msg)
    db.commit()
    db.refresh(new_contact_msg)


    return new_contact_msg

'''Endpoint to get specific contact msg'''

@all_contact_msg_id.get('/contact-us/messages/{message_id}',status_code=status.HTTP_200_OK,response_model=ContactUsMsgResponse)
def get_specific_contact_msg(message_id: str,db: Session = Depends(get_db),current_user: User = Depends(user_service.get_current_user)
):  
 
    contact_msg = db.query(ContactUs).filter(ContactUs.id == message_id).first()
    if not current_user.is_super_admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )
    if not contact_msg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"contact message with ID: {message_id} not found")
    
    return contact_msg
