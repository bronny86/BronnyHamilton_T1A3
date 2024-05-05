#! /bin/bash

# check if python is installed
python3 --version

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

# make script executable
chmod +x ./run.sh

# run game
./run.sh
python3 wordle.py