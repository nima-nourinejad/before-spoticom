from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base

# class Questions(Base):
#     __tablename__ = "questions"
    
#     id: Column[int] = Column(Integer, primary_key=True, index=True)
#     question_text: Column[str] = Column(String, index=True)






# class Choices(Base):
#     __tablename__ = "choices"
    
#     id: Column[int] = Column(Integer, primary_key=True, index=True)
#     choice_text: Column[str] = Column(String, index=True)
#     is_correct: Column[bool] = Column(Boolean, default=False)
#     question_id: Column[int] = Column(Integer, ForeignKey("questions.id"))





class User(Base):
	__tablename__ = "user"
	
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=oa#hash-and-verify-the-passwords


# Router for signing up and logging in

# {main_uri}/authentication/signup

# Get a payload of name, email, and password and return JWT Token

# Validation for email is required to check if the email is in correct format

# The max length for the name should be 50 char

# Password should have more than 8 chars containing numbers and chars and special chars

# {main_uri}/authentication/login

# Get username and password -> Return JWT Token