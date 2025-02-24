from sqlalchemy.orm import Session
from app.schemas.schemas import (
    AuthResponseSchema,
    SignupRequestSchema,
)
from app.auth.auth_util import auth_util
from app.database.database_util import database_util


class AuthRouterUtil:
    @staticmethod
    def signup(request: SignupRequestSchema, session: Session) -> AuthResponseSchema:
        database_util.add_user(request, session)
        access_token = auth_util.create_access_token(request.email)
        return AuthResponseSchema(access_token=access_token, token_type="bearer")

    @staticmethod
    def login(username: str, password: str, session: Session) -> AuthResponseSchema:
        user = database_util.get_user_with_username(username, session)
        auth_util.verify_password(password, user.hashed_password)
        access_token = auth_util.create_access_token(user.email)
        return AuthResponseSchema(access_token=access_token, token_type="bearer")
