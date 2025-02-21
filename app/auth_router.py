from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import AuthResponseSchema, LoginRequestSchema, SignupRequestSchema
from app.database import database
from app.models import User


auth_router = APIRouter(prefix="/authentication", tags=["authentication"])


@auth_router.post("/signup", response_model=AuthResponseSchema)
async def signup(
    request: SignupRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    db_user = User(
        username=request.username,
        email=request.email,
        hashed_password=request.password,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return AuthResponseSchema(
        access_token="",
        token_type="bearer"
    )


@auth_router.post("/login", response_model=AuthResponseSchema)
async def login(
    request: LoginRequestSchema, session: Session = Depends(database.get_session)
) -> AuthResponseSchema:
    pass
