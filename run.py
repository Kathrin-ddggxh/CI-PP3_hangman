import random
import string
from words import words

alphabet = set(string.ascii_uppercase)
used_letters = set() # stores letters already guessed
lives = 6 # equivalent to number of strokes in hangman image 


def get_word(words):
    """
    Returns random word from words list
    in uppercase letters
    """
    word = random.choice(words).upper()

    return word

word = get_word(words)
word_letters = set(word)

def get_user_input():
    """
    Runs the game by asking user for letter input
    """ 
    player_letter = input("Guess a letter:\n").upper()

    return player_letter

def handle_lives():
    """
    Decrements lives for each wrong guess
    """
    global lives
    lives = lives - 1 
    print(f"Wrong letter! You have {lives} lives left.")
    

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
        else:
            handle_lives()

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
    print(word) #remove later
    while len(word_letters) > 0 and lives > 0:
        print(f"You've guessed these letters so far: {' '.join(used_letters)}")

        display_word()

        check_letter()

        if lives == 0:
            print(f"Sorry, you're dangling 😢 The word was {word}")
            break
        elif len(word_letters) == 0:
            print("🎉 Well done! You guessed the whole word 🎉")
            break





def main():
    """
    Runs entire application
    """
    run_game()
    #check_letter()


main()



