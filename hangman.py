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

        print(lives_visual_dict[lives]) # printing the hangman figure corresponding to the current life
        print("Current word:"," ".join(word_list)) # shows the current word with the _ for incomplete letters

    # letters and arrangements
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"{user_letter} is not in the word. You now have {lives} lives left.") if lives != 1 else print(f"{user_letter} is not in the word. You now have {lives} life left.") # The if statement is to maintain correct grammar.

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.") 

        else:
            print("Invalid input. Please try again.") # Incase the user types something other than letters.

    # gets here if the user either wins or loses
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died. The word was", word + ".")
    else:
        print("Congratulations! You guessed the word", word + ".")
        global score
        score += 1 
        print("Your score is:", score)

# executing the program
if __name__ == "__main__":
    score = 0
    while True:
        hangman()
        response = input("Do you wish to play? (y/n) ").lower()
        while response != "y" and response != "n":
            response = input("Invalid input. Do you wish to play? (y/n) ").lower()
        if response == "n":
            print("Your final score is:", score)
            print("Game over")
            break