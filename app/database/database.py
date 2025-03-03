import os
from typing import Generator
from fastapi import HTTPException
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self) -> None:
        self.__engine: Engine = self.__build_engine()
        self.__session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )

    def __build_engine(self) -> Engine:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise HTTPException(status_code=500, detail="Internal server error")
        return create_engine(db_url)

    def get_session(self) -> Generator[Session, None, None]:
        session: Session = self.__session_factory()
        try:
            yield session
        finally:
            session.close()


database = Database()
