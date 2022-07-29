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


def get_user_input():
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
    player_letter = get_user_input() # current guessed letter

    # adds guessed letter to used letters set
    if player_letter in alphabet - used_letters:
        used_letters.add(player_letter)
        print("not yet guessed")
        # removes correctly guessed letter from word
        if player_letter in word_letters:
            word_letters.remove(player_letter)
            print("correct letter")
    # tells user to guess again if letter is already guessed
    elif player_letter in used_letters:
        print("Sorry, you've already guessed this one. Try a different letter!")
    # validate user input is a letter
    else:
        print("This one isn't valid. Please only guess letters!")


def display_word():
    """
    Shows user correctly guessed letters
    """
    correct_letters = [letter if letter in used_letters else "_" for letter in word]
    print(f"Try to guess this word: {' '.join(correct_letters)}")
    

def run_game():
    """
    Runs a loop to determine when game is finished
    """
    while len(word_letters) > 0:
        print(f"You've already used these letter: {' '.join(used_letters)}")

        display_word()

        check_letter()

        if len(word_letters) == 0:
            break


word = get_word(words)
word_letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set() # stores letters already guessed


def main():
    """
    Runs entire application
    """
    run_game()
    #check_letter()


main()



