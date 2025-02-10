"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.INFO)


fake = Faker(locale="fr_FR")

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"



def get_users(n):
    """Generate a list of users

    Args:
        n (int): Number of users to generate

    Returns:
        list[str]: users
    """
    logging.info(f"Generatinf a list of {n} users.")
    return [get_user() for _ in range(n)]   
    
if __name__ == "__main__":
    user = get_user()
    print(f"Utilisateur: {user}")
    users = get_users(3)
    print(f"Utilisateurs: {users}")  

    