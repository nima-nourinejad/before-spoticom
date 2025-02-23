from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy, PasswordStats
from pydantic import EmailStr


class SchemaValidator:
    @staticmethod
    def validate_name(value: str) -> str:
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        return value

    @staticmethod
    def validate_email(value: EmailStr) -> EmailStr:
        try:
            validate_email(value, check_deliverability=True)
        except EmailNotValidError as error:
            raise ValueError(str(error)) from error
        return value

    @staticmethod
    def validate_password(value: str) -> str:
        policy = PasswordPolicy.from_names(
            length=8,
            uppercase=1,
            numbers=1,
            special=1,
        )
        if policy.test(value):
            raise ValueError("Password does not meet the requirements")
        if PasswordStats(value).strength() < 0.5:
            raise ValueError("Password is too weak")
        if not any(char.islower() for char in value):
            raise ValueError("Password does not meet the requirements")
        return value
