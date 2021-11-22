#!/bin/env python3
import os
import random

MAX_INCORRECT = 8

def main():
    word = pick_word()
    guess = "_" * len(word)
    incorect_count = 0

    while incorect_count < MAX_INCORRECT and word != guess:
        print_screen(incorect_count, guess)

        letter = get_letter()

        if is_guess_correct(letter, word):
            guess = update_guess(guess, letter, word)
        else:
            incorect_count += 1

    print_screen(incorect_count, guess)
    print(f"The word was {word}\n")

    if word == guess:
        print("You Win!")
    else:
        print("You Lose!")


def print_screen(incorect_count, guess):
    clear_screen()
    print_clothesline(incorect_count)
    print(f"\n{guess}\n")


def clear_screen():
    #os.system("clear")
    print("\033[H\033[J", end="")


def pick_word():
    words = [
        "apple",
        "banana",
        "pear",
        "orange",
        "lemon",
        "monkey",
        "deer",
        "buffalo",
        "eagle",
        "ant",
    ]
    return random.choice(words)


def get_letter():
    user_input = input("> ")
    return user_input[0]


def is_guess_correct(letter, word):
    return letter in word


def update_guess(guess, letter,  word):
    new_guess = ""
    for i in range(len(guess)):
        if word[i] == letter:
            new_guess += letter
        else:
            new_guess += guess[i]

    return new_guess


def print_clothesline(incorect_count):
    if MAX_INCORRECT - incorect_count == 8:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````
"""
    elif MAX_INCORRECT - incorect_count == 7:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!======
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|
"""

    elif MAX_INCORRECT - incorect_count == 6:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!==============
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
"""
    elif MAX_INCORRECT - incorect_count == 5:
        clothesline = r"""
=====!=====!=======!=====!=======!====================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
"""
    elif MAX_INCORRECT - incorect_count == 4:
        clothesline = r"""
=====!=====!=======!=====!============================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
"""
    elif MAX_INCORRECT - incorect_count == 3:
        clothesline = r"""
=====!=====!=======!==================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
"""
    elif MAX_INCORRECT - incorect_count == 2:
        clothesline = r"""
=====!=====!==========================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
"""
    elif MAX_INCORRECT - incorect_count == 1:
        clothesline = r"""
=====!================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
"""
    else:
        clothesline = r"""
======================================================






"""

    print(clothesline)


main()
