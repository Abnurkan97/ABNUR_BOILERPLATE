from fastapi import status

REGISTER_ENDPOINT = 'api/v1/re/register'


def test_register_user(client):
    register_response = client.post(REGISTER_ENDPOINT,
                           json={
                                "email": "kaka@example.com",
                                "password": "kaka123"
                                })
    assert register_response.status_code == status.HTTP_201_CREATED
    assert register_response.json() == {"message": "registered succesfully"}

