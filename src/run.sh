#! /bin/bash

# install venv
python3 -m pip install --user virtualenv
# create virtual environment
python3 -m venv .venv
# activate virtual environment
source venv/bin/activate

# install nltk
pip install nltk

# install termcolor

pip install termcolor

# run game
python3 wordle.py