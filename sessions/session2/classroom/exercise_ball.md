# Exercise - Bouncing Ball

In the real world it is very rare to start coding from scratch. In most cases, you'll be given existing code and you'll have to make changes to it. There may be bugs in the code that need to be fixed or the customer my be requesting new features. In either case, you'll have to work with code that someone else wrote. This exercise is your first taste of what it's like to add to existing code.

The code below is a partially working bouncing ball "animation" that runs in the terminal. Your task is to fix it and then to add a feature.

## Setup

1. Create a new Python file called `bouncing_ball.py` and paste the following code into it. Make sure you save the file.

    ```python
    import time # We will cover "import" later in the course

    ############################################################
    # This section contains the "frames" for the animation
    ############################################################

    frame_0 = r"""
    +---------------------+
    |O                    |
    |                     |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_1 = r"""
    +---------------------+
    |                     |
    | O                   |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_2 = r"""
    +---------------------+
    |                     |
    |                     |
    |  O                  |
    |                     |
    |                     |
    +---------------------+
    """

    frame_3 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |   O                 |
    |                     |
    +---------------------+
    """

    frame_4 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |    o                |
    +---------------------+
    """

    frame_5 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |     O               |
    |                     |
    +---------------------+
    """

    frame_6 = r"""
    +---------------------+
    |                     |
    |                     |
    |      O              |
    |                     |
    |                     |
    +---------------------+
    """

    frame_7 = r"""
    +---------------------+
    |                     |
    |       O             |
    |                     |
    |                     |
    |                     |
    +---------------------+
    """

    frame_8 = r"""
    +---------------------+
    |                     |
    |                     |
    |        O            |
    |                     |
    |                     |
    +---------------------+
    """

    frame_9 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |         O           |
    |                     |
    +---------------------+
    """

    frame_10 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |          o          |
    +---------------------+
    """

    frame_11 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |           O         |
    |                     |
    +---------------------+
    """

    frame_12 = r"""
    +---------------------+
    |                     |
    |                     |
    |            O        |
    |                     |
    |                     |
    +---------------------+
    """

    frame_13 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |             O       |
    |                     |
    +---------------------+
    """

    frame_14 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |              o      |
    +---------------------+
    """

    frame_15 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |               O     |
    |                     |
    +---------------------+
    """

    frame_16 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                o    |
    +---------------------+
    """

    frame_17 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                  o  |
    +---------------------+
    """

    frame_18 = r"""
    +---------------------+
    |                     |
    |                     |
    |                     |
    |                     |
    |                   o |
    +---------------------+
    """

    frame_19 = r"""
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
