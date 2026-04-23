from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mssql+pyodbc://(localdb)\\MSSQLLocalDB/HelloGLH?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


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