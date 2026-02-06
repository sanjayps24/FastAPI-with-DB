from fastapi import APIRouter

router =  APIRouter()

@router.post("/signup")
def signup():
    return {"message":"user created successfully"}

@router.post("/login")
def login():
    return {"message":"user logged in succesfully"}