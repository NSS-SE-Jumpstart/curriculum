# Variables, Values and Data Types

You've been using variables for a while now. You know that a variable is a container for data. Every variable has a name and a value.

Here are some variables.

```python
the_answer = 42
name = "Fred Rogers"
good_enough_gpa = 2.1
is_the_moon_real = True
```

The code above creates variables and _assigns_ each variable a value using the _assignment operator_ (`=`). The left side of the `=` is the variable name and the right side is the value.

Simple, right? Well, simple-ish...

## Values

Variables are great. You can't write an "real" program without them. But the variables themselves aren't the interesting thing. It's not the containers that matter, it's what's inside. It's the _values_ that matter.

_Values_ can be a bit of a tricky concept. When we talk about values, we're talking about the actual data. The integer `23` is a value. The string `"Who you lookin' at?"` is a value. The booleans `True` and `False` are values.

Sometimes it can help to get a little philosophical, so let's try that. Let's take _you_ for instance. You have a name. When people praise you and your many accomplishments, they use your name so everyone will know they're taking about. But _you_ are not your _name_.

_You_ are the sum total of all the atoms in your body, of all the thoughts in your mind, and all the memories and experiences of your life. _You_ are hopes and dreams. _You_ are fears and joys and private secrets. _You_ are the real value. Your _name_ is the variable.

## Data Types

In software every value has a _type_. A type is a way to describe what kind of data we're dealing with. In the code snippet below, each variable is of a different type.

```python
the_answer = 42
name = "Fred Rogers"
good_enough_gpa = 2.1
is_the_moon_real = True
```

Here are some commonly used types.

| Type Name | Description                                                            | Examples                |
| --------- | ---------------------------------------------------------------------- | ----------------------- |
| int       | An integer. Integers are numbers that don't have decimal points.       | `42`, `-3`, `0`         |
| float     | A "floating point" number. This is a number with a decimal point.      | `3.14`, `-100.1`, `5.0` |
| str       | A string. Strings are text surrounded by quotes. Strings may be empty. | `"Hello"`, `""`         |
| bool      | A boolean. A boolean can only be `True` or `False`                     | `True`, `False`         |

### Why do types matter?

This is actually a really big and complex question. Don't worry, though, we won't go into all the nitty-gritty details here.

A value's type determines what kinds of things you can do with the value and how different operators work with it.

For example, the plus (`+`) operator works differently between strings and numbers.

```python
2 + 2 # 4
"Pizza " + "Time!" # "Pizza Time!"
```

Certain operations can only be performed on particular types. For example we can use the `len()` function to determine how long a string is.

```python
name = "Ted"
len(name) # 3
```

But it makes no sense to get the length of a number

```python
a_number = 2000

# This will cause this error: 
# TypeError: object of type 'int' has no len()
len(a_number) 
```
