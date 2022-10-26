# third party
from fastapi import APIRouter
from fastapi import Request
from fastapi import status
from fastapi.encoders import jsonable_encoder

# project
from .dependencies import get_password_hash
from .models import User
from .forms import UserForm
from .models import UserInDB

accounts_router = APIRouter(tags=["accounts"])


# ACCOUNTS


@accounts_router.post("/users/create", response_model=User, status_code=status.HTTP_201_CREATED)
async def users_create(request: Request, user: UserForm):
    """
    Create a new user
    """
    user = UserInDB(**user.dict(), hashed_password=get_password_hash(user.password))
    new_user = await request.app.mongodb["users"].insert_one(jsonable_encoder(user))
    return await request.app.mongodb["users"].find_one({"_id": new_user.inserted_id})
