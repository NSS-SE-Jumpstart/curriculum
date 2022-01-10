# Looping Over Lists

In the [lists lesson](./lists.md) you learned that we can loop over the elements in a list with a `while` loop like this.

```python
marx_brothers = ["Groucho", "Chico", "Harpo"]
index = 0
while index < len(marx_brothers):
    brother = marx_brothers[index]
    print(brother + " is a Marx Brother.")
    index = index + 1
```

This approach works well enough, Python offers us an easier way, the `for` loop.

## The `for` Loop

Here's an example of using a `for` loop.

```python
marx_brothers = ["Groucho", "Chico", "Harpo"]
for brother in marx_brothers:
    print(brother + " is a Marx Brother.")
```

As you can see the `for` loop makes the code significantly shorter and (arguably) easier to understand.

The code above will loop three times - once for each element in the `marx_brothers` list. At each iteration of the loop, the `brother` variable will be assigned the next element from the list.

So, during the first iteration the `brother` variable will be `"Groucho"`. During the second, it will be `"Groucho"`. Finally, during the third iteration, it will be `"Harpo"`.

When you run the code, it produces this output.

```txt
Groucho is a Marx Brother.
Chico is a Marx Brother.
Harpo is a Marx Brother.
```

## The `range()` Function

There are occasions when we to perform some action a certain number of times. One way we might do this is to create a `list` of numbers and loop over it. For example if we wanted to boisterously print `"Hey, everybody!"` five times, we could do this.

```python
numbers = [0, 1, 2, 3, 4]
for index in numbers:
    print("Hey, everybody!")
```

Or maybe we're feeling Christmas-y.

```python
santa_message = ""
numbers = [0, 1, 2]

for index in numbers:
    message = message + "Ho! "

print(santa_message)
```

This would print.

```txt
Ho! Ho! Ho! 
```

The above examples may be a bit contrived, but it really is true that this sort of thing happens a lot in software. You'll see examples later on.

In fact it happens so often that Python gives us the `range()` function that will generate the collection of numbers for us. The `range()` function will generate a collection of numbers of a given size.

Here's how you can use `range()` to say `"Hey, everybody!"` five times.

```python
for index in range(5):
    print("Hey, everybody!")
```

## Get a `list` Index with `range()` and `len()`

Sometimes, when looping through a list, we need to know the index and the element. You can do that in Python if you combine what you've learned about `range()`, `len()` and accessing individual elements in a list with `[]`.

```python
# A list of the best sci-fi movie titles
best_indie_sci_fi = ["Primer", "Moon", "Coherence", "Under the Skin", "her"]

# Print a header 
print("The top 5 independent sci-fi movies are:")

# get the index of each movie in the list
for movie_index in range(len(best_indie_sci_fi)):
    # get the movie element at the particular index
    movie = best_indie_sci_fi[movie_index]

    # Get the position number (i.e. 1, 2, 3...)
    # And convert it to a string
    movie_position = str(movie_index + 1)

    # Print the movie position and title
    print(movie_position + ". " + movie)
```
