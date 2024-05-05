# T1A3 Python Terminal App - Wordle Clone

- six turns to guess five letter word.

GitHub Repo Link

Trello board:

## Code Styling Guide

***

I chose to follow the Python Code style guide PEP 8 for all of my coding for this project.

PEP 8 dictates using four spaces for indentation rather than tabs, a maximum line length of 79 characters, seperating top-level function and classes with two blank lines while seperating method definitions inside classes with one blank line.

I elected to use autopep8 in VS Code to auto-adjust my code, once I was finished writing a piece of code I would simple right-click on the text, select 'Format Document' and if there was anything I had missed that didn't adhere to the PEP 8 conventions, autopep would adjust it for me.

## To install application

### System requirements:

- MacOS/Windows/Linux
- Python 3.9 or above

### Dependancies:

- Nltk
- Termcolor

### To run application:

- Open terminal
- Make sure run.sh is executable by inputting: chmod +x run.sh
- Run run.sh

***
The run.sh file will check what version of Python the user has, create a virtual environment, install the required packages and then run the application.

***

Once the application has opened, the user types in a five letter English language word to begin the game.