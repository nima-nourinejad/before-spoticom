import os
from typing import Union
from typing import Any
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi import HTTPException
import jwt


class AuthUtil:
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "FAILED_SECRET_KEY")
    if SECRET_KEY == "FAILED_SECRET_KEY":
        raise HTTPException(status_code=500, detail="Internal server error")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def hash_password(self, password: str) -> str:
        return self.PWD_CONTEXT.hash(password)

    def create_access_token(self, username: str) -> str:
        to_encode: dict[str, Union[str, datetime]] = {"sub": username}
        expire: datetime = datetime.now(timezone.utc) + timedelta(
            minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        access_token: str = jwt.encode(
            to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM
        )
        return access_token

    def verify_password(self, plain_password: str, hashed_password: str) -> None:
        if not self.PWD_CONTEXT.verify(plain_password, hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect password")


auth_util = AuthUtil()
