from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

USER = "postgres"
PASSWORD = "123456"
DB_NAME = "game"
HOST_PORT = "localhost:5432"
PREFIX = "postgresql+psycopg"
URL_DATABASE = f"{PREFIX}://{USER}:{PASSWORD}@{HOST_PORT}/{DB_NAME}"
engine = create_engine(URL_DATABASE)


Base = declarative_base()
