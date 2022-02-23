
# Checkpoint
### Question 1

Which of the following is a way to gain access to the `random` library in Python code?

<details>
<summary>
<b>A. </b>
<code>include random</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>get random</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>gimme random</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>import random</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> 
</details>

### Question 2

What will the following Python code print the terminal?

```python
import random

flip = random.randint(1, 2)
if flip == 1:
    print("heads")
else:
    print("tails")
```

<details>
<summary>
<b>A. </b>
<code>heads</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>tails</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
It won't print anything
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
A random number
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
Either <code>heads</code> or <code>tails</code>, but there is no way to know which one until you run the code
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> 
</details>

The next few questions will refer to the `add()` function defined below:

```python
def add(a, b):
    print(a)

    c = a + b
    return c
```
### Question 3

If you ran the code below what would be printed to the terminal?

```python
result = add(70, 2)
```

<details>
<summary>
<b>A. </b>
<code>a</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>b</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>2</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>70</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The code `print(a)` will print the value of the first parameter passed into the `add()` function. In this case that is `70`.
</details>
<details>
<summary>
<b>E. </b>
<code>72</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>F. </b>
<code>result</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>G. </b>
Nothing would be printed
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>H. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>

### Question 4

What is the value of `result` after the code below is run?

```python
result = add(70, 2)
```

<details>
<summary>
<b>A. </b>
<code>a</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>b</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>2</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>70</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
<code>72</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The `result` variable is set to the value _returned_ by the `add()` function. In this case, that is `70 + 2` which is `72`.
</details>
<details>
<summary>
<b>F. </b>
<code>result</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>G. </b>
It will have no value
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>H. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>

### Question 5

If you ran the code below what would be printed to the terminal?

```python
result = add("bat", "man")
```

<details>
<summary>
<b>A. </b>
<code>a</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>b</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>bat</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The code `print(a)` will print the value of the first parameter passed into the `add()` function. In this case that is `bat`.
</details>
<details>
<summary>
<b>D. </b>
<code>man</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
<code>batman</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>F. </b>
<code>result</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>G. </b>
Nothing would be printed
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>H. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>

### Question 6

What is the value of `result` after the code below is run?

```python
result = add("bat", "man")

```
<details>
<summary>
<b>A. </b>
<code>a</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>b</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>bat</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>man</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
<code>batman</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The `result` variable is set to the value _returned_ by the `add()` function. In this case, that is `"bat" + "man"` which is the string `"batman"`. Note that the quotes (`"`) are not printed.
</details>
<details>
<summary>
<b>F. </b>
<code>result</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>G. </b>
It will have no value
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>H. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>

The next few questions will refer to the `add()` function defined below:

```python
def welcome(name):
    print("Welcome, " + name)


def make_exciting(word):
    return word + "!!!"
```
### Question 7

What would the following code print to the terminal?

```python
make_exciting("Spider")
```

<details>
<summary>
<b>A. </b>
<code>Spider</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>Spider!!!</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>!!!</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>word + !!!</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>E. </b>
Nothing would be printed
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> The `make_exciting()` function _returns_ a value but does **NOT** print anything.
</details>
<details>
<summary>
<b>F. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>

### Question 8


What would the following code print to the terminal?

```python
welcome(make_exciting("Jan"))
```

<details>
<summary>
<b>A. </b>
<code>Jan</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>B. </b>
<code>Jan!!!</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>C. </b>
<code>Welcome, Jan</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>D. </b>
<code>Welcome, Jan!!!</code>
</summary>

&emsp; :heavy_check_mark: **CORRECT**

> This code will first call the `make_exciting()` function with `"Jan"` as a parameter. The `make_exciting()` function will then return `"Jan!!!"`. The value, `"Jan!!!"` is then passed as a parameter into the `welcome()` function where the message `Welcome, Jan!!!` is printed to the terminal.
</details>
<details>
<summary>
<b>E. </b>
<code>word + !!!</code>
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>F. </b>
Nothing would be printed
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
<details>
<summary>
<b>G. </b>
This code would cause an error
</summary>

&emsp; :x: **INCORRECT**

> 
</details>
