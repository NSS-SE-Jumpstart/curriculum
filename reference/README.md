# Reference

This document contains brief descriptions and examples of topics covered in the course.

## Builtin Functions

These are just a few of the functions that Python provides.

### `print()`

Display text or data to the terminal. `print()` can be used to display all data types covered in this course,  `str`, `int`, `float`, `bool`, and `list` _(and more that we didn't cover)_.

#### Example

```python
cat = "Fluffy"
print("The cat is called " + cat)
```

### `input()`

Get text input from the user. `input()` takes an optional "prompt" parameter that displays a message to the user before accepting their input.

`input()` always produces a `str`. If you want to get a number you'll need to convert it.

#### Example

```python
str_num = input("What's 2 + 2? ")
num = int(str_num)
if num == 4:
    print("You got it!")
```

### `len()`

Returns the length of a `list` or `str`.

#### Example

```python
numbers = [4, 5, 6]
numbers_length = len(lst) # 3

message = "Good times are nice"
message_length = len(message) # 19
```

### `range()`

Produces a collection of numbers. In the simplest case, the "range" of numbers begins with zero and goes to the value of the parameter minus one.

`range()` is often used to make a `for` loop iterate a certain number of times.

#### Example

```python
for i in range(5):
    print(i)
```

The above code will print:

```txt
0
1
2
3
4
```

### `open()`

Opens a text file so that it's contents can be read into a Python program.

#### Example

Imagine you have a file called `enemies_list.txt` that looks like this:

```txt
Vinnie
Jan
The lunch lady from middle school
Ted
```

The following code would read the file into a Python `list` and print it.

```python
file = open("enemies_list.txt")
enemies = file.read().splitlines()

for e in enemies:
    print(e)

file.close()
```

---

## Command Line

See [Terminal](#terminal).

---

## Data Types

A data type defines a set of legal values and operations.

_You know what? Honestly, it's a confusing concept and best described by way of examples. Here are some examples_

### `bool`

A Boolean type. `bool`s are either `True` or `False`. They are often used in `if` statements and `while` loops.

#### Example

```python
is_the_sky_blue = True

if is_the_sky_blue:
    print("We must be on Earth!")
```

### `float`

A number that includes a decimal point. The name `float` is a weird, archaic reference that, frankly, should be replaced.

#### Example

```python
GPA = 3.5

if GPA > 3.0:
    print("Pizza Party!")
else:
    print("Study Party...yay...woo...studying.......")
```

### `int`

An integer type. A number without a decimal. `int`s may be positive, negative or zero.

#### Example

```python
the_answer = 42
half_the_answer = the_answer / 2
one_more_than_the_answer = the_answer + 1

temp = -10
if temp < 0:
    print("It's much to cold. It should be less cold. Who do I see about that?")
```

### `list`

A collection type. A list contains zero or more elements. Each element is at a particular index. Index values start at zero. A list has a length.

#### Example

```python
empty_list = []
```

### `str`

Text data between quotes (`"`).

#### Example

```python
language = "Python"
```

---

## Functions

Functions are named containers of code that can accept input data _(parameters)_ and can output data with the `return` keyword.

### Defining Functions

Functions are defined with the `def` keyword followed by the function name, the parameter list and the _body_ of the function.

#### Example

This function adds two numbers and returns the result.

```python
def add(num1, num2):
    result = num1 + num2
    return result
```

* The _name_ of the function is `add`
* The _parameters_ are `num1` and `num2`
* the _body_ of the function is `result = num1 + num2`
* The _return value_ is `result`

### Calling Functions

A function is called by using it's name followed by parentheses. If the function accepts parameters, they should be passed in between the parentheses.

#### Example

Here are a few examples of calling the `add()` function defined above.

```python
res1 = add(3, 3)

num = 7
res2 = add(num, num)

res3 = add(1, num)

res4 = add(num, 33)
```

---

## If Statement

Used to _conditionally execute_ code.

`if` statements are optionally followed by `elif` and/or `else` blocks.

An `if` statement checks a condition in order to determine what code to run. When the condition is `True`, the code immediately below the `if` runs. When the condition is `False`, the code immediately below the `if` will not run but code in an `else` block will run.

The _conditions_ of an `if` often use comparison and logical [operators](#operators).

#### Example

```python
age = get_age() # call a made-up function

if age >= 18 and age <= 45:
    print("Advertisers care about you.")
elif age > 60:
    print("Politicians care about you.")
else:
    print("I still care about you.")
```

---

## Loops

Loops execute code zero or more times. Python has two kinds of loops.

### `for`

Used to _iterate_ over each element in a collection, such as a list or string, and perform an action for each element.

```python
turtles = ["Leonardo", "Raphael", "Donatello",  "Michelangelo"]

for turtle in turtles:
    print(turtle + " likes pizza")
```

### `while`

Loops until a condition is `False`.

`while` loops can be useful for ensuring a user has entered valid data.

#### Example

```python
yes_or_no = input("Do you like cheese")

while yes_or_no != "yes" and yes_or_no != "no":
    yes_or_no = input("Do you like cheese")
    
if yes_or_no == "yes":
    print("Cheese is so good!")
else:
    print("I have nothing to say to you")
```

---

## `None`

A special value that means "there's nothing here". `None` is often used in situations where you may or may not have a value.

Although there are cases when `None` is appropriate value to use, many times it is an error for a variable to be `None`.

#### Example

Calling `len()` on `None` is an error.

```python
not_a_list = None
len(not_a_list)
```

This will produce an error that looks something like this

```txt
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    len(not_a_list)
TypeError: object of type 'NoneType' has no len()
```

---

## Operators

Operators are special symbols or words for doing variable assignment, math, making comparisons, negating booleans or logically joining expressions.

### Assignment Operator

The `=` is used to assign a value to a variable. The variable is on the left and the value is on the right.

#### Example

The `name` variable is assigned the string `"Wilma"`.

```python
name = "Wilma" 
```

### Math Operators

| Operator | Definition                                  |
| -------- | ------------------------------------------- |
| `+`      | Add two numbers or join two strings         |
| `-`      | Subtract two numbers                        |
| `*`      | Multiply two numbers                        |
| `\`      | Divide two numbers                          |
| `\\`     | Divide two integers                         |
| `%`      | Divide two numbers and return the remainder |

### Comparison Operators

| Operator | Definition               |
| -------- | ------------------------ |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |
| `==`     | Is equal                 |
| `~=`     | Is not equal             |

### Logical Operators

| Operator | Definition                                     |
| -------- | ---------------------------------------------- |
| `and`    | Are both sides `True`                          |
| `or`     | Is at least one side `True`                    |
| `not`    | Turn `True` to `False`. Turn `False` to `True` |

---

## Python

A popular programming language. Python programs are written in Python code, saved in files ending in `.py` and are executed with the `python3` command.

---

## Terminal

A text-based interface for interacting with a computer.

Also called _(too many things)_:

* Command Line Interface (the abbreviation CLI is often used as well)
* Command Prompt
* Shell
* Console

---

## Value

Refers to the _real_ data used in a program. Values have types and can be stored in variables.

#### Example

The concept of a _value_ is best understood by example. Each of these are values in Python.

```python
999
78.3
"Fido ate a bone"
False
["a", "b", "c", "d"]
```

---

## Variable

Named containers of data. Variables are used to store values to be used within your Python program.

A variable is assigned a value and can then be used as if it were the value.

#### Example

These two code snippets are equivalent.

```python
four = 1 + 3
```

```python
one = 1
three = 3
four = one + three
```

---

## Visual Studio Code

A popular text editor created by Microsoft. It can be used to edit source code in several programming languages or plain text files.

Visual Studio Code is often referred to as an _integrated development environment_ or IDE.

---
