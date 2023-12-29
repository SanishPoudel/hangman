from words import words
from hangman_visual import lives_visual_dict
import string
import random

def get_valid_words(words):
    """Function to get valid words without spaces or hyphes from the list of random words."""
    valid_words = random.choice(words)
    while " " in valid_words or "-" in valid_words:
        valid_words = random.choice(words)
    return valid_words.upper()
