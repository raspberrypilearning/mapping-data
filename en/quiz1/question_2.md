
--- question ---

---
legend: Question 2 of 3
---

You used functions with parameters to load your data and create your map pins. Which of these functions would accept two numbers as parameters, multiply them, and print the result?

--- choices ---

- ( ) 
```python
def my_function():
  a = 5
  b = 3
  result = a * b
  print(result)
```

  --- feedback ---
  Not quite! This function does multiply two numbers, but they're always the same numbers. The parameters let you use the same code on different input.
  --- /feedback ---

- ( ) 
```python
def my_function(a, b):
  print(10)
```

  --- feedback ---
  Not exactly. This function does accept two parameters, but it doesn't use them for anything. The function prints `10` no matter what input it receives.
  --- /feedback ---

- ( ) 
```python
def my_function():
  result = a * b
  print(result)
```

  --- feedback ---
 Close. This function does work with `a` and `b` as though they are parameters. But they're never actually set as parameters to the function.
  --- /feedback ---

- (x) 
```python
def my_function(a, b):
  result = a * b
  print(result)
```

  --- feedback ---
  That's right! This function takes `a` and `b` as parameters, multiplies them, and prints out the result. 
  --- /feedback ---

--- /choices ---

--- /question ---
