#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten

# Zet de code om eenmalig uit te voeren hier onder


def setup():
    pass


# Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
def mouse_pressed():
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex


run()
