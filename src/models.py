import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False) 
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    follower = relationship ('follower', backref='user', lazy=True)
    Comment = relationship ('fomment', backref='user', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    Author_ID = Column(Integer, ForeignKey("user.id"), nullable=False)
    Post_ID = Column(Integer, ForeignKey("post.id"), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    Comment = relationship ('comment', backref='post', lazy=True) 
    Media = relationship ('media', backref='post', lazy=True) 

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    Type = Column(enumerate, primary_key=True)
    URL = Column(String(250), nullable=False)        
    Post_ID = Column(Integer, ForeignKey("post.id"), nullable=False)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
