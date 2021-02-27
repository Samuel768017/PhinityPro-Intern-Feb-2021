
from pydantic import BaseModel


class UserBase(BaseModel):
    
    firstname: str
    lastname: str
    username: str
    email:str
    password: str

class UserCreate(UserBase):
    
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
     
class User(UserBase):
    id: int
    # is_active: bool
   
    class Config:
        orm_mode = True

