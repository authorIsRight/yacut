
import string
import random

from .models import URLMap


def is_unique_short_id(short_id):

    link = URLMap.query.filter_by(short=short_id).first()
    return link is None


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for i in range(6))
        if is_unique_short_id(short_id):
            return short_id


# def is_unique_short_id(short_id):

#     link = URLMap.query.filter_by(short_id=short_id).first()
#     return link is None