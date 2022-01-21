# Looping

Consider the following code

```python
y_or_n = input("Are you a programmer? (y/n) ")

if y_or_n == "y":
    print("Darn right, you are!")
elif y_or_n == "n":
    print("You're WRONG! You ARE a programmer!")
else:
    print("Please enter 'y' or 'n'.")
```

If you run the code above and enter some text other than `y` or `n`, you'll be informed that you should enter `y` or `n`, but then the program will just end without giving you a chance to try again. That's not a great user experience.

Instead we'd like to go back and let the user try again. We could do this.

```python
y_or_n = input("Are you a programmer? (y/n) ")

if y_or_n == "y":
    print("Darn right, you are!")
elif y_or_n == "n":
    print("You're WRONG! You ARE a programmer!")
else:
    print("Please enter 'y' or 'n'.")

    y_or_n = input("Are you a programmer? (y/n) ")

    if y_or_n == "y":
        print("Darn right, you are!")
    elif y_or_n == "n":
        print("You're WRONG! You ARE a programmer!")
    else:
        print("Please enter 'y' or 'n'.")
```

Hmm ... that code is pretty hard to read, but once you do decipher it, you'll see that it gives the user two chances to enter `y` or `n`. You could argue that's better, but what's to stop the user from entering the wrong thing the second time?

How about this?

```python
y_or_n = input("Are you a programmer? (y/n) ")

if y_or_n == "y":
    print("Darn right, you are!")
elif y_or_n == "n":
    print("You're WRONG! You ARE a programmer!")
else:
    print("Please enter 'y' or 'n'.")

    y_or_n = input("Are you a programmer? (y/n) ")

    if y_or_n == "y":
        print("Darn right, you are!")
    elif y_or_n == "n":
        print("You're WRONG! You ARE a programmer!")
    else:
        print("Please enter 'y' or 'n'.")

        y_or_n = input("Are you a programmer? (y/n) ")

        if y_or_n == "y":
            print("Darn right, you are!")
        elif y_or_n == "n":
            print("You're WRONG! You ARE a programmer!")
        else:
            print("Please enter 'y' or 'n'.")
```

Or this?

```python
y_or_n = input("Are you a programmer? (y/n) ")

if y_or_n == "y":
    print("Darn right, you are!")
elif y_or_n == "n":
    print("You're WRONG! You ARE a programmer!")
else:
    print("Please enter 'y' or 'n'.")

    y_or_n = input("Are you a programmer? (y/n) ")

    if y_or_n == "y":
        print("Darn right, you are!")
    elif y_or_n == "n":
        print("You're WRONG! You ARE a programmer!")
    else:
        print("Please enter 'y' or 'n'.")

        y_or_n = input("Are you a programmer? (y/n) ")

        if y_or_n == "y":
            print("Darn right, you are!")
        elif y_or_n == "n":
            print("You're WRONG! You ARE a programmer!")
        else:
            print("Please enter 'y' or 'n'.")

            y_or_n = input("Are you a programmer? (y/n) ")

            if y_or_n == "y":
                print("Darn right, you are!")
            elif y_or_n == "n":
                print("You're WRONG! You ARE a programmer!")
            else:
                print("Please enter 'y' or 'n'.")

                y_or_n = input("Are you a programmer? (y/n) ")

                if y_or_n == "y":
                    print("Darn right, you are!")
                elif y_or_n == "n":
                    print("You're WRONG! You ARE a programmer!")
                else:
                    print("Please enter 'y' or 'n'.")

                    y_or_n = input("Are you a programmer? (y/n) ")

                    if y_or_n == "y":
                        print("Darn right, you are!")
                    elif y_or_n == "n":
                        print("You're WRONG! You ARE a programmer!")
                    else:
                        print("Please enter 'y' or 'n'.")
```

You can see where we're going here. This is just ridiculous. We've added tons of repetitive code and _still_ there's no guarantee that it's enough. There's got to be a better way.

> **NOTE:** If anything can be said to be truly certain in the world of software engineering, it's this: _If it's possible for a user to do something, eventually at least one of them will._

## The `while` Loop

Here's a version of the above code that actually works.

```python
y_or_n = input("Are you a programmer? (y/n) ")

while y_or_n != "y" and y_or_n != "n":
    print("Please enter 'y' or 'n'.")
    y_or_n = input("C'mon, tell me...are you a programmer? (y/n) ")

if y_or_n == "y":
    print("Darn right, you are!")
elif y_or_n == "n":
    print("You're WRONG! You ARE a programmer!")
```

This code uses a _loop_. You may not be surprised to learn that a _loop_ is the way we do something more than once in code. There are a couple of different kinds of loops in Python. This is an example of a `while` loop.

Let's dig in to understand how it works.

```python
while y_or_n != "y" and y_or_n != "n":
    print("Please enter 'y' or 'n'.")
    y_or_n = input("Are you a programmer? (y/n) ")
```

Much like an `if` statement a `while` loop has a _condition_:

```python
y_or_n != "y" and y_or_n != "n"
```

The condition in the `while` loop asks a question. When the answer to the question is `True`, the code below the `while` loop runs. When the answer becomes `False`, the loop ends and the code after the `while` loop runs.

In this case we're asking the question, Is `y_or_n` something other than `"y"` **and also** is `y_or_n` something other than `"n"`?

If the user enters anything other than a `y` or `n`, the loop will run. It will inform the user that they should enter a `y` or `n` and then prompt them to try again.

If, on their next attempt, the user enters a `y` or `n`, then the loop will not run again.

## Run the Code

Reading the code and the explanation above is almost certainly not enough to fully understand what's happening. You should run the code.

1. Create a new Python file and open it in Visual Studio Code.
1. Copy and paste the code into your file. (Yes, it's ok to copy/paste this time!)

    ```python
    y_or_n = input("Are you a programmer? (y/n) ")

    while y_or_n != "y" and y_or_n != "n":
        print("Please enter 'y' or 'n'.")
        y_or_n = input("C'mon, tell me...are you a programmer? (y/n) ")

    if y_or_n == "y":
        print("Darn right, you are!")
    elif y_or_n == "n":
        print("You're WRONG! You ARE a programmer!")
    ```

1. Run the program in your terminal.
    1. When prompted, respond with `maybe`. See what happens.
    1. Next try responding with `yes`.
    1. Finally try responding with `y`.
1. Arrange your screen so that you can see the terminal and the code at the same time. Run the program again. Try to visualize the code running as you use the program.

> **NOTE:** Curiosity may kill the cat, but it really helps the programmer! As you run the code you're writing, don't be afraid to try entering different values as shown here to see what happens.

## What's that `and` all about?

We tried to slip this one by you, but alas, you're just too clever for us. Oh well ... we'll get you next time.

Let's revisit the condition of the `while` loop.

```python
while y_or_n != "y" and y_or_n != "n":
```

The use of the keyword `and` is something you haven't seen, but you may be able to imagine what it does. We use the `and` keyword when we need to ask more than one question in our code. When using an `and`, the left side and the right side must both be `True`.

Here's another example.

```python
if 1 == 1 and 2 == 2:
    print("That's a relief!")
```

In addition to `and` there is also an `or` keyword. When using `or` only one of the two sides must be true. For example.

```python
if 42 == 42 or 0 == 1:
    print("I guess that's close enough.")
```
