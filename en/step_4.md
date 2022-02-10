## Mark your data

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Display your data on the map, and make it interactive.
</div>
<div>
![A map with many pins. Information appears in the text output for some pins.](images/interaction.gif){:width="300px"}
</div>
</div>

Before you can put pins on the map for each place you have data about, you need to know where those places are. The starter project includes code to give you those locations.

You can use `get_region_coords()` to return a dictionary of the coordinates for a region. For example `get_region_coords('Japan')` will return `{'x': 880.151122422, 'y': 278.639809465}`.

--- task ---

Define a `draw_data()` function to put your data on the map. At first you can just print out the region's name and its `x` and `y` coordinates.

It should loop through your `region_list` and print a line for each region.

--- code ---
---
language: python
filename: main.py — draw_data()
---
def draw_data():
  for region in region_list:
    region_name = region['name'] # Get the name of the region
    region_coords = get_region_coords(region_name) # Use the name to get coordinates
    region_x = region_coords['x'] # Get the x coordinate
    region_y = region_coords['y'] # Get the y coordinate
    print(region_name, region_x, region_y)

--- /code ---

--- /task ---

--- task ---

In your `setup()` function, call `draw_data()` and then run your code to test that it works.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: false
line_number_start: 1
line_highlights: 12
---
def setup():
# Put code to run once here
  size(991, 768)
  map = load_image('map.jpeg') # Replace with your image
  image(
    map, # The image to draw
    0, # The x of the top-left corner
    0, # The y of the top-left corner
    width, # The width of the image
    height # The height of the image
    )
  draw_data()
--- /code ---

--- /task ---

--- task ---

Instead of printing out the name of the region, and its coordinates, you can use your `draw_pin()` function, to place your pins on the map. The code below would colour the pins red (`color(255, 0, 9)`) but you can choose a different colours to use.

--- code ---
---
language: python
filename: main.py — draw_data()
line_numbers: false
line_number_start: 1
line_highlights: 7-9
---
def draw_data():
  for region in region_list:
    region_name = region['name'] # Get the name of the region
    region_coords = get_region_coords(region_name) # Use the name to get coordinates
    region_x = region_coords['x'] # Get the x coordinate
    region_y = region_coords['y'] # Get the y coordinate
    #print(region_name, region_x, region_y)
    region_colour = color(255, 0, 0) # Set the pin colour
    draw_pin(region_x, region_y, region_colour) # Draw the pin

--- /code ---

--- /task ---

--- task ---

**Test:** Run your program. You should see lots of pins pop up on your map! Depending on the data you chose, you might see more or fewer pins than in the image below.

![A black and white map with many red dots on it.](images/map_many_pins.png)

--- /task ---

Next, you need to add some code to let users click on a pin and see some information printed out. To do this, each pin needs to be a different colour, and you need a way to match those colours to the right data.

--- task ---

**Choose:** Every pin needs a unique colour. But there are lots of different ways to make this happen. Here are a few suggestions, but you can create your own.

--- collapse ---
---
title: Change the value of one colour
---
This example changes the value for red each time the code places a pin:

--- code ---
---
language: python
filename: main.py — draw_data()
---
def draw_data():
  red_value = 255 # Set a starting value for red

  for region in region_list:
    region_name = region['name']
    region_coords = get_region_coords(region_name)
    region_x = region_coords['x']
    region_y = region_coords['y']
    region_colour = color(red_value, 0, 0) # Use the red value in the colour
    draw_pin(region_x, region_y, region_colour)
    red_value -= 1 # Change the red value

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Change the value of multiple colours
---
This example changes the red, green and blue values each time the code places a pin:

--- code ---
---
language: python
filename: main.py — draw_data()
---
def draw_data():
  red_value = 255 # Set a starting value for red
  blue_value = 0
  green_value = 255
  for region in region_list:
    region_name = region['name']
    region_coords = get_region_coords(region_name)
    region_x = region_coords['x']
    region_y = region_coords['y']
    region_colour = color(red_value, 0, 0) # Use the red value in the colour
    draw_pin(region_x, region_y, region_colour)
    red_value -= 1 # Change the red value
    green_value += 1 #Change the green value
    blue_value -= 1 #Change the blue value 

