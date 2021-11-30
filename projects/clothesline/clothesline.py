#!/bin/env python3
import os
import random

MAX_INCORRECT = 8
WORD_FILE = "easy_words.txt"


def main():
    word = pick_word()
    guess = "-" * len(word)
    incorrect_count = 0

    while incorrect_count < MAX_INCORRECT and word != guess:
        print_screen(incorrect_count, guess)

        letter = get_letter()

        if is_letter_in_word(letter, word):
            guess = update_guess(guess, letter, word)
        else:
            incorrect_count += 1

    print_screen(incorrect_count, guess)
    print(f"The word was {word}\n")

    if word == guess:
        print("You Win!")
    else:
        print("You Lose!")


def print_screen(incorrect_count, guess):
    clear_screen()
    print_clothesline(incorrect_count)
    print(f"\n{guess}\n")


def clear_screen():
    print("\033[H\033[J", end="")


def pick_word():
    with open(WORD_FILE) as word_file:
        words = word_file.readlines()

    word = random.choice(words)
    word = word.strip()

    return word


def get_letter():
    print("Guess a letter...if you dare!")
    user_input = input("> ")
    return user_input[0]


def is_letter_in_word(letter, word):
    return letter in word


def update_guess(old_guess, letter,  word):
    new_guess = ""
    for i in range(len(old_guess)):
        if word[i] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[i]

    return new_guess


def print_clothesline(incorrect_count):
    if MAX_INCORRECT - incorrect_count == 8:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````
"""
    elif MAX_INCORRECT - incorrect_count == 7:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!======
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|
"""

    elif MAX_INCORRECT - incorrect_count == 6:
        clothesline = r"""
=====!=====!=======!=====!=======!=====!==============
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
"""
    elif MAX_INCORRECT - incorrect_count == 5:
        clothesline = r"""
=====!=====!=======!=====!=======!====================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
"""
    elif MAX_INCORRECT - incorrect_count == 4:
        clothesline = r"""
=====!=====!=======!=====!============================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
"""
    elif MAX_INCORRECT - incorrect_count == 3:
        clothesline = r"""
=====!=====!=======!==================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
"""
    elif MAX_INCORRECT - incorrect_count == 2:
        clothesline = r"""
=====!=====!==========================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
"""
    elif MAX_INCORRECT - incorrect_count == 1:
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
