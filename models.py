# models.py
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    stats = relationship('Stat', back_populates='user', uselist=False)
    games = relationship('Game', back_populates='user')


class Stat(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    games_played = Column(Integer, default=0)
    average_score = Column(Float, default=0.0)
    best_score = Column(Float, default=0.0)
    highest_score = Column(Float, default=0.0)
    lowest_score = Column(Float, default=10.0)
    user = relationship('User', back_populates='stats')


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    score = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now)
    user = relationship('User', back_populates='games')


engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)
