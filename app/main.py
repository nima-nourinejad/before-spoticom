from fastapi import FastAPI
from app.middleware import add_cors_middleware
from app.auth_router import auth_router

app = FastAPI()
add_cors_middleware(app)
app.include_router(auth_router)
