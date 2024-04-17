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
                'region': info[0],
                'population': int(info[1]),
                'densite population': float(info[2]),
                'age moyen': float(info[3]),
                'pourcentage urbain': float(info[4])
            }
            #print(dico_regions)
            liste_regions.append(dico_regions)

def dessine_epingle(x, y, couleur):
    no_stroke()
    fill(couleur)
    rect(x, y, 7, 7)


def dessine_donnees():
    global couleurs
    couleurs = {}
    valeur_rouge = 255
    for region in liste_regions:
        if reponse == 'u' and region['pourcentage urbain'] >= 50.0:
            nom_region = region['region']
            coords_region = get_region_coords(nom_region)
            region_x = coords_region['x']
            region_y = coords_region['y']
            couleur_region = Color(valeur_rouge, 255, 0)
            dessine_epingle(region_x, region_y, couleur_region)
            couleurs[couleur_region.hex] = region
            valeur_rouge -= 1
        elif reponse == 'r' and region['pourcentage urbain'] < 50.0:
            nom_region = region['region']
            coords_region = get_region_coords(nom_region)
            region_x = coords_region['x']
            region_y = coords_region['y']
            couleur_region = Color(valeur_rouge, 255, 0)
            dessine_epingle(region_x, region_y, couleur_region)
            couleurs[couleur_region.hex] = region
            valeur_rouge -= 1
  

def preload():
    global carte
    carte = load_image('mercator_bw.png')


def setup():
    # Mets le code à exécuter une seule fois ici
    size(991, 768)
    charge_donnees('pop.csv')
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
        print(info['region'])
        print('Population: ', str(info['population']))
        print('Densité de population: ', str(info['densite population']))
        print('Age moyen: ', str(info['age median']))
        print('Pourcentage urbain: ', str(info['pourcentage urbain']))

reponse = None

while reponse not in ['u', 'r']:
    reponse = input('Veuillez saisir u pour voir les endroits qui sont principalement urbains, ou r pour voir les endroits qui sont principalement ruraux: ')


run()
