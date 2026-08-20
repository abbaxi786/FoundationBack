from pydantic import BaseModel
from fastapi import APIRouter,HTTPException
from db.mongo_connection import database
from lib.hash import HasPassword,VerifyPassword

class SignUp(BaseModel):
    username: str
    email:str
    password:str

class LogIn(BaseModel):
    email: str
    password: str

authRouter = APIRouter()

@authRouter.post('/api/sign_up')
async def SignUp(data:SignUp):

    try:
        existingUser = await database.User.find_one({
            "email": data.email
        })

        if existingUser:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

        hashPassword = HasPassword(data.password)

        user = {
            "username": data.username,
            "password": hashPassword,
            "email": data.email 
        }

        return {
            "success": True,
            "Message": "The account has been created"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "Message": str(e)
            }
        )



    

@authRouter.post('/api/log_in')
async def LogIn(data:LogIn):
    user = await database.User.find_one({
        "email": data.email
    })

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not VerifyPassword(
        data.password,
        user["password_hash"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful"
    }

@authRouter.get("/db-test")
async def database_test():

    result = await database.command("ping")

    return {
        "message": "MongoDB connected",
        "result": result
    }