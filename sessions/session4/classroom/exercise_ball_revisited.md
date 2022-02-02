# Exercise - Bouncing Ball Revisited

Now that you have lists in your toolbox, let's revisit the [bouncing ball](../../session2/classroom/exercise_ball.md) exercise. You may find the code to be much simpler.

## Discussion

When we say the code can be made "simple", it means it can become easier for an _experienced programmer_ to understand.

Unfortunately, we won't be able to make the creation of the individual frames _that_ much simpler, but at least we can make it a little shorter by using a list instead of using individual variables.

Because there are no blank lines between each frame, the code below is a little shorter than the code in the original exercise, but since each frame takes several lines of text, there's only so much we can do.

However the loop that prints each frame can be made much simpler. That'll be your task.

```python
frames = [
"""
+---------------------+
|O                    |
|                     |
|                     |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
| O                   |
|                     |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|  O                  |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|   O                 |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|    o                |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|     O               |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|      O              |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|       O             |
|                     |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|        O            |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|         O           |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|          o          |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|           O         |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|            O        |
|                     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|             O       |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|              o      |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|               O     |
|                     |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                o    |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                  o  |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                   o |
+---------------------+
""",
"""
+---------------------+
|                     |
|                     |
|                     |
|                     |
|                   _ |
+---------------------+
"""
]
```

## The Exercise

1. Create a new Python file called `bouncing_ball_revisited.py` and copy the code above into it?
1. Add code to loop over the `frames` list and display each frame.

    * You should include the `print()` code that clears the screen.
    * Also include the `sleep` code. Make sure you add the `input time` line to the top of the Python file.
    * Add code to print `Follow the bouncing ball...again` with each iteration of the loop.
    * You should **NOT** add code to prompt the user for which frame to start with.

