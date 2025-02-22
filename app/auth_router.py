
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import AuthResponseSchema, LoginRequestSchema, SignupRequestSchema
from app.database import database
from app.models import User



auth_router = APIRouter(prefix="/authentication", tags=["authentication"])


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

import os
from datetime import datetime, timedelta
import jwt

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(username: str) -> str:
    to_encode = {"sub": username}
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token



@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    hashed_password = hash_password(request.password)
    user = User(
        name=request.name,
        email=request.email,
        hashed_password = hashed_password
    )
    session.add(user)
    session.commit()
    access_token = create_access_token(user.email)
    return AuthResponseSchema(
        access_token=access_token,
        token_type="bearer"
    )


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    request: LoginRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    user = session.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    if not pwd_context.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    access_token = create_access_token(user.email)
    return AuthResponseSchema(
        access_token=access_token,
        token_type="bearer"
    )