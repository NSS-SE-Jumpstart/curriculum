# Modifying a List

We can change a list after it's been created. We can add new elements, remove elements, or replace an element.

> **NOTE:** The ability to modify a list is powerful, but it's not as useful as you may think. It turns out it's often better to make a new list instead of changing an existing list.

## Adding an Element

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

## Removing an Element

### `del`

Use the `del` keyword to remove _(aka "delete")_ an element at a particular index.

```python
transportation = ["bus", "car", "plane", "tugboat"]
del transportation[1]

print(transportation) # This will print ['bus', 'plane', 'tugboat']
```

### `remove()`

Use `remove()` to remove an element with a given value. It will remove **only the first** element with that value.

```python
lucky_numbers = [13, 3, 7, 13, 21]
lucky_numbers.remove(13)

print(lucky_numbers) # This will print [3, 7, 13, 21]
```

> **NOTE:** Only the first `13` was removed.

## Replacing an Element

Use the square bracket syntax `[]` to replace a list element.

```python
spice_girls = ["Scary", "Kevin", "Baby", "Ginger", "Posh"]
spice_girls[1] = "Sporty"

print(spice_girls) # This will print ['Scary', 'Sporty', 'Baby', 'Ginger', 'Posh']
```
