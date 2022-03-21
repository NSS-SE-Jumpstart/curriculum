# Exercise - Morning Routine

In this exercise, you'll write functions that guide the computer on how to do your average morning routine!

This exercise is divided into phases. Make sure you complete one phase at a time, and you **run your program to test it** after you finish each phase.

> **NOTE:** In addition to running your code after each phase, remember you can also run your program before you finish a phase. This can often be useful when debugging errors.

## Phase One

In this first phase you'll get setup by creating and running a simple Python program just to make sure everything is working properly.

1. Create a new Python file called `morning.py`.
1. Open `morning.py` in Visual Studio Code and write code to print `Hello, World!` to the terminal.
1. Run the program to test it.

    ```sh
    python3 morning.py
    ```

## Phase Two

Now that you know you can successfully write and run some Python code, you should remove the code that prints `Hello, World!` and replace it with a function that prints `Hello, World!` and call that function a couple times.

Something a little like this.

```python
def hello():
    print('Hello, World!')

hello()
hello()

```

Save and run the new program. You should run it to see your computer enthusiatically greeting you!

## Phase Three

Before we get very far with this exercise, let's do something that will make our lives a little easier. Let's introduce a function to contain the code in our program.

1. Create a function called `main()` and place those two calls of your hello function inside of it. 
1. Run the code to see what happens. Is it what you expected?

<details>
<summary>  Click here after you've run your program...  </summary>

3. Your code didn't do anything because you didn't call the `main()` function. Add code at the bottom of the `morning.py` file to call `main()`. When you're finished, your script should look like this:

    ```python
    def hello():
        print('Hello, World!')

    def main():
        hello()
        hello()


    main()
    ```

4. Now run your program again to see what happens. Is it what you expected?

> **NOTE:** This is another example of some patterns we saw in the lightning exercise about keeping our code organized.  Feel free to reference that again!

</details>

## Phase Four

Now that we've gotten a good feel on working with functions, let's get into the start of our morning.....waking up. 

1. Add a new function called `wake_up`. It should take no parameters yet, but don't worry we'll get there. The function should, like our hello world function, print `I'm waking up!`  Next, we want to return a string saying `I'm awake now!!`.
Do you see the difference between the print and the return?  The print happens in the function while we're still waking up, but the return is for after the function is finished.....so we've already woken up.

    <details>
    <summary> :sun_behind_small_cloud: Click here to see what your code might look like... :sun_behind_small_cloud: </summary>

    Example `wake_up` function code:

    ```python
    def wake_up():
        # print that we're waking up
        # then `return` that we woke up
    ```
    </details>

1. Let's go through that process one more time with getting out of bed!  Make a function called `get_out_of_bed()` and print that we're getting out of bed while returning that we got out of bed. 

    <details>
    <summary> :sleeping_bed: Another example of what your code might look like... :sleeping_bed: </summary>

    Example `get_out_of_bed` function code:

    ```python
    def get_out_of_bed():
        # print that we're getting out of bed
        # then `return` that we got out of bed
    ```
    </details>

1. Okay.  So now that we've made these functions, lets call them in our `main()` function.  Remember that when we return anything from a function we need to store that return in a variable to be able to use or print it. 

<details>
<summary> Hint: I've written code below to demonstrate what that looks like :) </summary>

Example of returning and using function return:

```python
def hello():
    print('Hello, World!')
    return "I've said hello now it's your turn"

def main():
    our_turn = hello()
    print(our_turn)

main()
```

Do we see whats happening there?  Look really closely!  When we call `hello` our function prints `'Hello, World!'`, but it **returns** a string saying its our turn.  With that return we can store (or "pipeline") that to a variable in main (that I've conveniently named our_turn), and then we can print it!  It's incredibly unseful to return things like this so they can be used whenever needed outside of our functions. 

</details>

Once you've made the changes, run the program to make sure it's working as intended.

## Phase Five

Alright!  So we've worked with functions that don't use parameters, but what about ones that do?

1. Now that we're out of bed, It's time to brush our teeth and eat some breakfast! Write some code in our main function prompting the user for what toothpaste they'll use and what breakfast they'll eat.

1. Perfect!  Now we want to take those variables and use them as parameters for our brushing and breakfast functions.

    Here's some helper code to see what that would look like:

    ```python
    def brush_teeth(toothpaste):
        print("I'm brushing my teeth with " + toothpaste)
        # then `return` that our teeth are clean
    ```

1. Try running your program a couple time with different types of toothpaste and different breakfast foods. 

## Phase Six

Wow we've gotten so much done, but somehow we forgot to get dressed!  Let's make a function that handles that for us. 

Up until now we've only been printing things inside of our functions, but functions can do a lot more work than that!

Write some code **INSIDE** a get_dressed function that prompts the user for what clothes they want to wear, and then prompts them for what shoes they will wear as well.  

Make sure to return a statement saying what you are wearing and print it in `main()`

With that we are ready to face the day!

And you, dear student, are ready to face the next exercise. ;)
