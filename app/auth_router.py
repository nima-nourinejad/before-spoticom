from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AuthResponseSchema, LoginRequestSchema, SignupRequestSchema
from app.database import database
from app.auth_util import auth_util
from app.database_util import database_util


auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:

    database_util.add_user(request, session)
    access_token = auth_util.create_access_token(request.email)

    return AuthResponseSchema(access_token=access_token, token_type="bearer")


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    request: LoginRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:

    user = database_util.get_user(request.username, session)
    auth_util.verify_password(request.password, user.hashed_password)
    access_token = auth_util.create_access_token(user.email)

    return AuthResponseSchema(access_token=access_token, token_type="bearer")
