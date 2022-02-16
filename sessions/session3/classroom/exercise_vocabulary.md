# Exercise - Vocabulary Words

## Overview

In this exercise you'll build a terminal-based program for studying vocabulary words.

When the program is complete it will do the following:

1. Ask the user to enter a list of words and definitions
1. Prompt the user with each word and ask them to type in the definition
1. Show the actual definition after the user presses `Enter`
1. Offer the user a chance to repeat the words
1. When the user decides to stop, the list of words and definitions will be displayed before the program ends

## The Exercise

This exercise will be broken into several phases. You should complete each phase in order. It may be tempting to work on more than one phase at a time. **Resist this temptation.** Part of being a software engineer is being deliberate and methodical, and sometimes that means moving slowly. **Once a phase is complete do NOT move to the next until you run the program to test it.**

> **NOTE:** Remember, you may need to run the program multiple times in order to fully test a single phase.

As you go through this exercise, you'll sometimes be asked to add code in one phase that is then removed in a later phase. This is a standard part of the software development process and isn't just us messing with you.

## Phase One

1. Prompt the user for four word/definition pairs. First have the user enter a word, and when they press `Enter`, prompt them to enter a definition.

    * You should save each word in it's own variable called `word_X` where `X` is a number starting with `0`. For example, the first word should be saved in a variable called `word_0` and the second should be saved in a variable called `word_1`.

    * Similarly, definitions should be saved in variables called `definition_X`. The definition for `word_0` should be saved in `definition_0`.

1. After the user enters four words, display all the words and definitions. Separate each word/definition pair with a blank line.

    > **NOTE:** In order to display a blank line, use `print()` without putting anything between the parentheses. For example this Python code
    > ```python
    > print("Hello")
    > print()
    > print("World")
    > ```
    > will print
    > ```text
    > Hello
    >
    > World
    > ```

1. Make sure to run your program a few times to test it. Remember, for testing purposes, you don't need to take the time to type out full definitions. A word or two will do.

## Phase Two

1. Comment out the code at the bottom of your program that prints the words and definitions. You'll come back to this later, but for now it's just distracting.

   > **NOTE:** To comment out multiple lines at a time in VS Code you can select the lines you'd like to comment out, then click the Edit menu, then click "Toggle Line Comment". This works to remove the comments as well.

1. Add code to clear the screen after the user has entered all their words and definitions. You should copy and paste this code from the [Bouncing Ball](../../session2/classroom/exercise_ball.md) exercise.

1. Prompt the user to enter the definition for each word, one at a time. For example, if the word is "picnic", the user should be prompted like this:

    ```txt
    Define 'picnic': 
    ```

    For now, do not save the text that the user types in.

1. After the user types in a definition and presses `Enter`, display the correct definition.

1. Display a few blank lines after the correct definition and prompt the user to define the next word.

1. The program should end after the user has seen the correct definition for the fourth word.

## Phase Three

In this phase you'll give the user the option to go through the words and definitions again.

You'll be updating the code after you ask the user to enter the words and definitions. _We do not need to ask the user to re-enter the words and definitions._

1. Create a variable called `keep_going` and set it to the string `"yes"`.

1. Create a `while` loop that will loop as long as the `keep_going` variable is equal to `"yes"`.

1. Move all the code that prompts the user with words into the loop. This is the code you wrote in Phase Two.

1. At the end of the loop, ask the user if they'd like to continue. Save their answer into the `keep_going` variable. If the user types `yes`, that should trigger the `while` loop to run again, but if they type anything else the loop should not run again.

## Phase Four

You may have noticed that your program allows users to enter blank words and definitions. In this phase you'll handle the situation in which a word or definition is blank.

> **NOTE:** The following changes should be within the `while` loop. You should **not** change the code that inputs the values for the `word_X` and `definition_X` variables.

1. Within the `while` loop, before prompting the user to define each word, use an `if` statement to ensure the string in the `word_X` variable is **not** blank. You should only prompt the user to define the word if it is **not** blank.

1. If the word is not blank, but the value of the corresponding `definition_X` variable **is** blank, you should prompt the user to define the word, but instead of showing the correct definition, your code should print `-- No definition found --`

## Phase Five

1. Add code at the very end of the program to clear the terminal and display the words and definitions. You can reuse the code you commented out in Phase Two.

1. Update your code to only print word/definition pairs if the word is not blank.

## Example

When your program is complete, it should behave something like this:

> **NOTE:** In this example, the third word's definition is blank and the fourth word is blank.

![Vocabulary Example](./vocabulary.svg)

## Challenge

Change your code to disallow blank words and definitions. If a user enters a blank word, you should prompt them to reenter it until they enter something other than a blank.

Do the same with definitions. Do not make them reenter the word, only the definition.
