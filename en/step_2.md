## Choose a theme

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Do you have an idea of the kind of display you want to create? Use this step to choose and load your data.
</div>
<div>
<mark>Data outputting as a dictionary?</mark>![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open a [the starter project](#){:target="_blank"}. Trinket will open in another browser tab.

[[[working-offline]]]

--- /task ---

--- task ---

Before you can put your data on a map, you'll need to choose some data to display.

**Choose:** There are a number of data files included in the starter project. Read their descriptions below. Then note the name of the file you'd like to use in your display.

--- collapse ---
---
title: Olympic host nations
---

This file, called `olympics.csv` has data on countries that have hosted the Olympic Games. The data includes:

 - The name of the country
 - The number of times they have hosted the games

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- collapse ---
---
title: World population data
---

This file, called `pop.csv`, has data on the populations of different regions in the world. The data includes:

 - How many people live in the region
 - The average age of people in the region
 - How people live in each square kilometre of the region
 - What percentage of people live in cities

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- collapse ---
---
title: Carbon emissions
---

This file, called `carbon.csv`, has data on carbon emissions for each region in a year. The data includes:

 - How much carbon each region emits in total
 - How much carbon each region emits, per-person that lives in that region

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- collapse ---
---
title: Threatened species over time
---

This file, called `species.csv`, has data on the number of plant and animal species that are under threat in each region, across several years. The data includes:

 - The number of threatened plant species
 - The number of threatend vertebrate (animals with a spine) species
 - The number of threatened invertebrate (animals without a spine) species

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- collapse ---
---
title: The wealth of countries
---

The gross domestic product (GDP) of a place is the measures the value, in money, of everything produced there. It can measure how rich an area is. This file, called `gdp.csv`, has data on the of GDP of countries over a year. The data includes:

 - What the total GDP of that country was
 - That total GDP divided by the number of people in the country. This can give you a rough idea of how rich people there are. But remember that everyone doesn't get an equal share.

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- collapse ---
---
title: The happiest places in the world
---

This file, called `happy.csv`, has data from the world happiness report. The report is a survey of the happiness of people in different countries. People were asked to score their happiness on a scale of 0–10. The data includes:

 - The average happiness scrore for a country
 - Where that country ranks in the world for average happiness

Example data: <mark>Example data goes here</mark>

```

```

--- /collapse ---

--- /task ---

--- task ---

Now that you have your data, make a function to load it into a variable.

[[[generic-python-file-read]]]

--- /task ---

--- task ---

**Test:** `print()` your loaded data out, to check it. Think about how you will need to break each line up to get the region name and the numbers you want.

**Tip:** You will be moving data around a lot in the next few steps. It's a good idea to `print()` everything out. This will help you understand what your data looks like at each step. It's also good for catching bugs. You can always comment (with `#`) the `print()` lines out later.

--- /task ---

--- task ---

For each region in the data you have loaded, split that region's line of data into a list.

--- collapse ---
---
title: Split a text string into a list
---

The `split()` function breaks a string into a list. `split(',')` makes a new list item every time it sees a comma. So:

```python
info = 'Estonia,1326535,31,42,68'
my_list = info.split(',')
```

Would put `['Estonia', '1326535', '31', '42', '68']` into `my_list`.

--- /collapse ---

--- /task ---

--- task ---

Use the list you made from each region's data in the file. Create a dictionary for each region. Include the name of the region and the numbers you want to use.

--- collapse ---
---
title: Python dictionaries
---

A dictionary in Python stores pairs of **keys** and **values**.

Both keys and values can be almost any value you can store in Python. Although neither lists nor dictionaries can be keys.

You can use a key to get its connected value.

To make a dictionary you use curly brackets `{}`, with key: value pairs inside. A pair is a key, followed by a colon (`:`), followed by the value connected to that key. For example:

```python
person = {
  'age': 12,
  'height': 149.5,
  'hair': 'brown',
}
```
`age`, `height`, and `hair` are keys. You can use them to look up their values with square brackets `[]`. For example:

```python
print(person['hair'])
```
Will print out the value `brown`.
--- /collapse ---

--- collapse ---
---
title: Converting text to numbers
---

You will need to use a different function to convert text to a number, depending on the kind of number:

 - `int()` is for converting whole numbers
 - `float()` is for converting decimal numbers

To use one of these functions, pass it the text string you want to convert:

```python
text_number = '12345'
converted_number = int(text_number)
```

--- /collapse ---

--- /task ---

--- task ---

Create a global list of regions and add each of the dictionaries to that list. This will let you work with the data in the rest of your program.

--- collapse ---
---
title: Create a list
---

A Python list can hold a collection of data. You can create a list using square brackets `[]`:

```python
my_list = []
```

You can add items to a list as you create it. You can do this by putting them inside the `[]` and separating the items with commas:

```python
pets = ['cat', 'dog', 'rabbit']
```

--- /collapse ---

--- collapse ---
---
title: Add items to a list
---

You can add items to a list as you create it. You can do this by putting them inside the `[]` and separating the items with commas:

```python
pets = ['cat', 'dog', 'rabbit']
```

You also can add items to lists after they have been created, using `append()`. For example:

```python
pets = ['cat', 'dog', 'rabbit']
pets.append('bird')
```

Creates a `pets` list that looks like this:

```python
['cat', 'dog', 'rabbit', 'bird']
```

--- /collapse ---

--- collapse ---
---
title: Get items from a list

---

You can get an item from a list by using its index. An items index is the number of its position in the list, starting from zero.

```python
pets = ['cat', 'dog', 'rabbit']
print(pets[1])
```

Would print out `dog`.

--- /collapse ---

--- /task ---

--- task ---

 **Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- /task ---

--- save ---
