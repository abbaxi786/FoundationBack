from fastapi import FastAPI
from routes.auth import authRouter

app = FastAPI()




@app.get("/")
def root():
    return {
        "message": "Integrated Reservation System API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

app.include_router(authRouter)