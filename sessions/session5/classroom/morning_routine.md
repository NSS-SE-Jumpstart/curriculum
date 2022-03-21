# Exercise - Rolling Dice

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
    #print Hello, World! 

#call hello() a couple times here :)
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
        #print Hello, World! 

    def main():
        hello()
        hello()


    main()
    ```

4. Now run your program again to see what happens. Is it what you expected?

> **NOTE:** It may seem unnecessary to do this, but it's good practice to use functions to organize your code.

</details>

## Phase Four

Now that we've gotten a good feel on working with functions, let's get into the start of our morning.....waking up. 

1. Add a new function called wake_up. It should take no parameters yet, but don't worry we'll get there. The function should, like our hello world function, print `I'm waking up!`  Next, we want to return a string saying `I'm awake now!!`.
Do you see the difference between the print and the return?  The print happens in the function while we're still waking up, but the return is for after the function is finished.....so we've already woken up.

    ```python
    def wake_up():
        # print that we're waking up
        # then `return` that we woke up
    ```

1. Let's go through that process one more time with getting out of bed!

    ```python
    def get_up():
        # print that we're getting up
        # then `return` that we got up
    ```

1. Okay.  So now that we've made these functions, lets call them in our `main()` function.  Remember that when we return anything from a function we need to store that return in a variable to be able to use or print it. 

Once you've made the changes, run the program a few times to make sure it's working.

## Phase Five

Alright!  So we've worked with functions that don't use parameters, but what about ones that do?

Now that we're out of bed, It's time to brush our teeth and eat some breakfast! Write some code in our main function prompting the user for what toothpaste they'll use and what breakfast they'll eat.

Perfect!  Now we want to take those variables and use them as parameters for our brushing and breakfast functions.

Here's some helper code to see what that would look like:

```python
    def brush_teeth(toothpaste):
        # print that we're brushing our teeth with "toothpaste"
        # then `return` that our teeth are clean
```

## Phase Six

Wow we've gotten so much done, but somehow we forgot to get dressed!  Let's make a function that handles that for us. 

Up until now we've only been printing things inside of our functions, but functions can do a lot more work than that!

Write some code **INSIDE** a get_dressed function that prompts the user for what clothes they want to wear, and then prompts them for what shoes they will wear as well.  

Make sure to return a statement saying what you are wearing and print it in `main()`

## Phase Seven

Awesome!  We've gotten a lot done this morning so far!  Sometimes though....we want to change our outfit after we've selected it, and we still have time so let's code for that.

In our `main()` function, let's use a while loop to call the get_dressed function until we decide our outfit is cool enough!

Hint: It'll be similar to that `keep_going` loop we used for the vocab exercise so don't be afraid to go back and check.

## Phase Eight

At this point, we've accomplished quite a bit of our morning, but instead of continuing to make functions for each thing.....let's make one that can handle everything left to do. 

1. Create a function called `morning_routine()`. This function won't take any parameters but we're going to accomplish a lot inside of it. The function should use a `list` of finished morning tasks that will start empty.....but don't worry we'll add to it.

1. Back in our `main()` function, we used a while loop for deciding on if our outfit was cool enough. Now, let's place a similar while loop inside of our `morning_routine()` function that says until we're done getting ready the code inside will run.  What's the code inside?  Well......

1. Inside the while loop write code that prompts the user for a task they completed to get ready.  Then, append that completed task to the list we made above.  After adding the task to our list, check if we have any more tasks to do or if we're ready.

1. Once we're finally ready, we can leave that while loop and return the list of our finished morning tasks.  We're almost done now...... 

## Phase Nine

Alright!  We've accomplished so much this morning and we're ready to face the day head on, but wait...we need to tell everyone about all we've accomplished.  We still have our finished tasks list so let's put that to use.

Before we call our `morning_routine()` in our `main()` function let's print out `"Other things I accomplished this morning:"`

Now below this print we want to list out all of the things we did in our finished tasks list.

Now this is the final step!!  Get ready!

After printing out all of our finished tasks......print `Now I'm ready to face the day!!`

And you, dear student, are ready to face the next exercise. ;)
