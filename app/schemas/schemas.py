from pydantic import BaseModel, field_validator, Field, EmailStr
from app.schemas.schema_validator import SchemaValidator


class SignupRequestSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str)->str:
        return SchemaValidator.validate_name(value)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr)->EmailStr:
        return SchemaValidator.validate_email(value)

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str)->str:
        return SchemaValidator.validate_password(value)


class LoginRequestSchema(BaseModel):
    username: EmailStr
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: EmailStr) -> EmailStr:
        return SchemaValidator.validate_email(value)

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        return SchemaValidator.validate_password(value)


class AuthResponseSchema(BaseModel):
    access_token: str
    token_type: str
