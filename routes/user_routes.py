from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.User_repo import UserRepo

router =  APIRouter()

@router.post("/signup")
def signup():
    return {"message":"user created successfully"}

@router.post("/login")
def login():
    return {"message":"user logged in succesfully"}