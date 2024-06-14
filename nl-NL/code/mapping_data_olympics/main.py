#!/bin/python3
from p5 import *
from regions import haal_regio_coördinaten

def laad_gegevens(file_name):
    global regio_lijst
    regio_lijst = []

    with open(file_name) as f:
        for line in f:
            #print(line)
            info = line.split(',')
            # Wijzig de dictionary zodat deze overeenkomt met de gegevens die je gebruikt
            regio_dict = {
                'naam': info[0],
                'organisator_aantal': int(info[1])
            }
            #print(regio_dict)
            regio_lijst.append(regio_dict)


def preload():
    wereldkaart
    kaart = load_image('mercator.jpeg')


def teken_speld(x, y, kleur, organisator_aantal):
    no_stroke()
    fill(kleur)
    grootte = 7 + 3 * organisator_aantal
    ellipse(x, y, grootte, grootte)


def teken_gegevens():
    wereld kleuren
    kleuren = {}
    blauw_waarde = 255

    for regio in regio_lijst:
        regionaam = regio['naam']
        regio_coördinaten = haal_regio_coördinaten(regio_naam)
        regio_x = regio_coördinaten['x']
        regio_y = regio_coördinaten['y']
        organisator_aantal = regio['organisator_aantal']
        regio_kleur = Color(0, 0, blauw_waarde)
        teken_speld(regio_x, regio_y, regio_kleur, organisator_aantal)
        kleuren[regio_kleur.hex] = regio
        blauw_waarde -= 1
  
  
def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(991, 768)
    load_data ('olympics.csv')
    image(
        kaart, # De afbeelding om te tekenen
        0, # De x van de linkerbovenhoek
        0, # De y van de linker bovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    no_stroke()
    teken_gegevens()

  
def muis_ingedrukt():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex

    if pixel_kleur in kleuren:
        info = kleuren[pixel_kleur]
        print(info['regio'])
        if info['organisator_aantal'] == 1:
            print('Heeft de Spelen één keer georganiseerd.')
        else:
            print('Heeft de games '+str(info['organisator_aantal'])+ ' keer georganiseerd.')

run()
