# game_logic.py
import logging
import random

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from auth import hash_password  # Import the hash_password function
from models import Stat, User, Game, engine

# Setup logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

Session = sessionmaker(bind=engine)
session = Session()


def play_game(user_id):
    try:
        rolled_numbers = [round(random.uniform(0.0, 10.0), 1) for _ in range(10)]
        average_score = round(sum(rolled_numbers) / 10, 1)
        user_stat = session.query(Stat).filter_by(user_id=user_id).first()
        if not user_stat:
            raise AttributeError("User stats not found")
        user_stat.games_played += 1
        user_stat.average_score = average_score
        user_stat.best_score = max(user_stat.best_score, average_score)
        user_stat.highest_score = max(rolled_numbers)
        user_stat.lowest_score = min(rolled_numbers)
        session.commit()

        # Record the game in the game history
        new_game = Game(user_id=user_id, score=average_score)
        session.add(new_game)
        session.commit()

        # Calculate the global ranking
        all_stats = session.query(Stat).order_by(Stat.average_score.desc()).all()
        for index, stat in enumerate(all_stats, start=1):
            if stat.user_id == user_id:
                global_ranking = index
                break

        return rolled_numbers, average_score, global_ranking
    except Exception as e:
        logging.error(f"Unexpected error in play_game: {e}")
        raise


def generate_data(record_count):
    try:
        for _ in range(record_count):
            while True:
                num = str(random.randint(0, 99999))
                username = f'user_{num}'
                password = hash_password(num)  # Hash the password
                new_user = User(username=username, password=password)
                session.add(new_user)
                try:
                    session.commit()
                    break
                except IntegrityError:
                    session.rollback()
                    continue

            games_played = random.randint(1, 50)
            average_score = round(random.uniform(0.0, 10.0), 1)
            best_score = round(random.uniform(0.0, 10.0), 1)
            highest_score = round(random.uniform(0.0, 10.0), 1)
            lowest_score = round(random.uniform(0.0, 10.0), 1)

            new_stat = Stat(
                user_id=new_user.id,
                games_played=games_played,
                average_score=average_score,
                best_score=best_score,
                highest_score=highest_score,
                lowest_score=lowest_score
            )
            session.add(new_stat)
            session.commit()

            for _ in range(games_played):
                game_score = round(random.uniform(0.0, 10.0), 1)
                new_game = Game(user_id=new_user.id, score=game_score)
                session.add(new_game)

            session.commit()
    except Exception as e:
        logging.error(f"Error generating data: {e}")
        raise
