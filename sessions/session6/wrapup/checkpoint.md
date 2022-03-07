
# Checkpoint
### Question 1

When do a function's _parameter_ get assigned a _value_?

<details>
<summary>
<b>A. </b>
When the function is defined
</summary>

&emsp; :x: **INCORRECT**

> The names of the parameters are defined when the function is defined, but the values are not.
</details>
<details>
<summary>
<b>B. </b>
After the program ends
</summary>

&emsp; :x: **INCORRECT**

> Nothing has a value after the program ends.
</details>
<details>
<summary>
<b>C. </b>
When the function is called
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> When a function is called the values passed between the parentheses are assigned to the function parameters.
</details>
<details>
<summary>
<b>D. </b>
Function parameters always have a value
</summary>

&emsp; :x: **INCORRECT**

> When defining a function the parameters _stand for_ the values that will eventually be passed in, but they don't have values until the function is called.
</details>

### Question 2

---

In the code below what should the `__________` be replaced with?

```python
import random


def main():
    flip = flip_a_coin()
    print("The coin landed on " + flip)


def flip_a_coin():
    zero_or_one = random.randint(0, 1)
    if zeroe_or_one == 0:
        heads_or_tails = "Heads"
    else:
        heads_or_tails = "Tails"

    __________


main()
```

<details>
<summary>
<b>A. </b>
<code>print(heads_or_tails)</code>
</summary>

&emsp; :x: **INCORRECT**

> Remember _printing_ will display a value to the terminal, but in this case we need to get the value from the `flip_a_coin()` function back into the `main()` functions. Printing won't do that.
</details>
<details>
<summary>
<b>B. </b>
<code>print(flip_a_coin)</code>
</summary>

&emsp; :x: **INCORRECT**

> Remember _printing_ will display a value to the terminal, but in this case we need to get the value from the `flip_a_coin()` function back into the `main()` functions. Printing won't do that.
</details>
<details>
<summary>
<b>C. </b>
<code>input(heads_or_tails)</code>
</summary>

&emsp; :x: **INCORRECT**

> `input(heads_or_tails)` would prompt the user for information, but this function is is using `random.randint()` to get information.
</details>
<details>
<summary>
<b>D. </b>
<code>return heads_or_tails</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The `main()` function is trying to get information from the `flip_a_coin()` function. The way this happens is that the `flip_a_coin()` must `return` it and the `main()` function must receive it by assigning it to the `flip` variable.
</details>

### Question 3

---

What would the following code print to the terminal?

```python
def main():
    z_fun()
    print("is")
    x_fun()


def x_fun():
    y_fun()
    print("snake")


def y_fun():
    print("a")


def z_fun():
    y_fun()
    print("python")

main()

```

<details>
<summary>
<b>A. </b>
These words with one per line: <code>is</code> <code>a</code> <code>python</code> <code>a</code> <code>snake</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
These words with one per line: <code>a</code> <code>python</code> <code>is</code> <code>a</code> <code>snake</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
These words with one per line: <code>a</code> <code>snake</code> <code>a</code> <code>python</code> <code>is</code> 
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
These words with one per line: <code>is</code> <code>snake</code> <code>a</code> <code>python</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
It won't print anything
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
