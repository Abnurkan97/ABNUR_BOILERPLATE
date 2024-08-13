from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file



class EmailTemplate(Base):
    __tablename__ = 'email_templates'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    
    emails = relationship("Email", back_populates="template")
