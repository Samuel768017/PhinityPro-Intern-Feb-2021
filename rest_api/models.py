from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.expression import column, true

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    title =Column(String(255))
    firstname= Column(String(255))
    lastname= Column(String(255))
    email = Column(String(255), unique=True)
    username= Column(String(255))
    password = Column(String(255))
    status = Column(String(255))
    # is_active = Column(Boolean, default=True)

   