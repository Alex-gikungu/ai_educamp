from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///database.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()
