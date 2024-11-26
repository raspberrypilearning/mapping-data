#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten
from random import randint

regio_lijst = []
kleuren = {}

def preload():
    global kaart
    kaart = load_image('mercator_bw.png')


# Zet de code om eenmalig uit te voeren hier onder
def setup():
    size(991, 768)
    laad_gegevens('pop.csv')
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    teken_speld(300, 300, Color(255, 0, 0))
    teken_gegevens()


def teken_speld(x_coord, y_coord, kleur):
    no_stroke()
    fill(kleur)
    rect(x_coord, y_coord, 10, 10)

def laad_gegevens(file_name):
    with open(file_name) as f:
        for line in f:
            info = line.split(',')
            regio_dict = {
                'regio': info[0],
                'bevolking': info[1],
                'bevolkingsdichtheid': info[2]
            }
            regio_lijst.append(regio_dict)

def teken_gegevens():
    groen_waarde = 255
    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam op van de regio
        regio_coordinaten = haal_regio_coordinaten(regio_naam) # Gebruik de naam om coördinaten op te halen
        regio_x = regio_coordinaten['x'] # Haal de x-coördinaat op
        regio_y = regio_coordinaten['y'] # Haal de y-coördinaat op
        #print(regio_naam, regio_x, regio_y)
        regio_kleur = Color(0, groen_waarde, 0) # Stel de speldkleur in
        kleuren[regio_kleur.hex] = regio
        teken_speld(regio_x, regio_y, regio_kleur)
        groen_waarde -= 1
    
# Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
def mouse_pressed():
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print('Naam: ', feiten['regio'])
        print('Bevolking: ', feiten['bevolking'])
        print('Bevolkingsdichtheid', feiten['bevolkingsdichtheid'])
    else:
        print('Regio niet gedetecteerd')


run()
