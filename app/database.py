from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()


class Database:
    USER = "postgres"
    PASSWORD = "123456"
    DB_NAME = "game"
    HOST_PORT = "localhost:5432"
    PREFIX = "postgresql+psycopg2"

    def __init__(self):
        self.__engine = self.__build_engine()
        self.__session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )

    def __build_url(self):
        return f"{self.PREFIX}://{self.USER}:{self.PASSWORD}@{self.HOST_PORT}/{self.DB_NAME}"

    def __build_engine(self):
        return create_engine(self.__build_url())

    def get_session(self):
        session: Session = self.__session_factory()
        try:
            yield session
        finally:
            session.close()
