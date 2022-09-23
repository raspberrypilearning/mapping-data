## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**. 

Have fun!

--- question ---

---
legend: Question 1 of 3
---

In this project you stored your data in dictionaries and lists, including a list of dictionaries. If you had this list of dictionaries, which code would you use to `print()` the count of dogs?

```python
pets = [
  {
    'pet': 'cat',
    'count': 9
  },
  {
    'pet': 'dog',
    'count': 4
  },
  {
    'pet': 'rabbit',
    'count': 2
  }
]
```

--- choices ---

- (x) 
```python
dogs = pets[1]
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback ---
  Correct! This will print the count of dogs out.
  --- /feedback ---

- ( )
```python
dogs = pets[2]
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback ---
  Not quite! List indexes start at `0`, not `1`.
  --- /feedback ---

- ( ) 
```python
dogs = pets['dog']
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback ---
  Not exactly, `pets` is a list and numbers, called indexes, are used to select items from a list. 
  --- /feedback ---

- ( ) 
```python
dogs = pets[1]
dogs_count = dogs['pet']
print(dogs_count)
```

  --- feedback ---
  Close! This is the wrong key, but in the right dictionary.
  --- /feedback ---

--- /choices ---

--- /question ---
