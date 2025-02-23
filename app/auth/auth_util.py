import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from fastapi import HTTPException


class AuthUtil:
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise HTTPException(status_code=500, detail="Internal server error")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def hash_password(self, password: str) -> str:
        return self.PWD_CONTEXT.hash(password)

    def create_access_token(self, username: str) -> str:
        to_encode = {"sub": username}
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        access_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return access_token

    def verify_password(self, plain_password: str, hashed_password: str):
        if not self.PWD_CONTEXT.verify(plain_password, hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect password")


auth_util = AuthUtil()
