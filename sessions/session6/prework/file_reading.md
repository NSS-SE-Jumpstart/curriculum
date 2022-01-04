# Reading from a Text File

In this course we've discussed data quite a bit. We store data in variables. We process data in functions. We display data to a user with the `print()` function. We get data from the user with the `input()` function.

When it comes to getting data, we've explored two approaches. The first way is to create it inside a Python source code file.

```python
things_to_avoid = ["snakes", "spiders", "thanksgiving at Uncle Larry's", "assumptions"]
```

Or we might ask the user for it.

```python
first_name = input("What is your first name? ")
```

Each of these approaches work, but they really only work for small amounts of data. Imagine creating a list with 50 or more elements, or pestering the user with even 10 prompts. It's too much.

## Text Files

One, relatively simple, alternative to managing data is to store it in a _text file_.

What is a text file? To be honest it's pretty much what it claims to be. Much like a Python file contains Python code or a MS Word document contains a history paper or an image file contains a photo of you on New Year's Eve, a text file contains...text. Letter, numbers, punctuation...that sort of thing.

Maybe that text is the complete works of William Shakespeare, maybe it's a grocery list, or maybe it's _Rick and Morty_ fan fiction written as an epic poem.

Text files often end in with `.txt`. Like Python files, they can be created and edited using a _text editor_ such as Visual Studio Code. And, also like Python files, they can be managed from within the terminal.

## "Reading" a Text File in Python

Imagine you've got a new book all about the hygiene practices of seventeenth century European peasants. Of course, you yearn to absorb every bit of information contained within the book. Let's think about what needs to happen in order for you to gain that sweet, historical knowledge.

1. You open the book
1. Starting at the beginning you scan your eyes across each character
1. Your brain converts those characters into data
1. Your brain stores that new data inside it's memory
1. You close the book

> **NOTE:** It's possible that the above five step process is a touch over-simplified.

_"Reading"_ a text file in Python works in a similar way.

### An Example

Let's dive into an example.

Let's say we have a text file that contains a list of Nicolas Cage movies with one title per line in the file

[nick_cage_movies.txt](./nick_cage_movies.txt)

And we want to write a Python program to print each of movie titles.

```python
text_file = open("nick_cage_movies.txt")
movies = text_file.
```

## Not the Only Way to Store Data

We'd be remiss if we didn't mention that text files are far from the only way to store data. In fact, though they are used, they aren't even the most common way.

But text files are all we'll cover in this course.
