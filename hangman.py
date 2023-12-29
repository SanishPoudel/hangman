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


def hangman():
    """This is the main function that executes the hangman program."""
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # printing the setup
    lives = 7

    while len(word_letters) > 0 and lives > 0: # while the user has neither won nor lost

        print(f"Lives: {lives}. You have used these letters"," ".join(used_letters)) # showing the lives and used letters

        # displaying the letter in W _ R D format.
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("_")

        print(lives_visual_dict[lives]) # printing the hangman figure corresponding to the current lives
        print("Current word:"," ".join(word_list)) # shows the current word with the _ for incomplete letters

hangman()