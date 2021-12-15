# Code as Communication

Writing _readable code_ is important concept in software development. You should strive to write code in such a way that another programmer can easily understand it. After all, code, like other forms of writing, is a means of communication. Code is unique in that it should effectively communicate with a computer, but it should also effectively communicate with a human reader.

> **NOTE:** Remember that "human reader" may very well be you in the future.

## Meaningful Variable Names

Which of these snippets is more readable?

```python
x = input("What's your favorite dog breed? ")
y = "You like " + x + "!"
print(y)
```

or

```python
favorite_breed = input("What's your favorite dog breed? ")
favorite_breed_announcement = "You like " + favorite_breed + "!"
print(favorite_breed_announcement)
```

The second snippet is (at least, a little) more readable because it uses _meaningful_ variable names. Names that convey the type of data storied within the variables.

The above example is, admittedly, pretty trivial, but as your programs get larger and larger, we promise you'll find it **very** important to choose good names for your variables.

## Comments

Sometimes names aren't quite enough to adequately describe what the code is doing. At times like that programmers tern to writing _comments_.

A comment is a bit of text written within source code that is only meant for a human reader. The computer completely ignores comments.

In Python a comment starts with a hash (`#`) character.

```python
# This is a comment
# The computer will ignore this, but you can read it

# Add a couple of numbers and save the result in a variable
four = 2 + 2

print("2 + 2 is " + four) # display the result of the addition
```

### How many comments should you use?

When are comments helpful and when do they detract from readability?

This is a longstanding debate, but, particularly for beginners, the general advice is to err on the side of writing more comments. It's easy to understand code immediately after you've written it, but a day or two (or thirty) later you will have forgotten a lot. You'll thank your past self for leaving informative comments behind.

### "Commenting Out"

Comments can also be used to temporarily remove code without deleting it. It may be hard to imagine now, but this is a very useful feature of comments. You'll make heavy use of it.

Using a comment to remove code is called _"commenting out"_ the code. It's one of those terms that seems odd when you first hear it, but over time will seem perfectly natural.

In the following example the second `print()` function is commented out.

```python
name = input("What's your name? ")
print("Your name is " + name + ", but, really, what's in a name?")
# print("A rose by any other name would smell as sweet")
```
