
import random
import string

from .models import URLMap


def is_unique_short_id(short_id):
    """Check if short link is in the database"""
    link = URLMap.query.filter_by(short=short_id).first()
    return link is None


def get_unique_short_id():
    """Creates a unique short link and returns it to views"""
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for i in range(6))
        if is_unique_short_id(short_id):
            return short_id
