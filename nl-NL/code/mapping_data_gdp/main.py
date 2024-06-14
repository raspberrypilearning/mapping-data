#!/bin/python3
from p5 import *
from regions import haal_regio_coördinaten

regio_lijst = []
kleuren = {}


def preload():
    wereldkaart
    kaart = load_image('old-map.jpg') # Vervang door je afbeelding


def teken_speld(x, y, kleur):
    fill(kleur)
    ellipse(x, y, 10, 10) # x, y, breedte, hoogte


def teken_gegevens():

    rood_waarde =255 #Stel een startwaarde voor rood in

    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam op van de regio
        # Gebruik de naam om coördinaten te krijgen
        regio_coördinaten = haal_regio_coördinaten(regio_naam)
        regio_x = regio_coördinaten['x'] # Haal de x-coördinaat op
        regio_y = regio_coördinaten['y'] # Haal de y-coördinaat op
        # print(regio_naam, regio_x, regio_y)
        regio_kleur = Color(rood_waarde, 0, 0) # Stel de speldkleur in
        kleuren[regio_kleur.hex] = regio
        teken_speld(regio_x, regio_y, region_kleur) # Teken de speld
        rood_waarde -= 1 # Wijzig de roodwaarde

# Zet de code om eenmalig uit te voeren hier onder


def setup():
    size(991, 768)
    load_data ('gdp.csv')
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    teken_speld(300,300, Color(255,0,0))
    teken_gegevens()


# Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
def muis_ingedrukt():
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print(feiten['regio'])
        print(feiten['bbp'])
    else:
        print('Regio niet gedetecteerd')


def laad_gegevens(file_name):
    with open(file_name) as f:
        for line in f:
            # print(line)
            info = line.split(',')
            # Wijzig de dictionary zodat deze overeenkomt met de gegevens die je gebruikt
            regio_dict = {
                'regio': info[0],
                'bbp': info[1]
            }
            # print(regio_dict)
            regio_lijst.append(regio_dict)
            # print(regio_lijst)


run()
