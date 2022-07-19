from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None