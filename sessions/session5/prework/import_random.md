# Import a Little Randomness

So far we've seen features of Python: variables, user interactivity, `if` statements, two kinds of loops and functions. These are features all Python code can use at any point without requesting permission.

Some features of Python, however, demand a bit more politeness on the part of the programmer. These features must be requested before the are used. In Python we "request" access to a feature using the `import` keyword.

> **NOTE:** The good news is Python should never decline your request.

## `import random`

The best way to demonstrate this feature of Python is with an example. Say you'd like to write a program that simulates rolling dice. A standard die has six sides, and when rolled, will give a number between `1` and `6`. We can do this in Python as follows:

```python
import random

die_roll = random.randint(1, 6)
print("You rolled: " + str(die_roll))
```

The first line of the program requests access to the `random` features of Python.

```python
import random
```

The next line uses the `random.randint()` function to get a random integer between `1` and `6`, and saves that integer in a variable called `die_roll`.

```python
die_roll = random.randint(1, 6)
```

Finally, the code prints a message to the user informing them of the value of the roll.

```python
print("You rolled: " + str(die_roll))
```

> **NOTE:** There's more than `random.randint()` that we can use when we `import random`. We'll see some more later.

> **NOTE:** Given the fact that (most) computers don't have hands, this is exactly the way a real game would implement a dice roll. Even when there are fancy graphics and multiple players and complex game rules, somewhere in the code, is code just like we wrote above.

## More on `import`

In the code above we import what's known as the `random` _library_. In programming terms, the word _library_ refers to extra functionality that someone else has written for us and made available for us to use.

You can think of it as a library of books. Anyone can go to the library and check out whatever book they want and gain whatever knowledge is in that book. The `import` keyword let's us "check out" the extra functionality.

Python has a LOT of libraries that we can use. There are literally hundreds of them. However, in this course we do not have time to delve too deeply in to very many. We'll mostly be sticking to the `random` library.
