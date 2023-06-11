import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    User_from_id = Column(Integer, primary_key=True)
    User_to_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    iD = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(250), nullable=False)
    Lastname = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    iD = Column(Integer, primary_key=True)
    Comment_text = Column(String(250), nullable=False)
    Author_ID = Column(Integer, nullable=False)
    Post_ID = Column(Integer, nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    User_id = Column(Integer, nullable=False)  

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    Type = Column(enumerate, primary_key=True)
    URL = Column(String(250), nullable=False)        
    Post_ID = Column(Integer, nullable=False) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
