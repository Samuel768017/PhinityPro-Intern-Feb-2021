# from main import db_session_middleware
from sqlalchemy.orm import Session
from models import  User 
import schemas


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_login(db: Session, username: str, password: str):
    return db.query(User).filter(User.username == username, User.password == password).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# def decode_token(token):
#     # This doesn't provide any security at all
#     # Check the next version
#     user = get_user(db_session_middleware, token)
#     return user

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + ""
    db_user = User(firstname=user.firstname, lastname=user.lastname, username=user.username, email=user.email, password=fake_hashed_password,status=user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_login(db: Session, user: schemas.UserBase):
    fake_hashed_password = user.password + ""
    db_user = User(username=user.username, password=fake_hashed_password)
    # db.add(db_user)
    # db.commit()
    db.refresh(db_user)
    return db_user





