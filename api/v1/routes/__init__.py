from fastapi import APIRouter
from api.v1.routes.register_user import register

api_version_one = APIRouter(prefix="/api/v1")
api_version_one.include_router(register)
