# Searching and Modifying Lists

This topic covers a few advanced features of the Python `list` type. These are't things you'll use every day, but they are important to a fundamental understanding of `list`s.

## Searching a `list`

You can use the `in` keyword to determine whether a list contains a particular element.

```python
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

today = "Tuesday"
if today in week_days:
    print("No laying around today!")
    
if "Saturday" in week_days:
    print("What's happened?!?!")
else:
    print("Ok...all is well.")
```

> **NOTE:** This syntax kinda looks like a `for` loop...but it's not.

To determine if an element is **not** in the list use `not in`.

```python
hated_foods = ["onion", "olive", "cabbage"]
lunch = "hamburger"

if lunch not in hated_foods:
    print("Let's eat")
```

## Modifying a `list`

### `append()`

Use `append()` to add an element to the end of a list.

```python
directions = ["up", "down", "left"]
directions.append("right")

print(directions) # This will print ['up', 'down', 'left', 'right']
```

### `insert()`

Use `insert()` to add a new element at a specific index.

```python
beatles = ["Paul", "George", "Ringo"]
beatles.insert(0, "John")

print(beatles) # This will print ['John', 'Paul', 'George', 'Ringo']
```

> **NOTE:** Remember index values start at `0`

### Changing an Element

Use the square bracket syntax `[]` to change a list element.

```python
spice_girls = ["Scary", "Spotty", "Baby", "Ginger", "Posh"]

spice_girls[1] = "Sporty"
```
