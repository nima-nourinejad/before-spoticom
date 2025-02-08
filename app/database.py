from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    USER = "postgres"
    PASSWORD = "123456"
    DB_NAME = "game"
    HOST_PORT = "localhost:5432"
    PREFIX = "postgresql+psycopg"

    def __init__(self):
        self.base = self.__build_base()
        self.__engine = self.__build_engine()

    def __build_url(self):
        return f"{self.PREFIX}://{self.USER}:{self.PASSWORD}@{self.HOST_PORT}/{self.DB_NAME}"

    def __build_engine(self):
        url = self.__build_url()
        return create_engine(url)

    def __build_base(self):
        return declarative_base()

    def __build_tables(self):
        self.base.metadata.create_all(bind=self.__engine)

    def build_session(self):
        self.__build_tables()
        session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        return session


database = Database()
