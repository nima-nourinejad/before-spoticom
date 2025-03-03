from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.schemas import SignupRequestSchema
from app.auth.auth_util import auth_util


class DatabaseUtil:
    def add_user(self, request: SignupRequestSchema, session: Session) -> None:
        user = self.__find_user(request.email, session)
        if user:
            raise HTTPException(status_code=409, detail="User already exists")
        hashed_password = auth_util.hash_password(request.password)
        user = User(
            name=request.name, email=request.email, hashed_password=hashed_password
        )
        session.add(user)
        session.commit()

    def get_user_with_username(self, username: str, session: Session) -> User:
        user = self.__find_user(username, session)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def __find_user(self, email: str, session: Session) -> Optional[User]:
        user = session.query(User).filter(User.email == email).first()
        return user

    def get_user_from_access_token(
        self, access_token: str, session: Session
    ) -> Optional[User]:
        username = auth_util.get_username_from_access_token(access_token)
        user = self.__find_user(username, session)
        if not user:
            raise auth_util.CREDENTIALS_EXCEPTION
        return user


database_util = DatabaseUtil()
