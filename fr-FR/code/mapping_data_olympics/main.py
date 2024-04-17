#!/bin/python3
from p5 import *
from regions import get_region_coords

def charge_donnees(nom_fichier):
    global liste_regions
    liste_regions = []

    with open(nom_fichier) as f:
        for ligne in f:
            #print(ligne)
            info = ligne.split(',')
            # Modifie le dictionnaire pour qu'il corresponde aux données que tu utilises
            dico_regions = {
                'nom': info[0],
                'pays_hote' : int(info[1])
            }
            #print(dico_regions)
            liste_regions.append(dico_regions)


def preload():
    global carte
    carte = load_image('mercator.jpeg')


def dessine_epingle(x, y, couleur, pays_hote):
    no_stroke()
    fill(couleur)
    taille = 7 + 3 * pays_hote
    ellipse(x, y, taille, taille)


def dessine_donnees():
    global couleurs
    couleurs = {}
    valeur_bleu = 255

    for region in liste_regions:
        nom_region = region['nom']
        region_coords = get_region_coords(nom_region)
        region_x = region_coords['x']
        region_y = region_coords['y']
        pays_hote = region['pays_hote']
        couleur_region = Color(0, 0, valeur_bleu)
        dessine_epingle(region_x, region_y, couleur_region, pays_hote)
        couleurs[couleur_region.hex] = region
        valeur_bleu -= 1
  
  
def setup():
    # Mets le code à exécuter une seule fois ici
    size(991, 768)
    charge_donnees('olympics.csv')
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    no_stroke()
    dessine_donnees()

  
def mouse_pressed():
    # Place ici le code à exécuter lorsque la souris est cliquée
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex

    if couleur_pixel in couleurs:
        info = couleurs[couleur_pixel]
        print(info['nom'])
        if info['pays_hote'] == 1:
            print('A hébergé les jeux une seule fois.')
        else:
            print('A hébergé les jeux '+str(info['pays_hote'])+ ' fois.')

run()
