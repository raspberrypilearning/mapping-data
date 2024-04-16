#!/bin/python3
from p5 import *
from regions import get_region_coords

# Mets le code à exécuter une seule fois ici


def setup():
    pass


# Place ici le code à exécuter lorsque la souris est cliquée
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex


run()
