# from collections import UserDict, UserString
import unittest
from typing import List, Optional
from fastapi import Request, Form
from fastapi import Response


from fastapi import Depends, FastAPI, HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import secrets
import uvicorn
import crud, schemas
from  models import Base
from  database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db(request: Request):
    return request.state.db


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/users/authenticate/", response_model=schemas.User)
async def user_login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("Authentication called")
    print(user.username)
    print(user.password)
    db_user = crud.get_user_login(db,username = user.username, password = user.password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="username and password not found")
    return db_user

# @app.post("/users/authenticate/", response_model=schemas.User)
# async def user_login(user:schemas.UserBase, db : Session = Depends(get_db)):
#     print("Authentication called")
#     #print(user.username)
#     #print(user.password)
#     #console.log("Authentication called");
#     db_user = crud.get_user_login(db,username = user.username, password = user.password)
#     #db_user=crud.user_login(db,username=username,password=password);
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="usename or password not correct")
#     return db_user

# @app.post("/users/authenticate/", response_model=schemas.User)
# async def user_login(user:schemas.UserBase, db : Session = Depends(get_db)):
#     print("Authentication called")
#     db_user = crud.get_user_login(db,username = username, password = password)
#     #db_user=crud.user_login(db,username=username,password=password);
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="usename or password not correct")
#     return db_user

@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user 

 
@app.get("/users/authenticate/",response_model=schemas.User)
def get_user_login(username:str, password:str, db : Session = Depends(get_db)):
    db_user = crud.get_user_login(db,username = username, password = password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="credentials not found")
    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user_by_id(db, user_id=user_id)
    return db_user 


# @app.post("/users/authenticate/", response_model=schemas.User)
# async def user_login(user: schemas.UserBase, db: Session = Depends(get_db)):
#     db_user = crud.get_user_login(db, username=user.username,password=user.password)
#     if db_user:
#         raise HTTPException(status_code=400, detail="username is not load")
#     return crud.user_login(db_user, user=user.username)


# async def user_login(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_login(db,username = user.username,password=user.password)
#     if db_user:
#         raise HTTPException(status_code=400, detail="usename or password not correct")
#     return crud.create_user(db=db, user=user)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000 , reload=True, access_log=False)   