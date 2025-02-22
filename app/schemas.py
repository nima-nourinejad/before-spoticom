from pydantic import BaseModel


class SignupRequestSchema(BaseModel):
    name: str
    email: str
    password: str


class LoginRequestSchema(BaseModel):
    username: str
    password: str


class AuthResponseSchema(BaseModel):
    access_token: str
    token_type: str
