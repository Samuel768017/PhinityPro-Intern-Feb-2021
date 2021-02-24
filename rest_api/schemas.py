
from pydantic import BaseModel

class UserBase(BaseModel):
    id:int
    firstname: str
    lastname: str
    username: str
    email:str
    hashed_password: str

class UserCreate(UserBase):
    id :int
    firstname: str
    lastname: str
    username: str
    email: str
    hashed_password: str
     

class User(UserBase):
    id: int
    # is_active: bool
    # items: List[Item] = []

    class Config:
        orm_mode = True

# from pydantic.types import StrIntFloat


# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True        