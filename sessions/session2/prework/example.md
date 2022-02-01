# Example Code

It's time to see some code in action.

1. Create a new directory called `examples` within your `workspace` directory, and `cd` into it.

    ```txt
    cd ~/workspace
    mkdir examples
    cd examples
    ```

1. Open Visual Studio Code.

    ```txt
    code .
    ```

    > **NOTE:** if you see a message that says "Do you trust the authors of the files in this folder?", click the "Yes, I trust the authors" button.

1. Create a new file using the _File_ -> _New File_ menu option.

1. Copy the following code and paste it into the new file.

    ```python
    # This is a comment
    # Python will ignore this
    # But a human can read it




    ####################################
    # if statement example

    favorite_color = input("What's your favorite color? ")

    if favorite_color == "green":
        print("I like green too")
    elif favorite_color == "red":
        print("Like a fire engine!")
    elif favorite_color == "purple":
        print("You must have royal blood")
    else:
        print("Your favorite color, " + favorite_color + ", does not interest me")




    ####################################
    # print a visual separator

    print() # print a blank line
    print("-------------------")
    print()




    ####################################
    # while loop example

    counter = 0
    while counter < 3:
        print("Cheer!")
        counter = counter + 1




    ####################################
    # print a visual separator

    print()
    print("-------------------")
    print()




    ####################################
    # string to integer example

    str_loop_count = input("How many times should we loop? ")
    loop_count = int(str_loop_count)

    counter = 0
    while counter < loop_count:
        print("LOOP-DA-LOOP")
        counter = counter + 1
    ```

1. Use the _File_ -> _Save_ option to save the new file as `session2_examples.py`.
1. Read through the code. See if you can imagine what it will do when it runs.
1. In your terminal, run the program.

    ```txt
    python3 session2_examples.py
    ```
1. After you answer the questions the program asks and examine the output, spend a few moments comparing the program output with the code. Try to spot which lines of code lead to each printed message.
1. Take a little time to _play_ with the code. Make changes to the code and run it to see what happens. Does it do what you expected? Does it do something surprising? Does it blow up? Lean into that curiosity we mentioned earlier!

## Demo

![Demo](./example.svg)
