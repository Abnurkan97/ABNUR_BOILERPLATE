from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file


class NotificationTemplate(Base):
    __tablename__ = 'notification_templates'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default= text("gen_random_uuid()"))
    message = Column(Text, nullable=False)
    
    notifications = relationship("Notification", back_populates="template")
