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

Save and run the new program. You should run it a few times to ensure you get different numbers each time.

## Phase Three

Before we get very far with this exercise, let's do something that will make our lives a little easier. Let's introduce a function to contain the code in our program.

1. Create a function called `main()` and place the last two lines of your script inside of it. Do not put the `import random` line within the function.
1. Run the code to see what happens. Is it what you expected?

<details>
<summary> :game_die: Click here after you've run your program... :game_die: </summary>

3. Your code didn't do anything because you didn't call the `main()` function. Add code at the bottom of the `dice.py` file to call `main()`. When you're finished, your script should look like this:

    ```python
    import random

    def main():
        die_roll = random.randint(1, 6)
        print("You rolled: " + str(die_roll))


    main()
    ```

4. Now run your program again to see what happens. Is it what you expected?

> **NOTE:** It may seem unnecessary to do this, but it's good practice to use functions to organize your code.

</details>

## Phase Four

The serious nerds among you may be aware that dice are not limited to six sides. There's a wide array of different types of dice.

![multiple sizes of dice](https://www.allaboutlean.com/wp-content/uploads/2019/11/D4-D6-D8-D10-D12-D20-Dice-Red.jpg)

1. Add a new function called roll_die. It should take a parameter called `max_value`. The function should return a random number between `1` and `max_value`. Here's a bit of code to get you started.

    ```python
    def roll_die(max_value):
        # do something here to get a random int between 1 and max_value
        # then `return` that number
    ```

1. Make your game more interesting by changing your code from a six-sided die to a twenty-sided die. Do this by replacing the call to `random.randint(1, 6)` with a call to your new function, passing `20` as a parameter.

    ```python
    def main():
        die_roll = roll_die(20)
        print("You rolled: " + str(die_roll))
    ```

Once you've made the change, run the program a few times to make sure it's working.

## Phase Five

The `die_roll` variable is for storing the human player's roll. Make that intention more clear by renaming it to `human_roll`.

Now that you have a `human_roll`, It's time for a `computer_roll`. Write code to roll a second twenty-sided die and save the value of the roll into a variable called `computer_roll`. Print the result of the computer roll along side the human roll.

When you run your program the output should look something like this:

```txt
You rolled: 12
Computer rolled: 9
```

## Phase Six

Calling the human player "you" is so impersonal. You should give your user a name. How about "Xena"?

Inside the `main()` function, create a variable called `human_player` and set it equal to the string, `"Xena"`. Update the `print()` call to print the value of the `human_player` variable.

Do **NOT** simply replace the string, `"You"` with the string `"Xena"`. Make sure you use the `human_player` variable.

When you run your program the output should look something like this:

```txt
Xena rolled: 12
Computer rolled: 9
```

## Phase Seven

Now, we're being rude to the computer. It doesn't want to be called "computer" any more than you want to be called "human". It wants to be called "Graptor-3000"...because that's it's name.

Update your program to create a `computer_player` variable, set it's value to `"Graptor-3000"` and display it when displaying the computer's roll.

## Phase Eight

At this point, your game leaves it up to the human player to read the output and determine whether or not they won. They actually have to **compare numbers!** But comparing numbers is computer-work. Let's make the computer do it.

1. Create a function called `determine_winner()`. This function should take four parameters, `human_player`, `human_roll`, `computer_player` and `computer_roll`. The function should use an `if` statement to determine who won. It should return the name of the winner or, if there's a tie, it should return the string `"tie"`.

1. Back in the `main()` function, save the result of calling `determine_winner()` into a variable and use that variable in a `print()` that announces who won. For example if Xena wins, the program should print `"Xena wins!"` and if Graptor-3000 wins, the program should print `"Graptor-3000 wins!"`. However 

1. If `determine_winner()` returns the string `"tie"`, let's do the hippie thing and say both players win. If there's a tie, your program should **NOT** print either of the winning messages described above. It should print a single message that says: `Both Xena and Graptor-3000 win!`

## Phase Nine

Your game is getting closer to actually being fun. It's sort of irritating that you can only roll once though.

Update the code the play the game five times. Don't just copy/paste the code. Use a `while` loop and a `counter` variable. Initially `counter` should be set to `0`. On each iteration of the loop add `1` to `counter`. Make the loop stop when `counter == 5`.

Make sure you place the code that calls `roll_die()` and the code the prints the results within the loop. When you run the program, the output should look something like this:

```txt
Xena rolled: 12
Graptor-3000 rolled: 9
Xena wins!

Xena rolled: 1
Graptor-3000 rolled: 20
Graptor-3000 wins!

Xena rolled: 7
Graptor-3000 rolled: 7
Both Xena and Graptor-3000 win!

Xena rolled: 8
Graptor-3000 rolled: 9
Graptor-3000 wins!

Xena rolled: 4
Graptor-3000 rolled: 1
Xena wins!
```

## Phase Ten

It's come to our attention that some humans aren't named Xena.

Update the code to prompt the user to input their name and save that into the `human_player` variable.

Make sure your code always uses the `human_player` variable when it prints the name and doesn't have any "Xena"s hanging out.

## Phase Eleven

Update the game to display the number of rounds each player won after the final round.

Use two variables, `human_wins` and `computer_wins` to keep track of the number of wins. Remember a tie means both players win. Print the values of these variables - along with a friendly message to the user - **after** the `while` loop.

> **NOTE:** This phase requires you to change code in the `main()` function. You should not have to change any code in the `determine_winner()` function.

## Phase Twelve

Add code to display the name of the overall winner. The overall winner is the player that wins the most rounds.

## Phase Thirteen

Now we need to ask if our human friend would like to play again by taking an input for (Y/n).  If they put in Y, our human friend can play again, otherwise we want to ignore the input. Hint: We can use another while loop on the outside with a boolean for playing again.  Also remember ties are possible with playing again, so be sure to check for ties for the final winner. 
