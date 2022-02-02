---
nav_order: 40
---

# What is code, anyway?

You've heard people talk about "coding", "writing code" and "learning to code". Code, code, _code_. People love to talk about it. People love to sing it's praises. People love to make a big deal about how important it is. But it might seem like they never get around to actually saying _what_ it is.

## So, what is code?

_Code_ is text that a computer understands and obeys. Code is written in a special kind of _language_ called a _programming language_. It's made up of words and symbols (which you might normally think of as punctuation) that are arranged in such a way as to be meaningful.

Code is also known as _source code_ because it is the source of a computer's behavior. We use source code to create _programs_ that run on a computer. This is why the terms "coding" and "programming" are synonyms. A person who's writing code is said to be programming a computer.

> **NOTE:** In fact there are *several* terms used to describe the act of writing code. Here are a few: coding, programming, hacking, software development, and developing. Some people might argue that each term has a subtly different meaning, but in the end they all mean telling a computer what do to.
>
> Unfortunately, you'll find that there are many synonyms and ambiguous terms used throughout the world of coding. This is a fact that may surprise you since the code that we write must be very precise and exact in order to instruct the computer to do what we want. It's as if we have a limited capacity for strict precision - and we have to use all that on the computer - so that we become loose with our language when talking with other humans. Fortunately, humans are much better at handling ambiguity than computers, but it takes some time and patience.

## Our first code example

This is some code written in the Python programming language.

```python
print("What is your favorite ice cream flavor: chocolate, vanilla or strawberry?")

flavor = input()

if flavor == "vanilla":
    print("Hey, vanilla is my favorite ice cream too! We should be friends!")
else:
    print("I guess everyone is entitled to their option.")
```

Take a moment with the code above. Try not to get bogged down in the details, but see if you can get a feel for what it would do if run by a computer.

It's _almost_ English, isn't it? I mean, it's _sort of_ English. Well, it's kinda, _vaguely_ similar to English. Right?

After you've spent some time reading the code, take a few moments and write down what you think it does. Once you've done that click the text below to see a description.

<details markdown="1">
<summary>
<b>Click here to read about the code</b>
</summary>

### Explanation 

The code does the following:

1. It prints a message to the user to ask what their favorite ice cream flavor is.

1. It then waits for the user to type in their favorite ice cream, and "saves" the word they typed into a container called `flavor`.

1. Finally, it checks to see if the flavor the user entered is `"vanilla"`.

   * If the flavor is vanilla, the code prints the message: _"Hey, vanilla is my favorite ice cream too! We should be friends!"_
   * Otherwise, the code prints the message: _"I guess everyone is entitled to their option."_

### Demo

Here's a demonstration of the `favorite_ice_cream` program running. In this demo, the program is run twice.

![Favorite Ice Cream Program](./favorite_ice_cream.svg)

> **NOTE:** Do not worry if none of this makes sense to you. We'll get there.

</details>

## What does code do?

As we said earlier code is used to create programs (often called _applications_ or _apps_) that run on a computer. Every program you use was created with code. From games to word processors to the web browser you're using to read this, as well as thousands and thousands of others ... all written in code. And, moreover, that code was all written by human beings. Human beings just like you.

## Ok, so what is a computer?

This may seem a silly question, but it really isn't. The definition of what is or isn't a computer is becoming less clear all the time. Rather than offer a definition, it's probably more clear to give some examples:

- A laptop
- A desktop
- An Android, iPhone or other smartphone
- A tablet
- A smartwatch
- A modern television or pretty much any piece of modern home theater equipment
- A space probe orbiting Mars
- A refrigerator
- A dancing robot poodle
- A vending machine
- A heads-up display in a car...heck, the entire car

All either are computers or have computers as an essential component.  All are powered by software written in code.

## It's not magic

Computers and the programs that run on them are not magic. We harp on this fact a lot in this course because it's easy to forget. We spend a lot of our lives using software without considering the work that went into it. Without considering the people who's job it is to write the code.

Most people can get away with this lack of consideration. In a way it's a testament to the quality of programmers that it's possible to ignore all the work that they put in and just use the program. But as software engineers we don't have such a luxury. We're gonna have to dig in and understand, so that we can create new programs that will be blindly used by people who will ignore our existence.
