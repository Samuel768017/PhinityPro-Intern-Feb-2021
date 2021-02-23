from typing import List, Optional

from pydantic import BaseModel
# from pydantic.types import StrIntFloat


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    firstname:str
    lastname:str
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True