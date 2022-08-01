import random
import string
from words import words

alphabet = set(string.ascii_uppercase)
used_letters = set() # stores letters already guessed
lives = 7 # equivalent to number of strokes in hangman image 

lives_images = {
    0: """
            ___________
            | /        | 
            |/        ( )
            |          |
            |         / \\
            |
        """,
    1: """
            ___________
            | /        | 
            |/        ( )
            |          |
            |         / 
            |
        """,
    2: """
            ___________
            | /        | 
            |/        ( )
            |          |
            |          
            |
        """,
    3: """
            ___________
            | /        | 
            |/        ( )
            |          
            |          
            |
        """,
    4: """
            ___________
            | /        | 
            |/        
            |          
            |          
            |
        """,
    5: """
            ___________
            | /        
            |/        
            |          
            |          
            |
        """,
    6: """
            |
            |
            |
            |
            |
        """,
    7: "",
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
            return "Easy"
        elif self.level == "2":
            return "Medium"
        elif self.level == "3":
            return "Hard"
       

chosen_level = input("Choose your level:\n 1. Easy\n 2. Medium\n 3. Hard\n")
level = Level(chosen_level).decide_level()


def filter_words(words, level):
    """
    Filters words by length into seperate lists
    depending on chosen level
    """
    if level == "Easy":
        easy = [word for word in words if len(word) <= 5]
        print(f"{level}: Get hung for the lamb!")
        return easy
    elif level == "Medium":
        Medium = [word for word in words if len(word) < 10]
        print(f"{level}: Get hung for the sheep!")
        return Medium
    elif level == "Hard":
        hard = [word for word in words if len(word) >= 10]
        return hard
    else:
        print("Please only enter 1, 2 or 3")
      
word_list = filter_words(words, level)


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

        print(lives_images[lives])

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
    

main()



