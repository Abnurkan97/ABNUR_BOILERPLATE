from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.v1.models.blog_post import BlogPost
from api.v1.models.user import User

class BlogService:
    '''Blog service functionality'''

    def __init__(self, db: Session):
        self.db = db

    def fetch(self, blog_id: str):
        '''Fetch a blog post by its ID'''
        pass

    def update(self, blog_id: str, title: Optional[str] = None, content: Optional[str] = None, current_user: User = None):
        '''Updates a blog post'''
        
        pass