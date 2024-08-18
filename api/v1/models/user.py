import uuid
from sqlalchemy import TIMESTAMP, Column, String, Integer, ForeignKey, Boolean, DateTime, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from datetime import datetime
from api.v1.models.base import Base  # Import Base from the new base.py file




class User(Base):
    __tablename__ = 'users'
    

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))


    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    user_preference = relationship("UserPreference", back_populates="user", uselist=False)
    organizations = relationship("UserOrganization", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    emails = relationship("Email", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    notification_settings = relationship("NotificationSetting", back_populates="user", uselist=False)
    blog_posts = relationship("BlogPost", back_populates="user")
    waitlist = relationship("Waitlist", back_populates="user", uselist=False)
    user_profile = relationship("UserProfile", back_populates="user", uselist=False)
    activity_logs = relationship("ActivityLog", back_populates="user")
    invite_links = relationship("InviteLink", back_populates="user")
    magic_links = relationship("MagicLink", back_populates="user")
    random_data = relationship("RandomData", back_populates="user")
    contact_us = relationship("ContactUs", back_populates="user")



