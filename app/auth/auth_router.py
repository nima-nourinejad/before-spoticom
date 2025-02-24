from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.schemas import AuthResponseSchema, SignupRequestSchema
from app.database.database import database
from app.auth.auth_util import auth_util
from app.database.database_util import database_util
from app.auth.auth_router_util import AuthRouterUtil

auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema,
    session: Annotated[Session, Depends(database.get_session)],
) -> AuthResponseSchema:
    return AuthRouterUtil.signup(request, session)


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(database.get_session)],
) -> AuthResponseSchema:
    return AuthRouterUtil.login(form_data.username, form_data.password, session)


@auth_router.get("/user")
async def get_user(
    access_token: Annotated[str, Depends(auth_util.OAUTH2_SCHEME)],
    session: Annotated[Session, Depends(database.get_session)],
) -> dict[str, str]:
    user = database_util.get_user_from_access_token(access_token, session)
    if user:
        return {"name": user.name, "email": user.email}
    return {"message": "User not found"}
