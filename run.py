import random  # generates random numbers
import string  # module for string manipulation
from words import words  # imports word list from word.py
import colorama
from colorama import Fore, Back, Style  # enables different coloured text
from time import sleep  # allows time delay for print statements

colorama.init(autoreset=True)

alphabet = set(string.ascii_uppercase)  # stores letters A-Z
used_letters = set()  # stores letters already guessed
lives = 10  # equivalent to number of strokes in hangman image

logo = """   ___     _
  / _ \\___| |_    /\\  /\\_   _ _ __   __ _
 / /_\\/ _ \\ __|  / /_/ / | | | '_ \\ / _` |
/ /_\\\\  __/ |_  / __  /| |_| | | | | (_| |
\\____/\\___|\\__| \\/ /_/  \\__,_|_| |_|\\__, |
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
            print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Easy:{Style.RESET_ALL} Get hung for the lamb!\n"
            )
            return "Easy"
        elif self.level == "2":
            print(
                f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Medium:{Style.RESET_ALL} Get hung for the sheep!\n"
            )
            return "Medium"
        elif self.level == "3":
            print(
                f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Hard:{Style.RESET_ALL} Get hung for the whole herd!\n"
            )
            return "Hard"


def validate_level(value):
    """
    Checks if user input for level choice equals only 1, 2 or 3
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed {Style.BRIGHT}{value}{Style.RESET_ALL}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data:{Fore.RESET} {e}, please try again\n")
        return False
    return True


def get_level():
    """
    Gets level value from user and creates word list accordingly
    """
    while True:
        chosen_level = input(
            "Choose your level:\n\n 1. Easy\n 2. Medium\n 3. Hard\n")
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
        if letter not in alphabet:
            raise ValueError(
                f"Please only guess single letters (a-z). You typed {Style.BRIGHT}{letter}{Style.RESET_ALL}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data:{Fore.RESET} {e}.\n")
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
    print(f"Wrong letter! You have {Style.BRIGHT}{lives} lives left.\n")


def check_letter():
    """
    Checks if guessed letter has already been guessed
    and if letter is in word
    """
    player_letter = get_user_letter()  # current guessed letter

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
        print("Sorry, you've already guessed this one. Try a different letter!\n")
    # validate user input is a letter
    else:
        print("This one isn't valid. Please only guess single letters!\n")


def display_word():
    """
    Shows user correctly guessed letters
    """
    correct_letters = [
        letter if letter in used_letters else "_" for letter in word]
    print(
        f"Try to guess this word: {Fore.LIGHTGREEN_EX}{' '.join(correct_letters)}\n")


def run_intro():
    """
    Displays logo, game introduction and rules
    """
    print(f"{Style.BRIGHT}{Fore.GREEN}{logo}")
    print("Welcome! And try not to get hung...\n")
    sleep(1)
    print(
        "First, choose your skill level. The word you have to guess gets longer the higher your level is.\n"
    )
    sleep(0.5)
    print(
        "Then try and guess the mystery word one letter at a time before you're out of lives.\n"
    )
    sleep(0.5)
    print(
        f"You'll start off with {Style.BRIGHT}10 {Style.RESET_ALL}lives. For each wrong guess you lose one and your gallows gets built more until you dangle.\n"
    )
    sleep(0.5)
    print(
        f"If you want to play again, simply restart the game by pressing the {Style.BRIGHT}{Fore.GREEN}RUN GAME {Style.RESET_ALL}button at the top.\n"
    )
    sleep(0.5)
    print(f"{Fore.LIGHTYELLOW_EX}GOOD LUCK 🤞\n")


def run_game():
    """
    Runs a loop to determine when game is finished
    """

    while len(word_letters) > 0 and lives > 0:
        print(
            f"You've guessed these letters so far: {Style.BRIGHT}{Fore.RED}{' '.join(used_letters)}\n"
        )

        display_word()

        check_letter()

        print(f"{Style.BRIGHT}{Fore.RED}{lives_images[lives]}")

        if lives == 0:
            print(
                f"Sorry, you're dangling 😢 The word was {Style.BRIGHT}{word.upper()}")
            break
        elif len(word_letters) == 0:
            display_word()
            print("🎉 WELL DONE! You guessed the whole word 🎉")
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