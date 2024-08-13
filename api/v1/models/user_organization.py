from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file

class UserOrganization(Base):
    __tablename__ = 'user_organizations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default= text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    organization_id = Column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    
    user = relationship("User", back_populates="organizations")
    organization = relationship("Organization", back_populates="users")
