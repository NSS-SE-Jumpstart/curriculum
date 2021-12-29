# Exercise - Rolling Dice

In this exercise, you'll write a game that pits a human player against the computer to see who's luckiest.

This exercise is divided into phases. Make sure you complete one phase at a time, and you **run your program to test it** after you finish each phase.

> **NOTE:** In addition to running your code after each phase, remember you can also run your program before you finish a phase. This can often be useful when debugging errors.

## Phase One

In this first phase you'll get setup by creating and running a simple Python program just to make sure everything is working properly.

1. Create a new Python file called `dice.py`.
1. Open `dice.py` in Visual Studio Code and write code to print `Hello, World!` to the terminal.
1. Run the program to test it.

```sh
python3 dice.py
```

## Phase Two

Now that you know you can successfully write and run some Python code, you should remove the code that prints `Hello, World!` and replace it with the code from the [Import a Little Randomness](./../prework/import_random.md) lesson.

Here's the code so you don't have to go back to that lesson if you don't want to.

```python
import random

die_roll = random.randint(1, 6)
print("You rolled: " + str(die_roll))
```

Save and run the new program. You should run it a few times to ensure you get various numbers.

## Phase Three

The serious nerds among you may be aware that dice are not limited to six sides. There's a wide array of different types of dice.

![multiple sizes of dice](https://www.allaboutlean.com/wp-content/uploads/2019/11/D4-D6-D8-D10-D12-D20-Dice-Red.jpg)

Make your game more interesting by changing your code from a six-sided die to a twenty-sided die.

Once you've made the change, run the program a few times to make sure it's working.

## Phase Four

The `dice_roll` variable is for storing the human player's roll. Make that intention more clear by renaming it to `human_roll`.

Now that you have a `human_roll`, It's time for a `computer_roll`. Write code to roll a second twenty-sided die and save the value of the roll into a variable called `computer_roll`. Print the result of the computer roll along side the human roll.

When you run your program the output should look something like this:

```txt
You rolled: 12
Computer rolled: 9
```

## Phase Five

Calling the human player "you" is so impersonal. You should give your user a name. How about "Xena"?

Create a variable called `human_player` and set it equal to the string, `"Xena"`. Update the `print()` call to print the value of the `human_player` variable.

Do **NOT** simply replace the string, `"You"` with the string `"Xena"`. Make sure you use the `human_player` variable.

When you run your program the output should look something like this:

```txt
Xena rolled: 12
Computer rolled: 9
```

## Phase Six

Now, we're being rude to the computer. It doesn't want to be called "computer" any more than you want to be called "human". It wants to be called "Graptor-3000"...because that's it's name.

Update your program to create a `computer_player` variable, set it's value to `"Graptor-3000"` and display it when displaying the computer's roll.
