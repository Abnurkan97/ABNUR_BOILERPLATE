from fastapi import status

LOGIN_ENDPOINT = 'api/v1/auth/login'
REGISTER_ENDPOINT = 'api/v1/auth/register'


def test_login(client):
    register_response = client.post(REGISTER_ENDPOINT,
                           json={
                                "email": "kaka@example.com",
                                "password": "kaka123"
                                })
  

    login_response = client.post(LOGIN_ENDPOINT,
                           data={
                                "username": "kaka@example.com",
                                "password": "kaka123"
                                })


    
    assert login_response.status_code == status.HTTP_200_OK    
    response_data = login_response.json()
    access_token = response_data.get("access token")
    refresh_token = response_data.get("refresh_token")
    
    # Check if the tokens are present and are strings
    assert isinstance(access_token, str)
    assert isinstance(refresh_token, str)
    assert login_response.json().get("message") == "login succesful"
   
def test_login_invalid(client):
    register_response = client.post(REGISTER_ENDPOINT,
                           json={
                                "email": "kaka@example.com",
                                "password": "kaka123"
                                })
  

    login_response = client.post(LOGIN_ENDPOINT,
                           data={
                                "username": "kaka2@example.com",
                                "password": "kaka123"
                                })


    
    assert login_response.status_code == status.HTTP_400_BAD_REQUEST    
   
