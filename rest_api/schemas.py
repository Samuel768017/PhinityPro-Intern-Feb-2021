
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    
    firstname: str
    lastname: str
    username: str
    email:str
    password: str
    status: Optional[str] = None
class UserCreate(UserBase):
    
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
    status:Optional[str] = None
     
class User(UserBase):
    id: int
    # is_active: bool
   
    class Config:
        orm_mode = True

