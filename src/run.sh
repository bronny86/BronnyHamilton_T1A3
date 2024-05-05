#!/bin/bash

# Check python version
python3 --version

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install packages
pip3 install nltk
pip3 install termcolor

# run game
python3 wordle.py