from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import SignupRequestSchema
from app.auth_util import auth_util


class DatabaseUtil:
    def add_user(self, request: SignupRequestSchema, session: Session):
        hashed_password = auth_util.hash_password(request.password)
        user = User(
            name=request.name, email=request.email, hashed_password=hashed_password
        )
        session.add(user)
        session.commit()

    def get_user(self, email: str, session: Session) -> User:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user


database_util = DatabaseUtil()
