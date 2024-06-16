# initialize_db.py
from auth import register
from models import Base, engine


def initialize_db():
    Base.metadata.create_all(engine)
    try:
        register("ad", "ad", True)
        print("Admin account created successfully.")
    except ValueError as e:
        print(f"Admin account creation error: {e}")


if __name__ == "__main__":
    initialize_db()
