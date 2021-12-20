# Lists

We've talked about a few of Python's data types already - i.e. `str`, `int`, `float`, `bool`. But Python has a much richer system of types than just those four. There's a lot more to explore. In this course, however, we're going to introduce just one more of Python's types: the `list` type.

A `list` in Python is a way to group data together. A single, `list` variable keeps track of several pieces of data in one place instead of needing to use multiple variables.

Imagine we wanted our program to work with the months of the year. We could do something like this:

```python
month1  = "January"
month2  = "February"
month3  = "March"
month4  = "April"
month5  = "May"
month6  = "June"
month7  = "July"
month8  = "August"
month9  = "September"
month10 = "October"
month11 = "November"
month12 = "December"
```

We can _(probably)_ make that work but that's **twelve** different variables to keep track of!

That's where `list`s can help.

```python
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
```

Now we only have one variable, `months`, to keep track of.

## Creating a `list`

In Python code a `list` is a collection of values surrounded by square brackets `[]` with each separated by a comma `,`.

The `months` variable above is an example of creating a `list`. Here are a couple more.

```python
tn_high_temps = [45, 50, 70, 23, 23, 22, 80]
hs_subjects = ["math", "science", "history", "lunch"]
```

## Using a `list`

Ok, so you can store data in a `list`, what do you do with it then? Well, there's quite a lot you can do, but let's start simple. Let's say we'd like to print each element in the list.

> **NOTE:** Although the code below will work to print each element in a `list`, we'll soon show you a better way. The better way requires a new kind of loop, though, and we're not quite ready to introduce it.

```python
index = 0bowling_scores = [9, 8, 1, ]
while index < len(months):
    a_month = months[index]
    print(a_month)

    index = index + 1
```

There's a lot going on in that code. Maybe we should comment it.

```python
# an integer that we'll use to get the "current" month
index = 0 

# Loop as long as the value of index is
#  less than the length of the months list
while index < len(months):

    # get a single month from the months list
    a_month = months[index]
    
    # print the month we got above
    print(a_month)

    # Add 1 to the index so we can get the next month 
    # from the months list when we loop again
    index = index + 1
```

Did those comments help? Maybe a little, but let's dig a little deeper.

### Getting data from a `list`

Each value in a list is referred to as an _element_ of the list. A particular element in a list is accessed by a numeric _index_. This works (almost) the same way as a numbered list of vocabulary words.

For example, consider a few vocabulary words for this course are:

1. Variable
1. Value
1. Loop
1. If statement
1. Source Code

The numbers give you a way to talk about the words. You might say, "I've got 1-3 figured out. I'm shaky on 4. And 5 is a mystery."

The difference between a `list` in Python and a list in every day use is that a Python `list` starts with `0` instead of `1`. Here's the `months` list with each element labeled with its index in a comment.

```python
months = [
    "January",   # 0
    "February",  # 1
    "March",     # 2
    "April",     # 3
    "May",       # 4
    "June",      # 5
    "July",      # 6
    "August",    # 7
    "September", # 8
    "October",   # 9
    "November",  # 10
    "December"   # 11
]
```

> **NOTE:** Python is not alone in having lists start with `0`. It's something almost all programming languages share. By the way, when lists start with `0` it's called _zero origin indexing_. You don't really need to know what it's called, but now you can impress people at parties.

When you want a particular element, you use its index number.

```python
a_month = months[0]        # January
another_month = months[11] # December
```

Of course, you can also use a variable.

```python
num_index = 2
a_month = months[num_index] # March

num_index = num_index + 1
another_month = months[num_index] # April
```

### The length of a `list`

Use the special `len()` function to get the length of a `list`.

```python
length = len(months) # 12
```

Since `list` indexes start at `0`, the length of a `list` is always one more than the index of the last element. In our `months` example, the last element is at index `11`, but the length of the list is `12`.

> **NOTE:** You can also use the `len()` function to get the length of a string.
> ```python
> name = "Genevieve"
> len(name) # 9
> ```

### Back to code

Now that we've covered all that, Let's revisit the month-printing code.

```python
months = [
    "January",   # 0
    "February",  # 1
    "March",     # 2
    "April",     # 3
    "May",       # 4
    "June",      # 5
    "July",      # 6
    "August",    # 7
    "September", # 8
    "October",   # 9
    "November",  # 10
    "December"   # 11
]

# an integer that we'll use to get the "current" month
index = 0 

# Loop as long as the value of index is
#  less than the length of the months list
while index < len(months):

    # get a single month from the months list
    a_month = months[index]
    
    # print the month we got above
    print(a_month)

    # Add 1 to the index so we can get the next month 
    # from the months list when we loop again
    index = index + 1
```

Create a new Python file with the code above. Save the file and run the program. You should see the following output.

```txt
January
February
March
April
May
June
July
August
September
October
November
December
```
