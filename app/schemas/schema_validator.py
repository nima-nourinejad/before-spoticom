from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy


class SchemaValidator:
    @staticmethod
    def validate_name(value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        return value

    @staticmethod
    def validate_email(value):
        try:
            validate_email(value, check_deliverability=True)
        except EmailNotValidError as error:
            raise ValueError(str(error)) from error
        return value

    @staticmethod
    def validate_password(value):
        policy = PasswordPolicy.from_names(
            length=8,
            uppercase=1,
            numbers=1,
            special=1,
        )
        if policy.test(value):
            raise ValueError("Password is not strong enough")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter")
        return value
