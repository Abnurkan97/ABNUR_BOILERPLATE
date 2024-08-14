#!/usr/bin/env python3
""" The database module
"""
# from sqlalchemy.ext.declarative import declarative_base
import logging
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import create_engine
from api.v1 import models
import psycopg2
from sqlalchemy import text
from api.v1.models.base import Base  # Import Base from the new base.py file
from decouple import config



# Database configurations from env
DB_HOST: str = config("DB_HOST")
DB_PORT: int = config("DB_PORT", cast=int)
DB_USER: str = config("DB_USER")
DB_PASSWORD: str = config("DB_PASSWORD")
DB_NAME: str = config("DB_NAME")
DB_TYPE: str = config("DB_TYPE")


SQLALCHEMY_DATABASE_URL = f'{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Admin@localhost/ABNUR_BOILERPLATE"

engine =create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)


from sqlalchemy.exc import SQLAlchemyError
def get_db():
    db =SessionLocal()  #create session with database
    try:
        yield db
    finally:
        db.close()
        

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        logging.info("Tables created successfully")
    except SQLAlchemyError as e:
        logging.error(f"Error creating tables: {e}")



def check_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return True
    except SQLAlchemyError as e:
        logging.error(f"Database connection failed: {e}")
        return False