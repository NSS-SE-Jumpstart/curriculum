# Jumpstart Project - Clothesline

A central tenet of the NSS philosophy is the importance of hands-on learning. We know you learn better by doing than by any other means. This is why we've devoted the last part of the course to a project - a game called _Clothesline_. While you will certainly learn new things while working on this project, the primary goal is reinforcing what you've already learned.

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
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


```

When two clothespins are removed the shirt falls off the clothesline.

```txt
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````
```

If all the shirts fall before the secret word is guessed, the player loses.

> **NOTE:** By now many of you have recognized this game as a barely camouflaged version of the classic game, [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)). In fact, when creating the project, we originally created a hangman game, but along the way decided clothes on a line were more fun than repeatedly hanging some random stick-figure dude.

## A Preview of Things to Come

To help you envision what you'll be building, we've created a version of _Clothesline_ for you to download and run. You won't be able to see the code, but you can begin to get a feel for how it should work. You can think of this as the _reference implementation_ of Clothesline.

To run the reference implementation:

1. In your terminal, create a new directory called `clothesline` in your `workspace` directory.
1. Download the [program](./clothesline_reference.py). Save it in the newly created `clothesline` directory.
1. In your terminal, `cd` into the `clothesline` directory and run the program.

    ```sh
    python3 clothesline_reference.py
    ```

1. You should see something that looks like this

    ```txt
    =====!=====!=======!=====!=======!=====!=======!=====!=====
        /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
       /         \   /         \   /         \   /         \
      '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
         |     |       |     |       |     |       |     |
         |     |       |     |       |     |       |     |
         ```````       ```````       ```````       ```````




    Word:    ---
    Guesses: 

    Guess a letter...if you dare!
    > 
    ```

1. Guess a few letters, you know...if you dare.

> **NOTE:** The further along you get in this project, the closer your program should become to the `clothesline_reference.py` program. It is a good idea to periodically run the reference program to help you remember how your program is supposed to work.

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

In this phase you need to create the "blanks" that the player will fill in when they make a correct guess. You want to display an individual dash character (`-`) for each letter in the `secret_word`.

For example if the secret word is "apple", the program should print five dashes, `-----`. If the word is "pear", the program should print four dashes, `----`.

Create a variable called `guess` and assign it to be a string of dashes that is the same length as the `secret_word`.

There are multiple ways you might accomplish creating a string with a variable number of dashes. You can use a `while` or `for` loop, or you can explore using [the `*` operator to repeat a string](https://www.kite.com/python/answers/how-to-repeat-a-string-in-python).

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

First, remove all the extraneous `print()` calls. Also remove any variables that you're no longer using, such as the `message` variable. The only things that should be printed to the screen are the dashes and the prompt that asks the user to enter a letter.

> **NOTE:** This is a good time to remind you that you can run your program whenever you think it would be helpful. You don't have to wait until the end of a phase.

Next, move your code into a `main` function. You'll be adding several functions as you continue to build Clothesline, but for now you only need one. Create a function called `main` and move your code into it. Don't forget to indent the code inside the new function.

If you run the program now, with the code all neatly nestled inside the `main` function, you might be surprised to find that nothing happens. Why? Well, recall that a function will only run when it's _called_. So in order to make your code run you need to add a line that calls the `main()` function. Add this code to the bottom of the file.

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

What can you do about it? Why not clear the terminal window each time the game starts? That way the user will only see the current iteration of the game.

You've already countered the "magical" terminal-clearing code earlier in this course. This time, however, you should place it into a function called `clear_screen()`. Copy the function below and paste it into your `clothesline.py` file.

```python
def clear_screen():
    print("\033[H\033[J", end="")
```

> **NOTE:** What's actually happening in this code is well beyond the scope of this course. However, there is a lesson to be learned here. There are times you've just gotta trust the code you're given. Many students have a hard time accepting this, but it's just how it is. Perhaps it'll help to remind you that you have no idea how the `print()` function works and you've been using that without question.

Add a call to `clear_screen()` to the top of the `main` function. Now every time the `main` function runs, the terminal will be cleared.

### Phase Eight

In the `main` function, create a variable called `incorrect_count` and assign it to be the number `0`. You'll use this variable to keep track of how many times the user makes a bad guess.

To determine if the user's guess is correct or not, create a function called `is_letter_in_word` that should accept two parameters, `letter` and `word`. The function should return `True` if the `letter` is in the `word` and `False` if the `letter` is not in the `word`.

Add code to the `main` function to call the `is_letter_in_word` function below the code that gets the input from the user. Pass in `letter` and `secret_word` as parameters.

Use the return value from the `is_letter_in_word` function to print a message informing the user if they guess correctly or not.

<details>

<summary><b>&#128276; Click here to see an example of calling <code>is_letter_in_word</code> &#128276;</b></summary>

```python
# ...other code omitted...

