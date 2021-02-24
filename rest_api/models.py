from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column, true

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname= Column(String(255), index = True)
    lastname= Column(String(255), index = True)
    email = Column(String(255), unique=True, index=True)
    username= Column(String(255), index = True)
    hashed_password = Column(String(255))
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), index=True)
#     description = Column(String(255), index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")