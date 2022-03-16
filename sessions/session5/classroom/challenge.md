# Challenge Exercise

This is an optional challenge exercise that you can try if you have completed the [Dice Exercise](./exercise_dice.md) early. It picks up with what we did togther in the Session 4 [Lightning Exercise](../../session4/classroom/lightning_exercises.md), so you'll want to make a copy of the Python file you wrote for that to use as the starting point for this exercise.

---

You're not going to change anything here. Well actually, you're not going to change _what_ your code is doing, but now that you know what _functions_ are, you're going to create several functions to contain different parts of your ordering system.

> **TIP:** This practice of taking some existing code, and making a lot of changes to it without necessarily changing the functionality is something that's called _refactoring_ and is done quite a bit in the world of software development.

You should take the time to work through each exercise, but if you get stuck or aren't clear what this should look like when you're done there's an outline linked after Exercise 5 that you can take a look at.


## Exercise 1

1. Create a function called `setup_shop()`, and move the the code that defines the variable for and prints the name of the coffee shop into it. This function has no parameters, and does not return anything. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

    > **TIP:** As you work through these first 4 exercises, you'll add the code that calls each function immediately after the function is defined.

    <details>
    <summary><b>Click to see what your code should look like after doing this ...</b></summary>

    ```python
    # define the function:
    def setup_shop():
        # move the code into the function here

    # call the function
    setup_shop()

    # the rest of your code
    ```
    </details>

## Exercise 2

1. Create a function called `get_customer_name()`, and move the code that gets the customers name into it. This function has no parameters, and should return the `customer_name` variable. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.
    > **NOTE:** Since this is returning a variable, make sure you save the returned value in a variable like `the_customer_name` that you can use later on in the code.

## Exercise 3

1. Create a function called `get_drink_menu()`, and move the code to define the variable for and print the list of available drinks into it. This function should return the `drink_menu` list. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.
    > **NOTE:** Since this is returning a variable, make sure you save the returned value in a variable like `the_menu` that you can use later on in the code.

## Exercise 4

1. Create a function called `take_order()`, and move the code that gets the customers order into it. This function should take `drink_menu` and `customer_name` as parameters, and does not return anything. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.
    > **NOTE:** When you call it you'll want to use the variables you created for the returned values in Exercises 2 and 3.

## Exercise 5

*As noted at the first exercise, you've been adding function calls right after the function definition. Now that all of your code is wrapped in function definitions, you can do one last bit of cleanup to make it easier to understand.*

1. Move all of the function calls to the end of the file, after all of the function definitions (making sure they're still called in the same order). Run the code to make sure that it works the same way that it did before you moved all of the function calls.

<details>
<summary><b>Click to see an outline of what the code should look like now ...</b></summary>

```python
def setup_shop():
    # setup_shop code

def get_customer_name():
    # get_customer_name code

def get_drink_menu():
    # get_drink_menu code

def take_order(drink_menu, customer_name):
    # take_order code

setup_shop()
the_customer_name = get_customer_name()
the_menu = get_drink_menu()
take_order(the_menu, the_customer_name)
```
</details>

---

## Final Notes

You may wonder if there's any benefit to having made all of these changes. This is always a great question to consider when refactoring - in this case, aside from getting some practice with writing functions, it should make it easier to quickly understand what the code is doing now. You can quickly look at the 4 function calls at the end of the file and get a sense for what this code does without having to read all of the code. *What other benefits do you think there are to having made these changes?*
