from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserSchema(BaseModel):
    id: int
    username: Optional[str] = None
    email: EmailStr
    face_encoding: Optional[List[float]] = None

    class Config:
        from_attributes = True