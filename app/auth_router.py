from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AuthResponseSchema, LoginRequestSchema, SignupRequestSchema
from app.database import database
from app.auth_router_util import AuthRouterUtil


auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    return AuthRouterUtil.signup(request, session)


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    request: LoginRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    return AuthRouterUtil.login(request, session)