--- /code ---


--- /collapse ---

--- collapse ---
---
title: Choose random colours
---

At the top of your code, with your other imports, you will need to import `randint` from the `random` library.

You can then choose a random colour for your region colours, each time around the `for` loop. There is a small chance that two or more colours might end up the same, but it is a very small chance.
--- code ---
---
language: python
filename: main.py — draw_data()
---
from random import randint

def draw_data():
  for region in region_list:
    region_name = region['name']
    region_coords = get_region_coords(region_name)
    region_x = region_coords['x']
    region_y = region_coords['y']
    region_colour = color(randint(0,255), randint(0,255), randint(0,255)) # Select a random colour
    draw_pin(region_x, region_y, region_colour)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Run your program and check that the pins are different colours. If you don't have many pins, it may be hard to tell. In that case, try using bigger changes between each pin.

--- /task ---

Your map has unique pins for each location, but you need to add some code to connect those pins to the information you want to show your users.

--- task ---

To use the pin's colour to look up the information, you need to create a `global` dictionary. Do this at the same time as setting the colours on the pins. Use pin colours as keys and the region dictionaries as values.

--- code ---
---
language: python
filename: main.py — draw_data()
---
def draw_data():
  global colours # Make colours global
  colours = {} # Create an empty colours dictionary
  red_value = 255

  for region in region_list:
    region_name = region['name']
    region_coords = get_region_coords(region_name)
    region_x = region_coords['x']
    region_y = region_coords['y']
    region_colour = color(red_value, 0, 0)
    draw_pin(region_x, region_y, region_colour)
    colours[region_colour] = region # Store the region information with the pin colour as the key
    red_value -= 1
--- /code ---

--- /task ---

Now you have a dictionary to look up. You can add some code to take the colour the user clicked and use it to print information from that dictionary.

--- task ---

In your `mouse_pressed()` function check if `pixel_colour` is in your `colours` dictionary. If it is, print out the interesting information from the dictionary.

Remember that `colours` is a dictionary of dictionaries. You will have to get the dictionary of region information, then get the information from inside that dictionary. For example:

```python
facts = colours(pixel_colour)
print(facts['name'])
```

--- collapse ---
---
title: Python dictionaries
---

A dictionary in Python stores pairs of **keys** and **values**.

Both keys and values can be almost any value you can store in Python. Although lists and dictionaries cannot be keys.

You can use a key to get its connected value.

To make a dictionary, you use curly brackets `{}`, with `key: value` pairs inside. A pair is a key, followed by a colon (`:`), followed by the value connected to that key. For example:

```python
person = {
  'age': 12,
  'height': 149.5,
  'hair': 'brown',
}
```
Here, `age`, `height`, and `hair` are keys. You can use them to look up their values with square brackets `[]`. For example:

```python
print(person['hair'])
```
This will print out the value `brown`.

--- /collapse ---


--- collapse ---
---
title: Check if a key is in a dictionary
---

It's useful to check if a key is in a dictionary. Trying to get the value for a key that doesn't exist causes an error.

You can check if a value is in a dictionary by using `in`:

```python
if thing in my_dictionary:
  # Do something
```

--- /collapse ---

--- /task ---

--- task ---

**Test:** Run your program. Click on a pin and check that your program correctly prints out data about that area.

--- /task ---

--- save ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: My pins do not appear on the map
---

If your pins are not appearing on the map, check that you are calling your `draw_data()` function from your `draw()` function.

--- /collapse ---

--- collapse ---
---
title: I get a message about a 'KeyError'
---

If you get a message about 'KeyError', check that the spelling of your dictionary keys match when you put values in and when you read them out. Whether the letters are UPPER CASE or lower case is important too.

If the error is for the `colours` dictionary, make sure you check the key exists in `colours` before trying to get the value.

--- /collapse ---

--- /task ---
