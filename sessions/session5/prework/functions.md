# Functions

In some of the previous lessons, we've used the word _function_ a few times without defining it. An understanding of the word wasn't as important as an understanding of whatever other material we were covering. But now that the lesson is called _"Functions"_ we should probably define the term.

A _function_ is a named container of code. In a sense a function contains code in the same way that a variable contains data. The code in a function can be executed by _calling_ the function.

Python has a LOT of functions built right into the language. We've already seen a handful of them.

```python
print()
input()
len()
range()
str()
int()
```

## Calling a Function

When your write the name of the function followed by parentheses `()`, you are _calling_ the function. For example this code calls the `print()` function.

```python
print("Look, Ma, I'm calling a function!")
```

## Function Parameters

Some functions take in data as input. The data passed into a function are known as the function's _parameters_. Parameters are _passed into_ a function inside the parentheses.

The `len()` function for example, takes a list or a string as a parameter and returns its length.

```python
foods = ["cheese", "bacon", "eggs", "more cheese"]

food_length = len(foods) # get the length of the foods list

print(food_length) # prints the number 4
```

```python
super_power = "invisibility"

power_length = len(super_power) # get the length of the super_power string

print(power_length) # prints the number 13
```

## Function Return Value

The above example illustrates another aspect of functions. A function can _return_ a value. In the code above calling the `len()` function returns the length of the list or string passed into it.

It is common to save the return value of a function in a variable as we've been doing with the `input()` function.

```python
opinion = input("What's more fun: a rollercoaster or a nap?")
```

After the above code runs, the `opinion` variable contains the text that the user typed into the terminal because the `input()` function _returns_ that text and the `=` assigns the text to the `opinion` variable.

## Defining Functions

This is where things get really good. The functions that Python gives us are great, but the real power of programming is writing your own functions. In Python we use the `def` keyword to define a function. Here's an example of a function that discourages someone from talking during a movie.

```python
def no_talking(name):
    print("Hey, " + name + "! I can tell you think what you have to say is important.")
    print("It is not.")
```

Now any time you want to smack down a movie talker you can call the `no_talking()` function.

```python
no_talking("Lloyd")
no_talking("Karen")
no_talking("entire movie audience")
```

Here's another example. This function takes two parameters, adds them together and returns the result.

```python
def add(num1, num2):
    return num1 + num2
```

To call it you would write something like this.

```python
result = add(2, 8) # result will be 10
```
