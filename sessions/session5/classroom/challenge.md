# Challenge Exercise

This is an optional challenge exercise that you can try if you have completed the [Dice Exercise](./exercise_dice.md) early. It continues with what we did in the Session 4 [Lightning Exercise](../../session4/classroom/lightning_exercises.md), so you'll want to make a copy of the Python file you wrote for that to use as the starting point for this exercise.

---

We're not going to change anything here. Well actually, we're not going to change _what_ our code is doing, but now that we know what _functions_ are, we're going to create several functions to contain different parts of our ordering system.

> **TIP:** As you work through the first 4 exercises, add the code that calls each function immediately after the function is defined. We'll clean things up a little in the last exercise.

## Exercise 1

1. Create a function called `setup_shop()` that contains the code to set and print the name of our shop. This function has no parameters, and does not return anything. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 2

1. Create a function called `get_customer_name()` that contains the code to get the customers name. This function has no parameters, and should return the `customer_name` variable. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.
> **NOTE:** Since this is returning a variable, make sure you save the returned value in a variable that you can use later on in the code.

## Exercise 3

1. Create a function called `get_drink_menu()` that contains the code to set and print the list of available drinks. This function should return the `drink_menu` list. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.
> **NOTE:** Since this is returning a variable, make sure you save the returned value in a variable that you can use later on in the code.

## Exercise 4

1. Create a function called `take_order()` that contains the code to get the customers order. This function should take the `drink_menu` and `customer_name` as parameters, and does not return anything. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 5

1. As noted above, now that we have all of our code wrapped in function definitions, we can do one last bit of cleanup. Move all of the function calls to the end of the file, after all of the function definitions (making sure they're still called in the same order). Run the code to make sure that it works the same way that it did before you moved all of the function calls.

```python
def one_of_our_new_functions():
    # code for this function

def another_new_function():
    # code for this function

# all of our other function definitions

one_of_our_new_functions()
a_variable = another_new_function()
# all of our function calls
```
*Your code should be patterned like this now.*

---

### Final Notes

This practice of taking some existing code, and making a lot of changes to it without necessarily changing the functionality is something that's called _refactoring_ and is done quite a bit in the real world.

You may wonder if there's any benefit to having made all of these changes. This is always a great question to consider when refactoring - in this case, aside from getting some practice with writing functions, it should make it easier to quickly understand what the code is doing now. You can quickly look at the 4 function calls at the end of the file and get a sense for what this code does without having to read all of the code. *What other benefits do you think there are to having made these changes?*
