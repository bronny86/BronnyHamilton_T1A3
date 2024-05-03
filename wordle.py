import random
import sys
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words

def print_menu():
    print("Let's play Wordle!")
    print("Six chances to guess a five letter word. Type your first guess and then hit enter!\n")

def read_random_word():
    with open ("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words).lower()
    
def eval_attempt(a, s): #a = attempt s = secret word
    res = [' '] * 5 #result as list of chars
    '''encoding for list elements:
    '*' - char. is correctly placed
    '+' - char. is in secret word but wrong place
    '_' char. is not in the secret word
    '''

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print(len(words_five))
print_menu()
play_again = " "
while play_again != "q":
    word = random.choice(words_five).lower()
    for attempt in range(1, 7):
        guess = input().lower()