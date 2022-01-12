# Example Code

Here's some example code that uses many of the concepts you've been reading about.

This program creates a shopping list for chicken noodle soup.

```python
ingredients = [
    "onions",
    "carrots",
    "celery",
    "chicken",
    "noodles"
]

quantities = []

print("Let's finalize our shopping list.")
for ingredient in ingredients:
    str_quantity = input("How many " + ingredient + " do you need? ")

    quantity = int(str_quantity)
    quantities.append(quantity)


print("SHOPPING LIST")
for index in range(len(quantities)):
    quantity = quantities[index]
    ingredient = ingredients[index]

    if quantity > 5:
        print(str(quantity) + " " + ingredient + " (BULK ITEM)")
    else:
        print(str(quantity) + " " + ingredient)
```

1. Copy and paste this code into a new Python file and run it.
1. Compare the output to the code. Can you find the line(s) of code that lead to each part of the output?
1. How many elements does the `quantities` list contain?
1. If you were commenting this code, what would you write? Which parts need clarification, and which parts are already clear?

