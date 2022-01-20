# Lightning Exercises

These lightning exercises are centered around taking an order at our favorite coffee shop (again). They use a combination of things we've done in previous exercises, as well as incorporating some features of Python that we've just learned about.

---

We'll be picking up where we left off in the Session 4 [Lightning Exercise](../../session4/classroom/lightning_exercises.md), you'll want to make a copy of the Python file you wrote for that as we continue on here.

We really don't want to change anything thing here. Well actually, we don't want to change _what_ our code is doing here, but now that we've learned what _functions_ are, we want to create several functions and move existing code into them. Other than that we're pretty happy with the functionality that our coffee shop ordering system provides.

## Exercise 1

1. Create a function called `setup_shop()` that contains the code to set and print the name of our shop. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 2

1. Create a function called `get_customer_name()` that contains the code to get and set the customers name. This function should return the `customer_name` variable. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

> **NOTE:** Make sure you capture the value that's returned by this function in a variable that you can use later on in the code.

## Exercise 3

1. Create a function called `get_available_drinks()` that contains the code to set and print the list of available drinks. This function should return the `available_drinks` list. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 4

1. Create a function called `take_order()` that contains the code to get and set the customers order. This function should return the `customer_order` list. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 5

1. Create a function called `print_order()` that takes the `customer_order` list as a parameter, and prints the order summary. Add a call to this function, and run the code to make sure it works the same way that it did before you added the function.

## Exercise 6

>**NOTE:** It's likely that your code is now sprinkled with function definitions and function calls throughout. It might look something like this:
>
>```python
>def one_of_our_new_functions():
>    # code for this function
>one_of_our_new_functions()
>
>def another_new_function():
>    # code for this function
>a_variable = another_new_function()
>
># all of our other functions and function calls
>```
>
> This is fine, but you might be thinking that all of these changes have just resulted in more code without any tangible benefit - and you're not entirely wrong. Let's do one more bit of code shuffling that will hopefully make it a little more obvious what the benefit of all these functions are.

1. Move all of the function calls to the end of the file. You'll want to keep them in the same order that they're being called.  Run the code to make sure that it works the same way that it did before you moved all of the function calls.

At this point your code should look somewhat like this:

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

> **NOTE:** This practice of taking some existing code, and making a lot of changes to it without necessarily changing the functionality is something that's called _refactoring_ and is done quite a bit in the real world.


## Thought Exercises

While we've been pretty happy with our ordering system, you can probably imagine multiple ways in which it could be improved. By moving each section of our code into separate functions, we can now easily add/change functionality in one part without worrying too much about breaking functionality of another part. Here are a few ideas of things that could be improved:

- Unless you've been adding extra `print()` statements along the way (which, kudos if you have!) the output of your code is probably a big run-on stream of text and the baristas are having a hard time making sense of it all. A simple improvement here would be to add a `print()` statement after each function call to help visually space out each section.
- You could standardize/improve how the heading for each section (e.g. shop setup, drink menu, order summary) is printed. Maybe you want them all to look like "## Drink Menu ##" (or use some other punctuation). You _could_ update each of the `print()` statements, or you could add a function like `print_header(message)` that formats the header the way you'd like, and then replace each `print()` statement with a call to that function. In addition to making sure each header is printed the same way, this would also make it easier to update what all of the headers look like by updating that one function.
- Let's say we need to take orders from 2 customers at a time. We could add a few more variables and make a few more function calls to get the name and order of a second customer.
- While our customers likely enjoy not having to pay for their drinks, we should probably start figuring out how much they owe us for their drink order. One way to do this would be to add another function like `compute_price()` that takes the `customer_order` and `available_drinks` variables as parameters, computes the price, and returns the final amount.

> **NOTE:** This list is by no means comprehensive. You likely have other ideas of ways that this could be improved, which is part of the beauty of learning how to write your own software - you can make it do whatever you want it to!