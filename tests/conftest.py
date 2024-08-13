import sys, os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './..')))



import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.db.database import Base, get_db
from main import app
from fastapi.testclient import TestClient
from decouple import config

DB_HOST: str = config("DB_HOST")
DB_PORT: int = config("DB_PORT", cast=int)
DB_USER: str = config("DB_USER")
DB_PASSWORD: str = config("DB_PASSWORD")
DB_NAME: str = config("DB_NAME")
DB_TYPE: str = config("DB_TYPE")
TEST_DB_NAME ='master_boilerplate_test'

# PostgreSQL test database URL (adjust with your PostgreSQL credentials)
SQLALCHEMY_DATABASE_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{TEST_DB_NAME}"


# Create an engine connected to the PostgreSQL test database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a new database session for each test
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)  # Create tables
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Drop tables after test

# Override the get_db dependency
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
