import re


def is_strong_password(password):
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special_character = re.search(r'[!@#$%^&*()_+[\]{};:/<>,.?~\\-]', password)
    if (
            len(password) >= min_length and
            has_uppercase and
            has_lowercase and
            has_digit and
            has_special_character
    ):
        return True
    else:
        return False
