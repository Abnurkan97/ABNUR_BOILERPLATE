## Description

This pull request implements an API endpoint for user login. The endpoint allows created users to login to his/her account by providing necessary details such  email and password.

### Endpoint Details

- **HTTP Method:** POST
- **Endpoint URL:** `/api/v1/auth/login`
- **Request Payload:**
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }


## Response:

- 200 Success: User successfully login.
- 400 Bad Request: Invalid input data (e.g., missing fields, invalid email format).
- 500 Internal Server Error: If there is a server-side error.

## Type of change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?

 Unit Tests
 Integration Tests
 Manual Testing

## Test Configuration:
Operating System:
Browser:
API Client (e.g., Postman):

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented on my code, particularly in hard-to-understand areas
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules

##  Screenshots (if applicable):
If applicable, add screenshots to help explain your changes.