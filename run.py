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

word = get_word(words)

def render_game():
    """
    Runs the game by asking user for letter input
    """ 
    player_letter = input("Guess a letter:\n").upper()

    return player_letter


print(render_game())


