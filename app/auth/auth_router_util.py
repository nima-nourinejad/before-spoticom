from sqlalchemy.orm import Session
from app.schemas.schemas import (
    AuthResponseSchema,
    LoginRequestSchema,
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
    def login(request: LoginRequestSchema, session: Session) -> AuthResponseSchema:
        user = database_util.get_user(request.username, session)
        auth_util.verify_password(request.password, user.hashed_password)
        access_token = auth_util.create_access_token(user.email)
        return AuthResponseSchema(access_token=access_token, token_type="bearer")
