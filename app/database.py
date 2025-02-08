from sqlalchemy import create_engine

USER = "postgres"
PASSWORD = "123456"
DB_NAME = "game"
HOST_PORT = "localhost:5432"
PREFIX = "postgresql+psycopg"
URL_DATABASE = f"{PREFIX}://{USER}:{PASSWORD}@{HOST_PORT}/{DB_NAME}"
engine = create_engine(URL_DATABASE)


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.create_all(bind=engine)
