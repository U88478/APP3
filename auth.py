# auth.py
import hashlib

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from models import User, Stat, engine

Session = sessionmaker(bind=engine)
session = Session()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password, is_admin=False):
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    try:
        hashed_password = hash_password(password)
        new_user = User(username=username, password=hashed_password, is_admin=is_admin)
        session.add(new_user)
        session.commit()
        new_stat = Stat(user_id=new_user.id, lowest_score=10.0)
        session.add(new_stat)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("Username already exists")


def login(username, password):
    hashed_password = hash_password(password)
    user = session.query(User).filter_by(username=username, password=hashed_password).first()
    return user
