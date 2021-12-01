# Jumpstart Project - Clothesline

# WIP

A central tenet of the NSS philosophy is the importance of hands-on learning. We know you learn better by doing than by any other means. Throughout this course you will be writing lots of code. This will include small exercises, as well as a larger project. This document describes that larger project, a game called _Clothesline_.

## Clothesline

Clothesline is a guessing game in which a player attempts to guess the letters that make up a secret word. When the game starts the player can see how many characters are in the word, but doesn't know any of the actual letters. On each turn the player guesses a single letter. If that letter is in the secret word, the position of that letter is revealed. However, if the letter is not in the secret word, the incorrect guess is recorded. A player has a limited number of incorrect guesses. If the player runs out of guesses before they reveal the entire secret word, they lose. If they manage to reveal the secret word, they win.

The number of remaining incorrect guesses is depicted by an [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art) image of shirts on a clothesline. At the start of the game there are four shirts and eight clothespins.

```txt
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````
```

> <sub>_Isn't that art simply breathtaking???_</sub>

When the player guesses incorrectly, one of the clothespins is removed.

```txt
=====!=====!=======!=====!=======!=====!=======!======
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|
```

When two clothespins are removed the shirt falls off the clothesline.

```txt
=====!=====!=======!=====!=======!=====!==============
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
```

If all the shirts fall before the secret word is guessed, the player loses.

> **NOTE:** By now many of you have recognized this game as a barely camouflaged version of the classic game, [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)). In fact, when creating the project, we originally created a hangman game, but along the way decided clothes on a line were more fun than repeatedly hanging some random stick-figure dude.

## The Project

This project will be broken into several phases. You should complete each phase in order. Many phases - especially the earlier ones - are very short. It may be tempting to work on more than one phase at a time. **Resist this temptation.** Part of being a software engineer is being deliberate and methodical, and sometimes that means moving slowly. **Once a phase is complete do NOT move to the next until you run the program to test it.**

> **NOTE:** Remember, you may need to run the program multiple times in order to fully test a single phase.

As you go through this project, you'll sometimes be asked to add code in one phase that is then removed in a later phase. This is a standard part of the software development process and isn't just us messing with you.

### Phase One

Create a new folder in your workspace called `clothesline`, then open that folder in Visual Studio Code and create a new Python file called `clothesline.py`.

Add code to `clothesline.py` to print "Welcome to Clothesline!" to the screen.

> **NOTE:** Remember to run the code to confirm it works before moving on to the next phase.

### Phase Two

Create a variable called `secret_word` and assign it the value `"apple"`.

Create another variable called `message` and assign it to the `"The secret word is: "`.

Print the sentence, "The secret word is: apple" by using string concatenation to join the `message` and `secret_word` variables.

### Phase Three

Create a variable called `secret_word_length` and use the `len()` function to set it to the length of the `secret_word`.

Print a message that displays the secret word and it's length.

### Phase Four

In this phase we need to create the "blanks" that the player will fill in when they make a correct guess. We want to display an individual dash character (`-`) for each letter in the `secret_word`.

For example if the secret word is "apple", the program should print five dashes, `-----`. If the word is "pear", the program should print four dashes, `----`.

Create a variable called `guess` and assign it to be a string of dashes that is the same length as the `secret_word`.

> **NOTE:** When testing this phase, you should change the value of `secret_word` to be various words of differing lengths.

### Phase Five

Now it's time to get some input from the user.

First, ask the user to enter a letter by printing the text: "Guess a letter...if you dare!".

Next, use the `input()` function to get the letter the user enters. Save that value to a variable called `letter`.

The input function should display a `> ` as a prompt, such that when the program runs you should see something like this:

```txt
Guess a letter...if you dare!
> _
```

When the user types in a character and hits the `Enter` key the value of the character should be saved into the `letter` variable.

Finally, print the value of the `letter` variable just to ensure everything is working properly.

### Phase Six

At this point our code is a bit messy. Let's clean it up.

First, remove all the extraneous `print()` calls. The only things that should be printed to the screen are the dashes and the prompt that asks the user to enter a letter.

> **NOTE:** This is a good time to remind you that you can run your program whenever you think it would be helpful. You don't have to wait until the end of a phase.

Next, move your code into a `main` function. We'll be adding several functions as we continue to build Clothesline, but for now we only need one. Create a function called `main` and move your code into it. Don't forget to indent the code inside the new function.

If you run the program now, with the code all neatly nestled inside the `main` function, you might be surprised to find that nothing happens. Why? Well, recall that a function will only run when it's _called_. So in order to make our code run we need to add a line that calls the `main()` function. Add this code to the bottom of the file.

After you complete the changes, you're `clothesline.py` file should look something like this:

```python

def main():
    # ...
    # code that creates variables,
    # prints messages and gets input
    # ...
    
main()
```

### Phase Seven

As you run and rerun your program, you've surely noticed how messy your terminal window is becoming. It's distracting to see the output from previous runs. And if it's distracting for us, just imagine how a player will feel. Clothesline is supposed to be a fun game, so it's best not to irritate the player.

What can we do about it? Why not clear the terminal window each time the game starts? That way the user will only see the current iteration of the game.

It turns out that clearing the screen in Python code isn't as straightforward as you might expect it to be, so just this once, we're going to provide you with the code to do it. Copy this function into your `clothesline.py` file.

