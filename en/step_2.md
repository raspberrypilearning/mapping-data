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

**Test:** Print your loaded data out, to check it. Think about how you will need to break each line up to get the region name and the numbers you want.

--- /task ---

--- task ---

Create a global empty list. You will fill this list with dictionaries of information on each region.

--- collapse ---
---
title: Lists in Python
---

A Python list can hold a collection of data. You can create a list using square brackets `[]`:

```python
my_list = []
```

Items can be added to a list as it is created. You can do this by putting them inside the `[]` and separating the items with commas:

```python
pets = ['cat', 'dog', 'rabbit']
```

Items can also be added to lists after they have been created, using `append()`. For example:

```python
pets = ['cat', 'dog', 'rabbit']
pets.append('bird')
```

Would create a `pets` list that looked like this:

```python
['cat', 'dog', 'rabbit', 'bird']
```


--- /collapse ---

--- /task ---

--- task ---

For each region, create a dictionary


--- collapse ---
---
title: Split a text string
---


--- /collapse ---


--- collapse ---
---
title: Create a dictionary
---




--- /collapse ---

--- /task ---

--- task ---

 **Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- /task ---

--- save ---
