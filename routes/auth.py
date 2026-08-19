from pydantic import BaseModel
from fastapi import APIRouter

class SignUp(BaseModel):
    username: str
    email:str
    password:str

class LogIn(BaseModel):
    email: str
    password: str

authRouter = APIRouter()

@authRouter.post('/api/sign_up')
def SignUp(data:SignUp):
    return{
        "message": f"{data.username} has created account with email {data.email}"
    }
    pass

@authRouter.post('/api/log_in')
def LogIn(data:LogIn):
    return{
        "message": f"The user with {data.email} email had log in !!!"
    }