```python
def clear_screen():
    print("\033[H\033[J", end="")
```

> **NOTE:** What's actually happening in this code is well beyond the scope of this course. However, there is a lesson to be learned here. There are times you've just gotta trust the code you're given. Many students have a hard time accepting this, but it's just how it is. Perhaps it'll help to remind you that you have no idea how the `print()` function works and you've been using that without question.

Add a call to `clear_screen()` to the top of the `main` function. Now every time the `main` function runs, the terminal will be cleared.

### Phase Eight

In the `main` function, create a variable called `incorrect_count` and assign it to be the number `0`. We'll use this variable to keep track of how many times the user makes a bad guess.

To determine if the user's guess is correct or not, create a function called `is_letter_in_word` that should accept two parameters, `letter` and `word`. The function should return `True` if the `letter` is in the `word` and `False` if the `letter` is not in the `word`.

Add code to the `main` function to call the `is_letter_in_word` function below the code that gets the input from the user. Pass in `letter` and `secret_word` as parameters.

Use the return value from the `is_letter_in_word` function to print a message informing the user if they guess correctly or not.

<details>

<summary><b>Click here to see an example of calling <code>is_letter_in_word</code></b></summary>

```python
# ...  other code ...

print("Guess a letter...if you dare!")
letter = input("> ")

is_correct = is_letter_in_word(letter, secret_word)

if is_correct == True:
    print("Good Guess!")
else:
    print("You're terrible at guessing.")

# ...  other code ...
```

</details>

### Phase Nine

Unless the secret word is very short, letting the user only guess one letter isn't going to work very well. Instead, we need to repeatedly ask the user for guesses. And what do we use when we want to do something more than once in our code? That's right, a loop.

Add a `while` loop to the `main` function. The loop should continue as long as `incorrect_count < 8`. Move the code that prompts the user, checks the guess and prints the result into the body of the `while` loop, remembering to indent properly.

In order to make the loop stop you'll need to add `1` to the `incorrect_count` variable each time the user guesses incorrectly. Write the code to do that now. Make sure to test your program.

> **NOTE:** Adding `1` to a number is so common in programming that it has a special name. We call it "incrementing". We also use the word "decrementing" for subtracting `1` .

### Phase Ten

Let's take a step closer to displaying our clothesline ASCII art. We won't draw the beautiful picture just yet, but we'll set the stage.

Create a new function called `print_clothesline` that takes the `incorrect_count` as a parameter. For now this function should just print a message that tells the user how many incorrect guesses they have left. The should start with eight (`8`) changes and lose one for each incorrect guess.

Add a call to `print_clothesline` to the top of the `while` loop so that it is displayed each time the user enters a letter.

### Phase Eleven

Things are getting messy again. Let's fix that.

Move the call to `clear_screen` so that it will clear the screen before prompting the user to enter a letter. In addition to the prompt, make sure that the number of remaining chances and the row of dashes are visible.

Now a few minutes to add some `print()` calls to display some blank lines around the output. Use your judgement as to what will make the output more readable.

### Phase Twelve

A few phases back you added code to display a row of dashes that has the same length as `secret_word`. You stored these dashes in a variable called `guess` and printed it to the screen. It's finally time to do something with the `guess` variable.

The goal of printing the `guess` variable is to visually indicate how many letters are in the secret word, and to display the location of letters when they are correctly guessed.

This means you'll need to change the value of `guess` after the user enters a correct guess. For example, if `secret_word` is `"apple"`, initially the value of `guess` will be:

```txt
"-----"
```

If the user types an `e` you should change `guess` to be

```txt
"----e"
```

Then, if the user types a `p`, `guess` should become

```txt
"-pp-e"
```

Create a function called `update_guess`. This function should take three parameters: `old_guess`, `letter` and `secret_word`. Add code to this function that will return a new string that has the new value of `guess`. Take a look at the following code for an example of how `update_guess` should work:

```python
guess = "-----"
secret_word = "apple"

guess = update_guess(guess, "e", secret_word)
print(guess) # should print: ----e

guess = update_guess(guess, "p", secret_word)
print(guess) # should print: -pp-e
```

> **NOTE:** Notice that the code above changes the `guess` variable, setting it to the value returned by `update_guess`.

Add a call to `update_guess` into the body of your `while` loop. You should call `update_guess` only after the user has entered a correct guess. Set the `guess` variable equal to the return value of `update_guess`. If the user entered an incorrect guess, you do NOT need to call `update_guess` and you do not need to update the `guess` variable.

> **NOTE:** The example above calls `update_guess` twice, but in your code you should add the call into the body of the `while` loop, so you only need to call it once.

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

_Have you written the `update_guess` function yet?_

...

...

...

...

...

...

...

...

...

_It's kinda a lot, isn't it?_

...

...

...

...

...

...

...

...

...

...

...

...

...

...

_You should definitely try to write it._

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

...

_But it's ok if it's too much._

...

...

...

...

...

<details>
<summary><b>Click here to see an implementation of the <code>update_guess</code> function<b></summary>

```python
def update_guess(old_guess, letter,  word):
    new_guess = ""
    for i in range(len(old_guess)):
        if word[i] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[i]

    return new_guess
```

<details>