from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AuthResponseSchema, LoginRequestSchema, SignupRequestSchema
from app.database import database


auth_router = APIRouter(prefix="/authentication", tags=["authentication"])


@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    pass


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    request: LoginRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    pass