print("Guess a letter...if you dare!")
letter = input("> ")

is_correct = is_letter_in_word(letter, secret_word)

if is_correct == True:
    print("Good Guess!")
else:
    print("You're terrible at guessing.")

# ...other code omitted...
```

</details>

### Phase Nine

Unless the secret word is very short, letting the user only guess one letter isn't going to work very well. Instead, you need to repeatedly ask the user for guesses. And what do you use when you want to do something more than once in our code? That's right, a loop.

Add a `while` loop to the `main` function. The loop should continue as long as `incorrect_count < 8`. Move the code that prompts the user, checks the guess and prints the result into the body of the `while` loop, remembering to indent properly.

In order to make the loop stop you'll need to add `1` to the `incorrect_count` variable each time the user guesses incorrectly. Write the code to do that now. Make sure to test your program.

> **NOTE:** Adding `1` to a number is so common in programming that it has a special name. We call it "incrementing". We also use the word "decrementing" for subtracting `1` .

### Phase Ten

Let's take a step closer to displaying our clothesline ASCII art. Sadly, you won't get to draw the beautiful picture just yet, but you'll set the stage.

Create a new function called `print_clothesline` that takes the `incorrect_count` as a parameter. For now this function should just print a message that tells the user how many incorrect guesses they have left. The should start with eight (`8`) changes and lose one for each incorrect guess.

Add a call to `print_clothesline` to the top of the `while` loop so that it is displayed each time the user enters a letter.

### Phase Eleven

Things are getting messy again. Let's fix that.

Move the call to `clear_screen` so that it will clear the screen before prompting the user to enter a letter. In addition to the prompt, make sure that the number of remaining chances and the row of dashes are visible.

> **NOTE:** Remember the "row of dashes" is stored in the `guess` variable. Make sure you are printing the `guess` variable after you call `clear_screen()`

Now a few minutes to add some `print()` calls to display some blank lines around the output. Use your judgement as to what will make the output more readable.

### Phase Twelve

A few phases back you added code to display a row of dashes that has the same length as `secret_word`. You stored these dashes in a variable called `guess` and printed it to the screen. Since creating the `guess` variable, you haven't really done all that much with it. It's finally time to change that.

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
<summary><b>&#128276; Click here to see an implementation of the <code>update_guess</code> function &#128276;</b></summary>

```python
def update_guess(old_guess, letter,  word):
    new_guess = ""
    for index in range(len(old_guess)):
        if word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]

    return new_guess
