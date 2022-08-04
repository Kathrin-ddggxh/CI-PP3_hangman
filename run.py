import random
import string
from words import words

alphabet = set(string.ascii_uppercase)
used_letters = set() # stores letters already guessed
lives = 10 # equivalent to number of strokes in hangman image 

logo = """
   ___     _                              
  / _ \___| |_    /\  /\_   _ _ __   __ _ 
 / /_\/ _ \ __|  / /_/ / | | | '_ \ / _` |
/ /_\\\  __/ |_  / __  /| |_| | | | | (_| |
\____/\___|\__| \/ /_/  \__,_|_| |_|\__, |
                                    |___/ 
"""

lives_images = {
    0: """
            ___________
            | /        | 
            |/        ( )
            |         \\|/ 
            |          |
            |         / \\
            |
        """,
    1: """
            ___________
            | /        | 
            |/        ( )
            |         \\| 
            |          |
            |         / \\
            |
        """,
    2: """
            ___________
            | /        | 
            |/        ( )
            |          | 
            |          |
            |         / \\
            |
        """,
    3: """
            ___________
            | /        | 
            |/        ( )
            |          |
            |          |
            |         / 
            |
        """,
    4: """
            ___________
            | /        | 
            |/        ( )
            |          |
            |          |
            |
            |
        """,
    5: """
            ___________
            | /        | 
            |/        ( )
            |          
            |          
            |
            |
        """,
    6: """
            ___________
            | /        | 
            |/        
            |          
            | 
            |         
            |
        """,
    7: """
            ___________
            | /        
            |/        
            |          
            |
            |          
            |
        """,
    8: """
            ___________
            |         
            |
            |        
            |          
            |          
            |
        """,
    9: """
            |
            |
            |
            |
            |
            |
        """,
    10: "",
}

class Level:
    """
    Level class
    """
    def __init__(self, level):
        self.level = level 

    def decide_level(self):
        """
        Decides level based on user input
        """

        if self.level == "1":
            print("Easy: Get hung for the lamb!")
            return "Easy"
        elif self.level == "2":
            print("Medium: Get hung for the sheep!")
            return "Medium"
        elif self.level == "3":
            print("Hard: Get hung for the whole herd!")
            return "Hard"


def validate_level(value):
    """
    Checks if user input for level choice equals only 1, 2 or 3
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False

    return True

       
def get_level():
    """
    Gets level value from user and creates word list accordingly
    """
    while True:
        chosen_level = input("Choose your level:\n 1. Easy\n 2. Medium\n 3. Hard\n")
        level = Level(chosen_level).decide_level()

        if validate_level(chosen_level):
            filter_words(words, level)
            break

    word_list = filter_words(words, level)

    return word_list


def filter_words(words, level):
    """
    Filters words by length into seperate lists
    depending on chosen level
    """
    if level == "Easy":
        easy = [word for word in words if len(word) < 5]  
        return easy
    elif level == "Medium":
        Medium = [word for word in words if len(word) < 10]
        return Medium
    elif level == "Hard":
        hard = [word for word in words if len(word) >= 10]
        return hard
      

def get_word(words):
    """
    Returns random word from words list
    in uppercase letters
    """
    word = random.choice(words).upper()

    return word


def validate_letter(letter):
    """
    Validates user input is letter (a-z)
    """
    try:
        if (letter not in alphabet):
            raise ValueError(
                f"Please only guess single letters (a-z). You typed {letter}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}.\n")
        return False

    return True


def get_user_letter():
    """
    Starts the game by asking user for letter input
    """ 
    while True:
        user_letter = input("Guess a letter:\n").upper()

        if validate_letter(user_letter):
            break

    return user_letter


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
    player_letter = get_user_letter() # current guessed letter
    
    # adds guessed letter to used letters set
    if player_letter in alphabet - used_letters:
        used_letters.add(player_letter)
        # removes correctly guessed letter from word
        if player_letter in word_letters:
            word_letters.remove(player_letter)
        else:
            handle_lives()

    # tells user to guess again if letter is already guessed
    elif player_letter in used_letters:
        print("Sorry, you've already guessed this one. Try a different letter!")
    # validate user input is a letter
    else:
        print("This one isn't valid. Please only guess single letters!")


def display_word():
    """
    Shows user correctly guessed letters
    """
    correct_letters = [letter if letter in used_letters else "_" for letter in word]
    print(f"Try to guess this word: {' '.join(correct_letters)}")


def run_intro():
    """
    Displays logo, game introduction and rules
    """
    print(logo)
    print("Welcome! And try not to get hung...\n")
    print("First, choose your skill level. The word you have to guess gets longer the higher your level is.\n")
    print("Then try and guess the mystery word one letter at a time before you're out of lives.\n")
    print("You'll start off with 10 lives. For each wrong guess you lose one and your gallows gets built more until you dangle.\n") 
    print("If you want to play again, simply restart the game by pressing the RUN GAME button at the top.\n")
    print("GOOD LUCK 🤞\n")
    

def run_game():
    """
    Runs a loop to determine when game is finished
    """
    print(word) #remove later

    while len(word_letters) > 0 and lives > 0:
        print(f"You've guessed these letters so far: {' '.join(used_letters)}")

        display_word()

        check_letter()

        print(lives_images[lives])

        if lives == 0:
            print(f"Sorry, you're dangling 😢 The word was {word}")
            break
        elif len(word_letters) == 0:
            display_word()
            print("🎉 Well done! You guessed the whole word 🎉")
            break


def main():
    """
    Runs entire application and shows game intro
    """
    global level, word_list, word, word_letters

    run_intro()
    word_list = get_level()
    word = get_word(word_list)
    word_letters = set(word)
    run_game()
    
main()
