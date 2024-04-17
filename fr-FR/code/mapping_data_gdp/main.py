#!/bin/python3
from p5 import *
from regions import get_region_coords

liste_regions = []
couleurs = {}


def preload():
    global carte
    carte = load_image('old-map.jpg')  # Remplace par ton image


def dessine_epingle(x, y, couleur):
    fill(couleur)
    ellipse(x, y, 10, 10)  # x, y, largeur, hauteur


def dessine_donnees():

    valeur_rouge = 255  # Définis une valeur de départ pour le rouge

    for region in liste_regions:
        nom_region = region['region']  # Récupère le nom de la région
        # Utilise le nom pour obtenir les coordonnées
        coords_region = get_region_coords(nom_region)
        region_x = coords_region['x']  # Récupère la coordonnée x
        region_y = coords_region['y']  # Récupère la coordonnée y
        # print(nom_region, region_x, region_y)
        couleur_region = Color(valeur_rouge, 0, 0)  # Définis la couleur de l'épingle
        couleurs[couleur_region.hex] = region
        dessine_epingle(region_x, region_y, couleur_region)  # Dessine l'épingle
        valeur_rouge -= 1  # Change la valeur rouge

# Mets le code à exécuter une seule fois ici


def setup():
    size(991, 768)
    charge_donnees('gdp.csv')
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    dessine_epingle(300, 300, Color(255, 0, 0))
    dessine_donnees()


# Place ici le code à exécuter lorsque la souris est cliquée
def mouse_pressed():
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    if couleur_pixel in couleurs:
        faits = couleurs[couleur_pixel]
        print(faits['region'])
        print(faits['pib'])
    else:
        print('Région non détectée')


def charge_donnees(nom_fichier):
    with open(nom_fichier) as f:
        for ligne in f:
            # print(ligne)
            info = ligne.split(',')
            # Modifie le dictionnaire pour qu'il corresponde aux données que tu utilises
            dico_regions = {
                'region': info[0],
                'pib': info[1]
            }
            # print(dico_regions)
            liste_regions.append(dico_regions)
            # print(liste_regions)


run()
