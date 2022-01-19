# Lightning Exercises

These lightning exercises are centered around taking an order at our favorite coffee shop (again). They use a combination of things we've done in previous exercises, as well as incorporating some features of Python that we've just learned about.

---

We'll be picking up where we left off in the Session 4 [Lightning Exercise](../../session4/classroom/lightning_exercises.md), you'll want to make a copy of the Python file you wrote for that as we continue on here.

## Exercise 1

We don't want to change a thing here. Well, we don't want to change _what_ our code is doing here, but we want to create several functions and move existing code into them, but right now we think our coffee shop ordering system is perfect in what it does. For each of these functions, you should just be copying the code from the previous exercise into the function.

1. Create a function called `setup_shop()` that prints the shop name. Call this function, and make sure that the code still works.
1. Create a function called `get_customer_name()` that gets the customers name. This function should return the `customer_name` variable. Call this function, and make sure that the code still works. 
1. Create a function called `get_available_drinks()` that sets and prints the list of available drinks. This function should return the `available_drinks` list. Call this function, and make sure that the code still works. 
1. Create a function called `take_order()` that gets the customers order. This function should return the `customer_order` list. Call this function and make sure that the code still works. 
1. Create a function called `print_order()` that takes the `customer_order` list as a parameter, and prints the order summary. Call this function and make sure that the code works. 

At this point you should have something that looks like this: 

```python
#
# lots of new functions that you've added
#

setup_shop()
customer_name = get_customer_name()
available_drinks = get_available_drinks()
customer_order = take_order(available_drinks)
print_order(customer_name, customer_order)
```

> **NOTE:** This practice of taking some existing code, and making a lot of changes to it is something that's called _Refactoring_ and is done quite a bit in the real world.  If all we wanted to do was add functions, this whole step would have been a bit pointless. Fortunately, we have a lot more that we want to do, and having those functions there will make it a lot easier to do now. 

## Exercise 2

1. Let's cleanup the output so that it's not just a unending stream of text. You can be somewhat creative here, make some changes, run the code, and see if you like the changes you've made. Would the barista using this system be able to easily see what orders the customer has placed? Here are some changes to consider making: 
    - Add some sort of punctuation to each section heading (e.g. "## Drink Menu" or "[ Drink Menu ]" or ":: Drink Menu ::" instead of "Drink Menu"). 
    - Add extra lines between each section (e.g. either an empty line or a short series of dashes like "\-\-\-").
    - Indent lines within a section by adding a few extra spaces to the `print()` statements (e.g. `print("  Drink...")` instead of `print("Drink...")`).

## Exercise 3

1. We want to be paid for our drinks. Add code to do this ... _multiple exercises TODO_
