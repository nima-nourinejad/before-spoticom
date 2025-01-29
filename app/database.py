from sqlAlchemy import create_engine
from sqlAlchemy.orm import sessionmaker
from sqlAlchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"