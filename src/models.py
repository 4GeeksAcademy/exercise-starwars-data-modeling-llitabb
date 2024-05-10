import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
     id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Comments(Base):
    __tablename__ = 'comment'
   id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Posts)
    comment_text = Column(String(250), nullable=False)
 
class Followers(Base):
    __tablename__ = 'follower'
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    user_id_follower = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

    def to_dict(self):
        return {}
    
render_er(Base, 'diagram.png')