```

> **NOTE:** Do not blindly accept that this code works. It's ok to copy code from trusted sources, but you should **NEVER** add code to your project until you understand it. Carefully read this code. Does it make sense? Could you describe it to someone else? If not, ask for help.

</details>

### Phase Thirteen

Displaying an unlabeled row of dashes to the user isn't exactly the greatest user experience. Add a `Word:    ` label before the dashes. This will let the user know that the dashes represent the secret word.

Add four spaces after the colon (`:`). That will make things look nicer once we add the feature to display the user's previously guessed letters.

### Phase Fourteen

As you've been testing your game, have you noticed how easy it is to forget which letters you've already guessed? How many times have you guessed the same, incorrect, letter without realizing it? Let's fix that.

Inside the `main()` function, create a new list called `letters_guessed`. We'll use this to store the letters the user has entered.

At this point, your code should be storing the letter the user enters into a variable called `letter`. Do not change this code, but add code below it to use the `append()` function to add the `letter` to the `letters_guessed` list.

Below the code that prints the `guess` varaible, use the `print()` function to display `"Guesses: "` followed by the `letters_guessed` list.

> **NOTE:** This is a great opportunity to run the reference program to see how this feature works. When you do, you'll notice that your "Guesses" list looks a little different from the reference program. This is fine for now.

### Phase Fifteen

Take a look at what you've built. You've almost got a working game. In fact, it does nearly everything it needs to do and, even now, it's playable.

One thing it doesn't (yet) do is end when the player wins. Let's fix that.

How do you know if the player has won? In a previous phase you added code to update the `guess` variable each time the user enters a correct letter. Each correct letter brings the value of the `guess` variable more inline with the value of the `secret_word` variable.  So, when has the user won the game? When the `guess` and `secret_word` variables are equal.

Add code to the `while` loop to ensure it loops when the user hasn't run out of chances and the `guess` variable is not equal to the `secret_word` variable. If should stop looping if the user runs out of chances or they guess every letter in the secret word.

### Phase Sixteen

Right now your program prints a message after the user enters a letter. This message lets the user know if they guessed correctly or not. This seems unnecessary now that your are updating the `guess` variable and displaying it's value each time through the `while` loop. Remove the code that displays the message.

In the previous phase you changed your program to end when a player wins or loses, but there is no "You Win" or "You Lose" message being displayed. Add code after the `while` loop that determines whether or not the user won and prints the appropriate message.

### Phase Seventeen

It's finally time to add the clothesline to your `clothesline.py` program.

Update the `print_clothesline` function to print the appropriate clothesline "image".  Your code should use the `incorrect_count` parameter to determine the "image" do display. For example if the value of `incorrect_count` is `0`, you should print a clothesline with four shirts and eight clothespins. If `incorrect_count` is `1`, you should print a clothesline with the last clothespin removed.

Do **NOT** go to the trouble of creating all this ASCII art. [We've done it for you](./clothesline_frames.md). You're welcome.

> **NOTE:** In each ASCII art string, you'll see an `r` in front of the triple quotes. This creates a "raw" string. It's not important that you understand exactly what that means, but in short it prevents Python from doing strange things with strings that contain backslash (`\`) characters. You will need to use raw strings for the ASCII art strings.

Here's a snippet of code that creates a `clothesline` variable with all four shirts and all eight clothespins.

```python
clothesline = r"""
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````
"""
```

Here's a snippet of code that creates a `clothesline` variable with the right-most clothespin removed.

```python
clothespin = r"""
=====!=====!=======!=====!=======!=====!=======!======
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|
"""
```

#### Important

It may be tempting to try to think of a _clever_ approach to "efficiently" print the clothesline image. Do not do this. It's perfectly fine to have nine different versions of the clothesline image and to use an `if/elif/else` statement to choose the right one.

### Phase Eighteen

Pause a moment. Look back at what you've built. It's a lot. What do you think of it? Are you proud of it? You should be.

We know. We know. We're not supposed to tell you how you _should_ feel. What you feel is, simply, what you feel. Whatever you feel is fine and valid and all that...

Still, though, you should be proud. Seriously.

### Phase Nineteen

The game works. It's great. As long as the secret word is "apple"...

Way back at the beginning of this project, you created a variable called `secret_word` and set its value to the string `"apple"`. As you've tested you may have changed the value to another word, but each time you run the program, you know what the word is. Where's the fun in that?

Create a new function called `pick_secret_word` that will return a secret word. Inside `pick_secret_word` create a new `list` called `secret_word_options`. Set `secret_word_options` to be a list of words. Five or six words is plenty for now. Feel free to come up with your own or you can use these: `["apple", "pear", "banana", "grape", "scorpion", "umbrella"]`.

The next step is to write code to choose a random item from the list to be the secret word. For this you'll use a function that's built into Python called [random.choice](https://www.w3schools.com/python/ref_random_choice.asp). At the top of your Python file import that `random` module. Then, inside the `pick_secret_word` function, call the `random.choice()` function passing the `secret_word_options` list as an argument. Save the result of calling `random.choice()` in a variable called `random_secret_word` and the return `random_secret_word` from the `pick_secret_word` function.

Now return to the `main` function and change the code that sets the `secret_word` variable so that it calls the `pick_secret_word` function and sets `secret_word` to the value that `pick_secret_word` returns.

After making these changes, you should get a new secret word each time you run the program.

<details>
<summary><b>&#128276; Click here to see an implementation of <code>pick_secret_word</code> &#128276;</b></summary>

```python
import random

# ...other code omitted...

