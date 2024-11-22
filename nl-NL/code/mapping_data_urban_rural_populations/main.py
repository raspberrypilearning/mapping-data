#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten

def laad_gegevens(file_name):
    global regio_lijst
    regio_lijst = []

    with open(file_name) as f:
        for line in f:
            #print(line)
            info = line.split(',')
            # Wijzig de dictionary zodat deze overeenkomt met de gegevens die je gebruikt
            regio_dict = {
                'regio': info[0],
                'bevolking': int(info[1]),
                'bevolkingsdichtheid': float(info[2]),
                'gemiddelde leeftijd': float(info[3]),
                'percentage stedelijk': float(info[4])
            }
            #print(regio_dict)
            regio_lijst.append(regio_dict)

def teken_speld(x, y, kleur):
    no_stroke()
    fill(kleur)
    rect(x, y, 7, 7)


def teken_gegevens():
    global kleuren
    kleuren = {}
    rood_waarde = 255
    for regio in regio_lijst:
        if answer == 'u' and regio['percentage stedelijk'] >= 50.0:
            regio_naam = regio['regio']
            regio_coordinaten = haal_regio_coordinaten(regio_naam)
            regio_x = regio_coordinaten['x']
            regio_y = regio_coordinaten['y']
            regio_kleur = Color(rood_waarde, 255, 0)
            teken_speld(regio_x, regio_y, regio_kleur)
            kleuren[regio_kleur.hex] = regio
            rood_waarde -= 1
        elif answer == 'r' and regio['percentage stedelijk'] < 50.0:
            regio_naam = regio['regio']
            regio_coordinaten = haal_regio_coordinaten(regio_naam)
            regio_x = regio_coordinaten['x']
            regio_y = regio_coordinaten['y']
            regio_kleur = Color(rood_waarde, 255, 0)
            teken_speld(regio_x, regio_y, regio_kleur)
            kleuren[regio_kleur.hex] = regio
            rood_waarde -= 1
  

def preload():
    global kaart
    kaart = load_image('mercator_bw.png')


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(991, 768)
    laad_gegevens('pop.csv')
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    no_stroke()
    teken_gegevens()
  
  
def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex

    if pixel_kleur in kleuren:
        info = kleuren[pixel_kleur]
        print(info['regio'])
        print('Bevolking: ', str(info['bevolking']))
        print('Bevolkingsdichtheid: ', str(info['bevolkingsdichtheid']))
        print('Gemiddelde leeftijd: ', str(info['gemiddelde leeftijd']))
        print('Percentage stedelijk: ', str(info['percentage stedelijk']))

answer = None

while answer not in ['u', 'r']:
    answer = input('Voer u in om plaatsen te zien die voornamelijk stedelijk zijn, of r om plaatsen te zien die voornamelijk landelijk zijn: ')


run()
