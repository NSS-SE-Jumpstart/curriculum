# Strings to Integers

When you prompt the user using `input()`, the value that is returned is always text. This is true whether they type a word or a number. This can be very irritating. In this lesson, we'll talk about how to deal with it.

But first, some context.

## Strings

In code, text data is called a _string_. In Python, we abbreviate that to `str`.

Strings are wrapped in quotes (`""`).

```python
# the 'statement' variable is set to an `str`s value
statement = "I've see some stuff."

# this looks like a number, but because it's in quotes, it's an `str`.
not_a_number = "25"
```

## Integers

An integer is a number that doesn't have a decimal point. In Python we abbreviate "integer" as `int`.

```python
# both of these variables contain `int` values

a_very_good_int = 42
six = 9 - 3
```

## Why does it matter?

### Comparison

The type of a value determines how comparisons and math operations work.

For example, strings are compared alphabetically. The string "a" is less than the string "b". The word "cat" is greater than the word "aardvark".

This alphabetic comparison includes strings that are made up of numeric digits. The string "1" is less than the string "2", but (surprisingly) the string "100" is also less than the string "2".

```python
if "100" < "2":
    print("weird....") # this will be printed
```

When working with integers comparisons work more as you'd expect.

```python
if 100 < 2:
    print("The world has gone crazy")
else:
    print("I feel comforted") # this will be printed
```

### Math

You've already seen that we can concatenate two strings with the plus (`+`) operator. This includes strings that are made up of numeric digits.

```python
not_eight = "4" + "4"
print(not_eight) # will print the string: 44
```

Integer values use plus (`+`) in a more traditional way.

```python
eight = 4 + 4
print(eight) # will print the integer 8
```

> **NOTE:** When printing to the terminal, it is impossible for the user to determine if a value is a string or an integer, because the quote marks are removed from strings. This makes a numeric string look just like a number. This is part of the reason programmers make the big bucks.

## What can be done to save us!?!?

If you need to get a number from the user, you must first get a string and then convert it to an integer using the `int()` function.

```python
str_age = input("How old are you? ")
age = int(str_age)
if age > 100:
    print("Are you a vampire?")
```

Notice the second line. That's where the magic is.

```python
age = int(str_age)
```

> **NOTE:** I wonder what would happen if the user typed the phrase "nonya business" instead of their age? Maybe you should try it out?

