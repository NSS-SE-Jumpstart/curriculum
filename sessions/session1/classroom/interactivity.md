# Interacting with the User

Our `hello_world` program is clearly fantastic. It's amazing. It's unbelievable. Nothing could be more exciting...Right?

OK, OK...It's boring.

A program that just prints messages isn't particularly interesting or useful. Software is meant to be a tool. It's meant to be used. A hammer that's just sitting on a workbench isn't doing anyone any good. A human must pick it up, must interact with it, must pound some nails or threaten some teenagers or _something_...or it's just useless.

Let's write some code that lets a user do something.

> **NOTE:** Whether or not our code will be _useful_ is up for debate, but, hopefully, when we're done, you'll be able to begin to imagine how to use these tools to build something more real.

## Accepting User Input

As we said above most useful programs are interactive. We've already seen how a program might communicate with a user using the `print()` function.

If our program were channeling Groucho Marx, for example...

```python
print("I never forget a face, but in your case I’d be glad to make an exception.")
```

Our programs can also get input from the user.

```python
favorite_golden_girl = input("Who's your favoriteGolden Girl? ")

print("You said your favorite Golden Girl is " + favorite_golden_girl)
```

If you were to run the program it would look something like this:

```txt
$ python3 golden_girls.py 
Who's your favorite Golden Girl? Sophia
You said your favorite Golden Girl is Sophia
```

Let's go ahead and create this program.

1. Create a new `goldengirls` folder in your `workspace` folder.

    ```sh
    cd ~/workspace
    mkdir goldengirls
    cd goldengirls
    ```

1. Create a `golden_girls.py` file.

    In Windows
    ```powershell
    new-item golden_girls.py
    ```

    In macOS
    ```sh
    touch golden_girls.py
    ```

1. Open the `golden_girls.py` file in Visual Studio Code and **type in the code** from above. We know you may be tempted to copy and paste, but for now it's best to type it in.

1. Run the program.

### `input()`

The `input()` function is the counterpart to the `print()` function. `input()` asks the user to enter some information and then waits until they do. We can pass a string of text into the `input()` function that will be displayed to the user. This is often called a _prompt_. In the sample above we're prompting the user to give us the name of a Golden Girl.

```python
input("Who's your favorite Golden Girl? ")
```

Notice the extra space after the question mark. This space will be displayed to the terminal just like the rest of the prompt. It will add some visual buffer between the prompt and the text that the user types. Try removing the space and rerunning your program. It will still work, but it'll be just a bit harder to use.

### Variables

We've seen how a program can get input from a user, but then what? What does it do with the input?

We store it in a _variable_.

Let's think about an analogy. Imagine you go to a restaurant in which you can see the kitchen. You order a grilled cheese sandwich. You watch the cook take some bread, smother it with delicious butter, expertly stack several pieces of cheese, close the sandwich with a gentle press, place the whole thing in a hot skillet, carefully flip it at just the right time, and, then, once it's perfectly cooked - with crispy, browned bread, and cheese melty and gooey and just this side of being too hot to eat - she tosses the whole thing out the window.

You don't want that. Nobody wants that.

What you want is for the cook to put your grilled cheese sandwich on a plate and send it out to you.

```python
favorite_golden_girl = input("Who's your favoriteGolden Girl? ")
```

In the code above `favorite_golden_girl` acts like a plate for your grilled cheese sandwich. It is a _variable_. A variable is a container for data. It has a _name_ and a _value_. In this case the name is `favorite_golden_girl` and the value is whatever the user typed into the terminal.

That last point about the _value_ of `favorite_golden_girl` is important. You, the programmer, cannot see the value of the variable. You know it's something, but not exactly what it is.

We can use the variable without knowing its value.

```python
print("You said your favorite Golden Girl is " + favorite_golden_girl)
```

The code above will always print "You said your favorite Golden Girl is ", but what it prints next is whatever the user typed in. It could be anything. If the user typed in "Dorothy", the message "You said your favorite Golden Girl is Dorothy" would be printed. If the user typed in "a badger with a top hat", the message "You said your favorite Golden Girl is a badger with a top hat" would be printed.

### String Concatenation

Let's take another look at the printing part of our code.

```python
print("You said your favorite Golden Girl is " + favorite_golden_girl)
```

You'll notice that we use the plus (`+`) sign to join the text to the variable. This is a way to join the two together.

It's kinda like adding two numbers. If you join 2 and 2, you get 4. If you join "Monkey" and "Butler", you get "MonkeyButler'.

In code we use the term _"string"_ to refer to text data and when we write code to join to strings together, we use the exceedingly fancy term, _"concatenation"_.

We can concatenate as many strings as we want.

```python
"All the Golden Girls are great, but " + favorite_golden_girl + " is definitely the best!"
```

## Exercise - Mad Libs

It's practice time.

> **NOTE:** This is the first of many practice exercises you'll encounter throughout the course. In general, when working on practice exercises we'll open the Zoom breakout rooms so that you can move into smaller "rooms" to work. Some students find working solo be more natural whereas others prefer working with classmates. Whichever you prefer, we **strongly encourage** you to do some of each. In the real world, software developers spend lots of time doing heads-down, individual work, but generally **more** time working directly with other developers.

You're going to make a [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs) game! Mad Libs that prompts a user to enter words of a particular part of speech and uses those words to complete a small (funny?) story.

1. Create a new directory within your `workspace` directory, and a Python file for the exercise. Remember to name things in such a way that you'll know what they are in a few weeks.

1. To start things off, write the code to print a the message, "Welcome to Mad Libs!" followed by a blank line.

1. Run the program and confirm that the message is displayed.

    > **NOTE:** This _iterative_ technique - write a little code, run it to check the output, then repeat - is the way all software is created. You should **always** write as little code as possible before you run it.

1. Let's start the story with a main character. Prompt the user to enter a main character's name and then display the following message with the main character's name filling in the blank.

    > _____ went to the store.

    Make sure to test your code by running the program before moving on to the next step.

1. Next, prompt the user to enter the type of store and update your printed story to display the type of store.

    > _____ went to the _____ store.

1. Next, make the main character more interesting by giving them something to love. Prompt the user to enter a noun that the main character loves and update the printed story accordingly.

    > _____, the _____-lover, went to the _____ store.

1. Continue adding new inputs and updating the printed text in your code until you have a complete story. If you're feeling particularly creative, you can write your own story, otherwise, you can use the story below.

    > <u>main_character</u>, the <u>lovable-thing</u>-lover, went to the <u>store_type</u> store to buy a <u>purchase</u>. However, before reaching the <u>store_type</u> store, <u>main_character</u> encountered a large <u>threatening_creature</u> that threatened to <u>harm_verb</u> the world with a <u>harm_noun</u>. Fortunately, <u>main_character</u> defeated the large <u>threatening_creature</u> with a <u>defense_adjective</u> <u>defense_noun</u>.

    > **NOTE:** In the above story, we've labeled each blank to (hopefully) make things more clear. Also, note that some of the labels are used more than once. For example <u>main_character</u> is used three times.
