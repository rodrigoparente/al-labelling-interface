# python
from typing import Optional

# third party
from pydantic import BaseModel


class UserForm(BaseModel):
    email: str
    password: str
    username: Optional[str] = None
