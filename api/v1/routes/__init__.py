from fastapi import APIRouter
from api.v1.routes.auth import auth
from api.v1.routes.newsletter import newsletter
from api.v1.routes.user import user
from api.v1.routes.testimonial import testimonial
from api.v1.routes.blog import blog
from api.v1.routes.contact_us import all_contact_msg_id

api_version_one = APIRouter(prefix="/api/v1")
api_version_one.include_router(auth)
api_version_one.include_router(newsletter)
api_version_one.include_router(user)
#This is a route for getting specific contact us msg by super admin
api_version_one.include_router(all_contact_msg_id)
