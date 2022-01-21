# Lightning Exercises

These lightning exercises are centered around taking an order at our favorite coffee shop. They use a combination of things we've done in previous exercises, as well as incorporating some features of Python that we've just learned about. After we've worked through all of these, we should have a simple ordering system that gets a customer name, gets 

These lightning exercises continue to build on things we've been learning, and folds in use of _lists_ to create a simple ordering service for our favorite coffee shop.

---

You should create a new Python file for these exercises. Do not overwrite the Python file from the previous lightning exercises.

## Exercise 1

1. Create a new directory within your `workspace` directory, and a Python file for the exercise. Remember to name things in such a way that you'll know what they are in a few weeks.
1. Write some code in the Python file that sets the name of the coffee shop in a variable called `shop_name` and prints a message like "__coffee shop name__ Ordering System".

## Exercise 2

1. Customer service is important at our coffee shop, we need to know who is ordering drinks. Add some code that asks for the customer name and saves it in a variable called `customer_name`. 
1. Using a _while_ loop, write code to force the user to enter something for their name (a blank customer name doesn't do us any good).
> **NOTE:** You can refer back to what you did in the [Session 2 Lightning Exercise](../../session2/classroom/lightning_exercises.md) for a refresher on how you've done this before.
1. Print a message like "Order is for __customer_name__".

## Exercise 3

1. It's time to take an order from our uncaffeinated customer. Print a message that says "Taking Order".
1. Add some code that asks what drink the customer would like to order and saves it in a variable called `drink_order`. 
1. Print a message that says "__customer_name__ has ordered a __drink_order__".

## Exercise 4

1. Whoops - we've let the customer order something without telling them what's on the menu! Let's create a _list_ variable called `drink_menu` with a list of the drinks that we can make. Whether you get creative or keep it simple, make sure there are at least 4 drinks on the menu.
1. We want to display this menu so we can tell the customer what they can order. Print a message that says "Drink Menu". Then using a _for_ loop, iterate over the `drink_menu` list, and print out each drink name.

> **NOTE:** We _could_ add this after the last step, but it'll make more sense to our barista if we show them the menu before they take the customer order. Be sure to add this code in the right spot. 

## Exercise 5

1. Customers are sometimes more creative than our menu planners, if a "half-caff caramel macchiato with extra whip" is not part our `drink_menu`, we shouldn't let a customer order it. Add a _while_ loop that makes sure that `drink_order` is something that's in the `drink_menu` list. 
1. Move the message that prints what the customer ordered (from [Exercise 3](#-exercise-3)) to be after this code.

*Whew - you did it - you deserve a coffee after all that after all that! We'll revisit this code and make a few more changes to it in our next session.*

<details>
<summary>
<b>Click here to see what our coffee shop ordering looks like...</b>
</summary>
<img src="final_example.svg">
</details>

## Exercise 5

1. Our coffee shop might be small, but our customers should be able to order more than one drink at a time. We're going to modify the code from the prior step to enable them to do this. Start by adding an empty _list_ variable called `customer_order` before your `drink_order` in the prior step.
1. Modify the _while_ loop from the prior step so that it continues to loop if the provided `drink_order` _is in_ the `available_drinks` list. Inside the loop, add each `drink_order` to the `customer_order` list using the `append()` function. You should also update the prompt in the `input()` function to indicate that more drinks can be added to the order.
1. To validate that your code is working correctly, replace the message that you printed at the end of the prior step with a message that prints the contents of the `customer_order` list (remember that you'll have to convert it to text). We'll do a better job of printing the order in the next step.

## Exercise 6

1. Time to review what's been ordered and get these drinks brewing! Print a message that says "Order Summary for __customer_name__".
1. How many drinks did this customer order? Fortunately we can easily figure out since we've stored all of their orders in the `customer_order` list. Create a new variable called `number_of_drinks` and set it to the number of drinks in the `customer_order` list using the `len()` function.
1. Print a message that says "Number of Drinks: __number_of_drinks__".
1. Using a `for` loop, iterate over the `customer_order` list and print a message that says "Drink: __drink_order__" for each drink order in the list. _(You can also remove the last `print()` statement from_ ___Exercise 5___ _now that we have a nicer order summary printing.)_

*Whew - you did it - you deserve a coffee after all that after all that! We'll revisit this code and make a few more changes to it in our next session.*