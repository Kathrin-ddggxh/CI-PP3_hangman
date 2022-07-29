import random
from words import words

def get_word(words):
    """
    Returns random word from words list
    in uppercase letters
    """
    word = random.choice(words).upper()

    return word

word = get_word(words)
print(word)


