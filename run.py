import random
import string
from words import words

def get_word(words):
    """
    Returns random word from words list
    in uppercase letters
    """
    word = random.choice(words).upper()

    return word


def render_game():
    """
    Runs the game by asking user for letter input
    """ 
    player_letter = input("Guess a letter:\n").upper()

    return player_letter


def check_letter():
    """
    Checks if guessed letter has already been guessed 
    and if letter is in word
    """
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # stores letters already guessed
    player_letter = render_game() # current guessed letter

    # adds guessed letter to used letters set
    if player_letter in alphabet - used_letters:
        used_letters.add(player_letter)
        # removes correctly guessed letter from word
        if player_letter in word_letters:
            word_letters.remove(player_letter)
    # tells user to guess again if letter is already guessed
    elif player_letter in used_letters:
        print("Sorry, you've already guessed this one. Try a different letter!")
    # validate user input is a letter
    else:
        print("This one isn't valid. Please only guess letters!")



