# Get Hung ...

... for the lamb, the sheep or the whole herd.
In this terminal based game of classic Hangman, the player tries to guess a word letter by letter before running out of lives and being sent to the gallows.

This project was built with Python3 as the "Python's Essentials" Project (portfolio project 3) for Code Insitute. 

[Link to live site](https://get-hung.herokuapp.com/)

![Responsive mock-up](assets/images/mockup.JPG)


## Planning

The following flowchart (created with [daigrams.net](https://app.diagrams.net/)) visualizes the planning process for this application.

![Flowchart](assets/images/GetHungFlow1.1.png)


## Fixed Bugs

**Word not displaying fully when game won**:

After entering the last letter of the fully guessed word, the last letter is not added to the word display. Therefore the finished word doesn't display properly.

*Solution*:

Run display_word function again when condition for game completion is met:
```
elif len(word_letters) == 0:
    display_word()
    print("🎉 Well done! You guessed the whole word 🎉")
```

## Credits

### Data

- **Word List**: 

    [This list](https://www.randomlists.com/data/words.json) was used as supplied by [this StackOverflow post](https://stackoverflow.com/questions/594273/how-to-pick-a-random-english-word-from-a-list)

    Using MS Word I manually removed all words containing "-" to simplify the game functionality. Also, I adapted the spelling to UK English where it originally differed. 

- **Logo**:

    [Text to ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

    Font: Ogre.


### Code

- **Hangman Game**

    [Tutorial by Kylie Ying](https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s)

    Code was adapted to meet granular function criteria

- **Hangman ascii visualisation**

    Taken from [tutorial repo](https://github.com/kying18/hangman/blob/master/hangman_visual.py)


### Styling

- **Colours**

    Built-in module [Colorama](https://github.com/techwithtim/ColoredTextInPython/blob/main/main.py)

- **Timing**

    [time module](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=Make%20your%20time%20delay%20specific,after%20a%20slight%20delay.%22) and sleep() function