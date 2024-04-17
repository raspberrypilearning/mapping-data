#!/bin/python3
from p5 import *
from regions import get_region_coords
from random import randint

liste_regions = []
couleurs = {}

def preload():
    global carte
    carte = load_image('mercator_bw.png')


# Mets le code à exécuter une seule fois ici
def setup():
    size(991, 768)
    charge_donnees('pop.csv')
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    dessine_epingle(300, 300, Color(255, 0, 0))
    dessine_donnees()


def dessine_epingle(x_coord, y_coord, couleur):
    no_stroke()
    fill(couleur)
    rect(x_coord, y_coord, 10, 10)

def charge_donnees(nom_fichier):
    with open(nom_fichier) as f:
        for ligne in f:
            info = ligne.split(',')
            dico_regions = {
                'region': info[0],
                'population': info[1],
                'densite population': info[2]
            }
            liste_regions.append(dico_regions)

def dessine_donnees():
    valeur_vert = 255
    for region in liste_regions:
        nom_region = region['region']  # Récupère le nom de la région
        region_coords = get_region_coords(nom_region)  # Utilise le nom pour obtenir les coordonnées
        region_x = region_coords['x']  # Récupère la coordonnée x
        region_y = region_coords['y']  # Récupère la coordonnée y
        #print(nom_region, region_x, region_y)
        couleur_region = Color(0, valeur_vert, 0)  # Définis la couleur de l'épingle
        couleurs[couleur_region.hex] = region
        dessine_epingle(region_x, region_y, couleur_region)
        valeur_vert -= 1
    
# Place ici le code à exécuter lorsque la souris est cliquée
def mouse_pressed():
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    
    if couleur_pixel in couleurs:
        faits = couleurs[couleur_pixel]
        print('Nom: ', faits['region'])
        print('Population: ', faits['population'])
        print('Densité de population', faits['densite population'])
    else:
        print('Région non détectée')


run()
