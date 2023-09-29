# backend/story.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.database import db

Base = declarative_base()

engine = create_engine("sqlite:///database.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()

class Story(Base):
    __tablename__ = "stories"

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String, nullable=False)
    story = db.Column(db.Text, nullable=False)

    def generate_story(self):
        # This function should generate a story based on the prompt
        pass

    def __repr__(self):
        return f"<Story id={self.id} prompt={self.prompt} story={self.story}>"

