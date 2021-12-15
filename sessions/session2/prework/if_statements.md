# Making Decisions in Code

Up until now you've encountered code that runs sequentially from top to bottom. It flows in the same way that a short story might be read, or the way you might follow instructions for assembling a cabinet.

This sort of sequential code is powerful, but it's not sufficient to do all we need to do. Sometimes we want our code to do one thing in a particular situation and a different thing in another. We want our code to decide how to proceed.

## `if/else`

Here's some code tha makes a decision based on some user input.

```python
best_color = input("What is the best color? ")

if best_color == "green":
    print("Green is the right answer. Good job.")
else:
    print("What? Why didn't you sey 'green'? You need help.")
```

When this code runs, one of two things will happen.

Either this...

```txt
What is the best color? green
Green is the right answer. Good job.
```

Or this...

```txt
What is the best color? hotdog
What? Why didn't you sey 'green'? You need help.
```

The code that runs depends on the value that the user enters. If the user enters `green`, they are praised for their good work. If they enter **anything else**, they are condemned for their poor life choices.

### Conditionals

Take another look at this line. This is where the magic happens.

```python
if best_color == "green":
```

This is an `if` statement. An `if` statement let your code ask a question about some data and make a decision about what to do next.

This code asks the question, _Is the value stored in the `best_color` variable equal to the string `"green"`?_

To ask this question we use the _equality operator_ (`==`). Sometimes known as a "double equals", this operator compares the thing on its left with the thing on its right. If the two things are the same, the `==` says it's `True` that they are equal, otherwise the `==` says it's `False` that they are equal.

```python
best_color == "green" # this may be True or False
```

The code above is called the _condition_ of the `if` statement. When the condition is `True` the code immediately below the `if` runs. When the condition is `False`, the code below the `else` runs.

```python
best_color = input("What is the best color? ")

# Is the best_color variable equal to "green"?
if best_color == "green":
    # True block - when best_color is equal to "green"
    print("Green is the right answer. Good job.")
else:
    # False block - when best_color is not equal to "green"
    print("What? Why didn't you sey 'green'? You need help.")
```

Notice that the code beneath the `if` and the `else` is indented. This is required and very important. You'll see similar code indention throughout Python code.

## `if/elif/else`

Sometimes a simple yes or no decision is not enough. For these situations Python provides us with the `elif` keyword.

```python
the_boss = input("Who's the boss? The cat or the human ")

if the_boss == "cat":
    print("Your honesty is commendable.")
elif the_boss == "human":
    print("Is the cat watching you right now? Are you safe?")
else:
    print("You gotta say 'cat' or 'human'.")
```

You can have as many `elif`s as you need.

```python
the_boss = input("Who's the boss? The cat, the human or the baby ")

if the_boss == "cat":
    print("Your honesty is commendable.")
elif the_boss == "human":
    print("Is the cat watching you right now? Are you safe?")
elif the_boss == "baby":
    print("Even the cat is no match for the baby!")
else:
    print("You gotta say 'cat', 'human' or 'baby'.")
```

## Just an `if`

Finally, Python allows you to have just an `if` without an `else` or `elif`. When you have have only an `if`, the code below it will run when the condition is `True`, but when the condition is `False` nothing happens.

```python
print("Everything's fine")
print("Everything's fine")
print("Everything's fine")

if 1 == 2:
    print("The world has gone crazy!!!!")

print("Everything's fine")
print("Everything's fine")
print("Everything's fine")
```
