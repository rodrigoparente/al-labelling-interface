# python
import uuid
from datetime import datetime
from typing import Optional

# third party
from pydantic import BaseModel
from pydantic import Field


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    created: Optional[datetime] = Field(default_factory=datetime.now)
    active: Optional[bool] = True
    email: str
    username: Optional[str] = None
    name: Optional[str] = None
    active_learning_model: Optional[int] = None
    amount_labelled_instances: Optional[int] = None

    class Config:
        allow_population_by_field_name = True


class UserInDB(User):
    hashed_password: str
