#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten
from random import randint

regio_lijst = []
kleuren = {}


def preload():
    global kaart
    kaart = load_image('tech_map.jpg')


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(991, 768)
    laad_gegevens('happy.csv')

    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    teken_gegevens()


def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print(feiten['naam'])
        print(feiten['ranking geluk'])
    else:
        print('Regio niet gedetecteerd')


def laad_gegevens(file_name):
    with open(file_name) as f:
        for line in f:
            # print(line)
            info = line.split(',')
            regio_dict = {
                'naam': info[0],
                'ranking geluk': int(info[1]),
                'geluksscore': float(info[2])
            }
            # print(regio_dict)
            regio_lijst.append(regio_dict)


def teken_speld(x, y, kleur):
    no_stroke()
    fill(kleur)
    ellipse(x, y, 10, 10)


def teken_gegevens():
    rood_waarde = 255
    for regio in regio_lijst:
        regio_naam = regio['naam'] # Haal de naam op van de regio
        # Gebruik de naam om coördinaten te krijgen
        regio_coordinaten = haal_regio_coordinaten(regio_naam)
        regio_x = regio_coordinaten['x'] # Haal de x-coördinaat op
        regio_y = regio_coordinaten['y'] # Haal de y-coördinaat op
        regio_kleur = Color(rood_waarde, 100, 0) # Stel de speldkleur in
        kleuren[regio_kleur.hex] = regio
        teken_speld(regio_x, regio_y, regio_kleur)
        rood_waarde -= 1


run()
