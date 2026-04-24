from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mssql+pyodbc://(localdb)\\MSSQLLocalDB/HelloGLH?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String)
    password_hash = Column(String, nullable=False)


class Producer(Base):
    __tablename__ = "Producers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    profession = Column(String)
    story = Column(String)


class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)
    description = Column(String)