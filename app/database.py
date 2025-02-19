from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

Base = declarative_base()


class Database:
    USER: str = "postgres"
    PASSWORD: str = "123456"
    DB_NAME: str = "game"
    HOST_PORT: str = "localhost:5432"
    PREFIX: str = "postgresql+psycopg2"

    def __init__(self) -> None:
        self.__engine: Engine = self.__build_engine()
        self.__session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )

    def __build_url(self) -> str:
        return f"{self.PREFIX}://{self.USER}:{self.PASSWORD}@{self.HOST_PORT}/{self.DB_NAME}"

    def __build_engine(self) -> Engine:
        return create_engine(self.__build_url())

    def get_session(self) -> Generator[Session, None, None]:
        session: Session = self.__session_factory()
        try:
            yield session
        finally:
            session.close()
