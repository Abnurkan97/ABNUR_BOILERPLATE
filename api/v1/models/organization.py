from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file


class Organization(Base):
    __tablename__ = 'organizations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default= text("gen_random_uuid()"))
    name = Column(String, nullable=False)
    
    users = relationship("UserOrganization", back_populates="organization")
    activity_logs = relationship("ActivityLog", back_populates="organization")
    payments = relationship("Payment", back_populates="organization")

