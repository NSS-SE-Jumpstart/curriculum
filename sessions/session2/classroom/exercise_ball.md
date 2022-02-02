# Exercise - Bouncing Ball

In the real world it is very rare to start coding from scratch. In most cases, you'll be given existing code and you'll have to make changes to it. There may be bugs in the code that need to be fixed or the customer may be requesting new features. In either case, you'll have to work with code that someone else wrote. This exercise is your first taste of what it's like to add to existing code.

But first we need to talk about multi-line strings.

## Multi-line Strings

In Python a string is text between opening and closing quotes. For example, `"This is a string"` is a string.

There is one restriction when using quotes to surround text. The text must all be on one line. The following is not value Python code, because it tries to create a string that extends over more than one line.

```python
fears = "snakes
public speaking
heights
the thought that all my friends have been replaced by robots"
```

Fortunately there's a simple solution. If you need s string to extend over multiple lines use _triple quotes_ (`"""`) as in the following example.

```python
fears = """snakes
public speaking
heights
the thought that all my friends have been replaced by robots"""
```

> **NOTE:** The only difference is that we replace each `"` with `"""`.

## The Exercise

Now that we've discussed multi-line strings, let's move onto the exercise.

The code below is a partially working bouncing ball "animation" that runs in the terminal. By "partially working", we mean it has bugs. Your task is to fix it and then to add a feature.

## Setup

1. Create a new Python file called `bouncing_ball.py` and paste the following code into it. Make sure you save the file.

    ```python
    import time # We will cover "import" later in the course

    ############################################################
    # This section contains the "frames" for the animation
    ############################################################

    frame_0 = """
    +---------------------+
    |O                    |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_1 = """
    +---------------------+
    |                     |
    | O                   |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_2 = """
    +---------------------+
    |                     |
    |                     |
    |  O                  |
    |                     |
    |                     |
    +---------------------+
    """

    frame_3 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |   O                 |
    |                     |
    +---------------------+
    """

    frame_4 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |    o                |
    +---------------------+
    """

    frame_5 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |     O               |
    |                     |
    +---------------------+
    """

    frame_6 = """
    +---------------------+
    |                     |
    |                     |
    |      O              |
    |                     |
    |                     |
    +---------------------+
    """

    frame_7 = """
    +---------------------+
    |                     |
    |       O             |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_8 = """
    +---------------------+
    |                     |
    |                     |
    |        O            |
    |                     |
    |                     |
    +---------------------+
    """

    frame_9 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |         O           |
    |                     |
    +---------------------+
    """

    frame_10 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |          o          |
    +---------------------+
    """

    frame_11 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |           O         |
    |                     |
    +---------------------+
    """

    frame_12 = """
    +---------------------+
    |                     |
    |                     |
    |            O        |
    |                     |
    |                     |
    +---------------------+
    """

    frame_13 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |             O       |
    |                     |
    +---------------------+
    """

    frame_14 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |              o      |
    +---------------------+
    """

    frame_15 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |               O     |
    |                     |
    +---------------------+
    """

    frame_16 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                o    |
    +---------------------+
    """

    frame_17 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                  o  |
    +---------------------+
    """

    frame_18 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                   o |
    +---------------------+
    """

    frame_19 = """
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                   _ |
    +---------------------+
    """

    ############################################################
    # This section contains the code to create the animation 
    ############################################################

    print("Follow the bouncing ball...")

    counter = 0
    while counter < 20:
        # This incantation will clear the terminal
        # You should NOT try to understand it... I don't :)
        print("\033[H\033[J")

        if counter == 0:
            print(frame_0)
        elif counter == 1:
            print(frame_1)
        elif counter == 2:
            print(frame_2)
        elif counter == 3:
            print(frame_3)
        elif counter == 4:
            print(frame_4)
        elif 5 == counter:
            print(frame_5)
        elif counter == 6:
            print(frame_6)
        elif counter == 7:
            print(frame_7)
        elif counter == 9:
            print(frame_8)
        elif counter == 9:
            print(frame_9)
        elif counter == 9:
            print(frame_10)
        elif counter == 9:
            print(frame_11)
        elif counter == 12:
            print(frame_12)
        elif counter == 13:
            print(frame_13)
        elif counter == 14:
            print(frame_14)
        elif counter == 15:
            print(frame_15)
        elif counter == 16:
            print(frame_16)
        elif counter == 17:
            print(frame_17)
        elif counter == 18:
            print(frame_18)
        elif counter == 19:
            print(frame_20)

        counter = counter + 1

        # Make the program pause for "x" seconds
        x = 1.1
        time.sleep(x)
    ```

1. Run the code in your terminal.

    ```txt
    python3 bouncing_ball.py
    ```

    Everything should work...until it doesn't.

    ![bouncing ball](./bouncing_ball_broken.svg)

## Bug Fixes

1. The first thing to fix is that nasty error message. The message itself is a bit hard to decipher, but the important part seems to be `name 'frame_20' is not defined`.

    * What does this error mean?
    * Where does `frame_20` appear in the code?
    * Should it be there?

    Fix the code so the error goes away.

1. The next bug is that odd blinking in the middle of the animation.

    * Where should you look to find the code for the middle of the animation?
    * The code clearly needs to be changed, but in what way?

    Fix the code so that the animation is smooth and unblinking.

1. Finally, there's supposed to be a message printed above the animated box. It should say "Follow the bouncing ball...".

    * But there is no such message.
    * Is there code for it?
    * Why isn't it being displayed?

    Fix the code so that the message is displayed and remains visible throughout the animation.

## New Features

1. The customer likes the animation, but it runs kinda slowly. Change the code to speed it up. Use your best judgement as to how fast, but each frame should be displayed for less than a second.

1. Add the ability for the user to decide which frame to start on.

    * Prompt the user to enter a number between `1` and `20`.
    * Subtract `1` from that number.
    * Begin the loop at that number.


## Final Product

After completing this exercise, your output should look something like this:

![bouncing ball final](./bouncing_ball_final.svg)