def pick_secret_word():
    secret_word_options = ["apple", "pear", "banana", "grape", "scorpion", "umbrella"]
    random_secret_word = random.choice(secret_word_options)
    return random_secret_word
```

</details>

<details>
<summary><b>&#128276; Click here to see an example of calling <code>pick_secret_word</code> &#128276;</b></summary>

```python
def main():
    # ...other code omitted...

    secret_word = pick_secret_word()

    # ...other code omitted...
```

</details>

## Phase Twenty

Take a look at your code. Is it readable? Will you be able to understand it after a few days or weeks? Do you need to improve any variable names or right clearer comments? Would it help to pull some of the code out into a separate function?

After you're satisfied with the code, You might want to add a few more words to the `secret_word_options` list so playing the game becomes more fun.

## Congratulations

You did it. You built a working game. Take some time to celebrate. Maybe play _Clothesline_ for a while.

## Challenge

One of the universal truths about software is: _software is never done_. We can always add more and more. This is not to say that we _should_ add more, but we always _can_ add more.

The remainder of this document describes some additional, _challenge_ features you might like to add to your version of the _Clothesline_ game.

### Challenge Phase One

The way that your program displays the guessed letters, is far from ideal. If you look at the reference implementation, you'll notice that the letters are printed out individually with a single space in between each letter.

Your challenge is to make you program behave the same way as the reference implementation.

### Challenge Phase Two

Your program prompts the user to enter a single letter, but what happens if the user enters more than one letter? Does it behave the way you'd like?

For this challenge, you should modify your code to only work with the first letter the user enters. For example, if the user types "dog", your program should behave as though they only typed a "d", and should ignore the "og".

### Challenge Phase Three

It's time to get fancy. Oh, yes...fancy...

Maybe you thought things were already pretty fancy. Maybe they are. It depends on your definition of "fancy". You know the old saying "fancy is in the eye of the beholder"

Anyway, it's time to get fancy.

Having a list of options for the secret word is clearly better than only having a single secret word, but, practically speaking, that list can only get so big before it becomes unmanageable. There's got to be a better way.

So, what's the alternative? What's the better way?

Before we answer that, let's pause and revisit what we're building. _Clothesline_ is a guessing game in which a player tries to guess a secret word. There are a couple of ideas implied in that description. First, we have the _game_ itself. The game is the code. It's the instructions that the computer executes in order to let the player play. Second, we have the _secret word_. The secret word is the _data_ that the game uses. The code that makes up the game **does not care** what the secret word is.

That last sentence is interesting. The code doesn't care about the value of the secret word. It can be "apple" or "aardvark" or "tintinnabulation". All the code expects is that there is some word - _any word_ - stored in the `secret_word` variable.

This separation between _the code_ and _the data_ is a key concept in software development. It influences the way we design and build software. In the _Clothesline_ game, it will lead us to pull the list of secret word options into a separate text file.

We'll do that in the next phase.


### Challenge Phase Four

Welcome to the next phase.

In this phase, you'll download a few text files containing several secret word options and you'll update your code to read from one of these files when picking a secret word.

Start by downloading this file: [easy_words.txt](./easy_words.txt).

Next, open `easy_words.txt` in Visual Studio Code. You'll see it contains a list of words with one word on each line.

Your task is to "read" the words from the file into your Python program. However, since this is a challenge, we're going to ask you to figure out how to do that. You might want to begin your search here: https://pythonspot.com/read-file/

Once you feel ready, modify the `pick_secret_word` function to open the `easy_words.txt` file, read the words into a list and choose a random secret word from the list.

> **NOTE:** Remember, your instructors are here to help you, but we want you to give it a try on your own first.

If you stuck or you want to compare check your solution, you can find an example below:

<details>
<summary><b>&#128276; Click here to see an example implementation of <code>pick_secret_word</code> &#128276;</b></summary>

```python
def pick_word():
    word_filename = "easy_words.txt"
    word_file = open(word_filename)
    all_text = word_file.read()
    all_words = all_text.splitlines()
    word_file.close()

    word = random.choice(all_words)
    return word

```

</details>

<p></p>

> **NOTE:** Here are a few more word files you may want to play with after you get `easy_words.txt` working.
> 
> * [animals.txt](./animals.txt)
> * [fruits.txt](./fruits.txt)
> * [hard_words.txt](./hard_words.txt)
