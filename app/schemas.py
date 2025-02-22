from pydantic import BaseModel, field_validator


class SignupRequestSchema(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        if len(value) > 50:
            raise ValueError("Name cannot be longer than 50 characters")
        return value


class LoginRequestSchema(BaseModel):
    username: str
    password: str


class AuthResponseSchema(BaseModel):
    access_token: str
    token_type: str
