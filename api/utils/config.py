import os
# Define your JWT secret and algorithm
ALGORITHM = os.getenv("ALGORITHM", "HS256")
SECRET_KEY = os.getenv("SECRET_KEY", "MY SECRET KEY")
