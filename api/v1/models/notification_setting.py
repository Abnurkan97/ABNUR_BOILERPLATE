from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file



class NotificationSetting(Base):
    __tablename__ = 'notification_settings'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default= text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    email_notifications = Column(Boolean, default=True)
    push_notifications = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="notification_settings")
