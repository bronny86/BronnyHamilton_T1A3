#!/bin/bash

# Make script executable
chmod +x /check_python.sh
chmod +x /create_venv.sh
chmod +x /install_packages.sh

# Run python check/install script
./check_python.sh

# Create vevn
./create_venv.sh

# Install packages
./install_package.sh

# run game
python3 wordle.py