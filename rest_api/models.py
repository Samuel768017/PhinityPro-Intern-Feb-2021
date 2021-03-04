from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.expression import column, true

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname= Column(String(255), index = True)
    lastname= Column(String(255), index = True)
    email = Column(String(255), unique=True, index=True)
    username= Column(String(255), index = True)
    password = Column(String(255))
    status = Column(String(255),index = True)
    # is_active = Column(Boolean, default=True)

   