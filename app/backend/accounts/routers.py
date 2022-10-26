# python
from datetime import timedelta

# third party
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

# project
from alli import settings

# app
from .dependencies import authenticate_user
from .dependencies import create_access_token
from .dependencies import get_current_active_user
from .dependencies import get_password_hash
from .forms import UserForm
from .models import Token
from .models import User
from .models import UserInDB

accounts_router = APIRouter(tags=["accounts"])


# ACCOUNTS


@accounts_router.post("/token", response_model=Token)
async def access_token_create(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(request.app.mongodb, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@accounts_router.post("/users/create", response_model=User, status_code=status.HTTP_201_CREATED)
async def users_create(request: Request, user: UserForm):
    """
    Create a new user
    """
    user = UserInDB(**user.dict(), hashed_password=get_password_hash(user.password))
    new_user = await request.app.mongodb["users"].insert_one(jsonable_encoder(user))
    return await request.app.mongodb["users"].find_one({"_id": new_user.inserted_id})


@accounts_router.get("/users/current", response_model=User)
async def users_current(current_user: User = Depends(get_current_active_user)):
    return current_user
