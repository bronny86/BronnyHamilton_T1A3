# T1A3 Python Terminal App - Wordle Clone

[GitHub Repo](https://github.com/bronny86/BronnyHamilton_T1A3)

[Trello board](https://trello.com/b/NHBzKddx/ATTIc94410449bdd3d338583ae5848b0021393D415EF/t1a3-python-terminal-wordle-app)

## Code Styling Guide

***

I chose to follow the Python Code style guide [PEP 8](https://peps.python.org/pep-0008/) for all of my coding for this project.

PEP 8 dictates using four spaces for indentation rather than tabs, a maximum line length of 79 characters, seperating top-level function and classes with two blank lines while seperating method definitions inside classes with one blank line.

I elected to use [autopep8](https://pypi.org/project/autopep8/) in VS Code to auto-adjust my code, once I was finished writing a piece of code I would simple right-click on the text, select 'Format Document' and if there was anything I had missed that didn't adhere to the PEP 8 conventions, autopep would adjust it for me.

***

## Help Documentation

### To install application

### System requirements

- MacOS/Windows/Linux
- Python 3.9 or above

### Dependancies

- [nltk](https://pypi.org/project/nltk/) (Natural Language Toolkit)
- [Termcolor](https://pypi.org/project/termcolor/)

### To run application

- Download zip from from my [Git Repo](https://github.com/bronny86/BronnyHamilton_T1A3)
- Unzip and choose where to place the file
- Open terminal
- Navigate to the /src directory
- Make sure run.sh is executable by inputting: chmod +x run.sh
- Run ./run.sh

***
The run.sh file will check what version of Python the user has, create a virtual environment, install the required packages and then run the application.

***

Once the application has opened, the user types in a five letter English language word to begin the game.

***

## Implementation Plan

Trello board linked above. Screenshot examples:

![Trello board 1](/docs/screenshots/Screenshot%202024-05-05%20at%2010.01.13 PM.png)

![Trello board 2](/docs/screenshots/Screenshot%202024-05-05%20at%2010.01.37 PM.png)

![Trello board 3](/docs/screenshots/Screenshot%202024-05-05%20at%2010.01.59 PM.png)

![Trello board 4](/docs/screenshots/Screenshot%202024-05-05%20at%209.59.41 PM.png)

***

## Flowchart Diagram of App

![Flowchart](/docs/screenshots/flowchart.png)

***

## Features and Logic

The app starts by welcoming the player, briefly explains the rules (six chances to guess a five letter word), and invites the player to begin by typing in a five letter word. The app chooses a random word (using the Python package random) and keeps it a secret from the user.

Once the player types in a guess, the program checks that the word they have input is five letters long and is an English language word recognised by the word list being used, which in this case is the Python library nltk (Natural Language Toolkit). If it is not a recognised word or is not five letters, the app will output 'Incorrect input. Try again!'

If the word the user has typed in as their guess is a recognised five letter word, the program will then search through each letter of the word as a separate character and compare to the secret word to determine which, if any, letters are the correct letter in the correct place, the correct letter but in the wrong position or if the letter is not in the secret word at all. The program will then output the user's guess marking correct letters in the correct place as green, correct letters in the wrong place as yellow and leaving letters that do not appear in the secret word as the default color.

The user then inputs their next guess and so on. The app allows the user six chances to guess and provides the right letter right place/right letter wrong place/wrong letter output for each guess while keeping track of how many turns the user has had.

If the user guesses the correct answer that matches the secret letter, the app will output 'Congrats! You got the word in x many attempts!'

If by the sixth try the user still has not correctly guessed the secret word, then the app will output 'Sorry the wordle was x.'

Then the app outputs 'Want to try again? If YES type a new word. If NO press q to quit.' If the user types in a new word, the whole process begins again. If the user types q, this ends the application and quits back to a terminal.

***

## Referenced Sources

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
- [nltk.org](https://www.nltk.org/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [autopep8](https://pypi.org/project/autopep8/)
- [Termcolor](https://pypi.org/project/termcolor/)
- [CodetoFlow](https://codetoflow.com/)
