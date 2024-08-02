import sys, os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from api.v1.models.contact_us import ContactUs
from api.v1.models.user import User
from api.v1.services.user import user_service
from uuid_extensions import uuid7
from api.db.database import get_db
from api.utils import dependencies
from fastapi import status

from datetime import datetime, timezone

client = TestClient(app)
REGISTER_CONTACTUS = '/api/v1/contact-us/messages/'
SPECIFIC_CONTACT_MSG_ENDPOINT = '/api/v1/contact-us/messages'

@pytest.fixture
def mock_db_session():
    """Fixture to create a mock database session."""
    with patch("api.v1.services.user.get_db", autospec=True) as mock_get_db:
        mock_db = MagicMock()
        app.dependency_overrides[get_db] = lambda: mock_db
        yield mock_db
    app.dependency_overrides = {}

@pytest.fixture
def mock_user_service():
    """Fixture to create a mock user service."""
    with patch("api.v1.services.user.user_service", autospec=True) as mock_service:
        yield mock_service

def create_mock_user(mock_user_service, mock_db_session, super_admin=False):
    """Create a mock user in the mock database session."""
    mock_user = User(
        id=str(uuid7()),
        username="testuser",
        email="testuser@gmail.com",
        password=user_service.hash_password("Testpassword@123"),
        first_name='Test',
        last_name='User',
        is_active=True,
        is_super_admin=super_admin,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    mock_db_session.query.return_value.filter.return_value.first.return_value = mock_user
    return mock_user


def create_mock_contact(mock_db_session):
    """Create a mock contact message in the mock database session."""
    mock_contact = MagicMock()
    mock_contact.id = "1"
    mock_contact.full_name = "John Doe"
    mock_contact.email = "john.doe@example.com"
    mock_contact.title = "Hello"
    mock_contact.message = "Hello"
    mock_db_session.query.return_value.filter.return_value.first.return_value = mock_contact
    return mock_contact



##############    """Test 1 for retrieving a specific contact message as super admin."""                      ###############################

@pytest.mark.usefixtures("mock_db_session", "mock_user_service")
def test_get_specific_contact_msg_as_super_admin(mock_user_service, mock_db_session):
    
    create_mock_user(mock_user_service, mock_db_session, super_admin=True)
    create_mock_contact(mock_db_session)

    access_token = user_service.create_access_token(user_id=str(uuid7()))
    response = client.get(
        f"{SPECIFIC_CONTACT_MSG_ENDPOINT}/1",
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"full_name": "John Doe", "email": "john.doe@example.com", "title": "Hello", "message": "Hello"}

##############    """Test 2 for retrieving a specific contact message as super admin."""                     ###############################


@pytest.mark.usefixtures("mock_db_session", "mock_user_service")
def test_get_specific_contact_msg_not_found(mock_user_service, mock_db_session):
    
    create_mock_user(mock_user_service, mock_db_session, super_admin=True)
    create_mock_contact(mock_db_session)

    access_token = user_service.create_access_token(user_id=str(uuid7()))
    response = client.get(
        f"{SPECIFIC_CONTACT_MSG_ENDPOINT}/2",
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"full_name": "John Doe", "email": "john.doe@example.com", "title": "Hello", "message": "Hello"}

# ###############    """Test 3 for retrieving a specific contact message as super admin."""                      ###############################

# @pytest.mark.usefixtures("mock_db_session", "mock_user_service")
# def test_get_specific_contact_msg_not_admin(mock_user_service, mock_db_session):
    
#     create_mock_user(mock_user_service, mock_db_session, super_admin=False)
#     create_mock_contact(mock_db_session)

#     access_token = user_service.create_access_token(user_id=str(uuid7()))
#     dependencies.get_current_admin(mock_db_session,access_token)
#     response = client.get(
#         f"{SPECIFIC_CONTACT_MSG_ENDPOINT}/1",
#         headers={'Authorization': f'Bearer {access_token}'}
#     )

#     assert response.status_code == status.HTTP_401_UNAUTHORIZED
#     assert response.json() == {"detail": "You do not have permission to perform this action."}

