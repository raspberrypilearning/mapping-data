#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten

regio_lijst = []
kleuren = {}


def preload():
    global kaart
    kaart = load_image('mercator_bw.png')

# Zet de code om eenmalig uit te voeren hier onder


def setup():
    size(991, 768)
    laad_gegevens('carbon.csv')
    print(regio_lijst)
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    teken_gegevens()


def teken_speld(x, y, kleur):
    no_stroke()
    fill(kleur)
    triangle(x-10, y-5, x, y+10, x+10, y-5)
    triangle(x-10, y+5, x, y-10, x+10, y+5)


def teken_gegevens():
    rood_waarde =255 # Stel een startwaarde voor rood in
    blauw_waarde = 0
    groen_waarde = 255
    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam op van de regio
        # Gebruik de naam om coördinaten te krijgen
        regio_coordinaten = haal_regio_coordinaten(regio_naam)
        regio_x = regio_coordinaten['x'] # Haal de x-coördinaat op
        regio_y = regio_coordinaten['y'] # Haal de y-coördinaat op
        # print(regio_naam, regio_x, regio_y)
        # Gebruik de rood waarde in de kleur
        regio_kleur = Color(rood_waarde, groen_waarde, blauw_waarde)
        kleuren[regio_kleur.hex] = regio
        teken_speld(regio_x, regio_y, regio_kleur) # Teken de speld
        rood_waarde -= 1 # Wijzig de roodwaarde
        groen_waarde += 1 # De groenwaarde wijzigen
        blauw_waarde -=1 #De blauwwaarde wijzigen


# Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print(feiten['regio'])
        print(feiten['totale koolstof'])
        print(feiten['koolstof per persoon'])
    else:
        print('Regio niet gedetecteerd')


def laad_gegevens(file_name):
    with open(file_name) as f:
        for line in f:
            # print(line)
            info = line.split(',')
            regio_dict = {
                'regio': info[0],
                'totale koolstof': info[1],
                'koolstof per persoon': info[2]
            }
            regio_lijst.append(regio_dict)


run()
