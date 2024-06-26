import random
import sys
from nltk.corpus import words
from termcolor import colored
import nltk
nltk.download('words')

# Main menu starts when app is opened
def print_menu():
    print("Let's play Wordle!")
    print("Six chances to guess a five letter word. Type your first guess and then hit enter!\n")

#Chooses a secret word
def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words).lower()


def eval_attempt(a, s):  # a = attempt s = secret word
    res = [' '] * 5  # result as list of chars
    # '''encoding for list elements:
    # '*' - char. is correctly placed
    # '+' - char. is in secret word but wrong place
    # '_' char. is not in the secret word
    # '''

    s2 = list(s)  # copt of s as list of chars
    a2 = list(a)  # copy of a as list of chars
    # mark '*' chars
    for pos, char in enumerate(a):
        if char == s[pos]:
            res[pos] = '*'
            a2[pos] = '0'  # mark char as 'checked'
            s2.remove(char)  # remove from s2
        # mark '+', '_' in chars
    for pos, char in enumerate(a2):
        if char != '0':  # only check chars that are not already checked
            if char in s2:
                res[pos] = '+'
                a2[pos] = '0'
                s2.remove(char)  # remove from s2
            else:
                res[pos] = '_'
        # print the attempt as colored chars
    for pos, char in enumerate(a):
        if res[pos] == '_':
            print(char, end='')
        elif res[pos] == '+':
            print(colored(char, 'yellow'), end="")
        else:  # '*'
            print(colored(char, 'green'), end="")

# Checks word length
nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print(len(words_five))

print_menu()
PLAY_AGAIN = " "
while PLAY_AGAIN != "q":
    word = random.choice(words_five).lower()  # using NLTK
    # word = read_random_word() using file words.txt for testing
    for attempt in range(1, 7):
        guess = input().lower()
        # input validation
        while len(guess) != 5 or not guess.isalpha():
            print("Incorrect input. Try Again!")
            guess = input().lower()

        sys.stdout.write('\x1b[1A]')
        sys.stdout.write('\x1b[2K]')

        eval_attempt(guess, word)
        print()

        if guess == word:
            print(colored(f"Congrats you got the word in {attempt}", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")
    PLAY_AGAIN = input(
        "Want to play again? If YES type a new word. If NO type q to exit")
