#!/bin/python3
from p5 import *
from regions import get_region_coords
from random import randint

liste_regions = []
couleurs = {}


def preload():
    global carte
    carte = load_image('tech_map.jpg')


def setup():
    # Mets le code à exécuter une seule fois ici
    size(991, 768)
    charge_donnees('happy.csv')

    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    dessine_donnees()


def mouse_pressed():
    # Place ici le code à exécuter lorsque la souris est cliquée
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    if couleur_pixel in couleurs:
        faits = couleurs[couleur_pixel]
        print(faits['nom'])
        print(faits['rang du bonheur'])
    else:
        print('Région non détectée')


def charge_donnees(nom_fichier):
    with open(nom_fichier) as f:
        for ligne in f:
            # print(ligne)
            info = ligne.split(',')
            dico_regions = {
                'nom': info[0],
                'rang du bonheur': int(info[1]),
                'score du bonheur': float(info[2])
            }
            # print(dico_regions)
            liste_regions.append(dico_regions)


def dessine_epingle(x, y, couleur):
    no_stroke()
    fill(couleur)
    ellipse(x, y, 10, 10)


def dessine_donnees():
    valeur_rouge = 255
    for region in liste_regions:
        nom_region = region['nom']  # Récupère le nom de la région
        # Utilise le nom pour obtenir les coordonnées
        coords_region = get_region_coords(nom_region)
        region_x = coords_region['x']  # Récupère la coordonnée x
        region_y = coords_region['y']  # Récupère la coordonnée y
        couleur_region = Color(valeur_rouge, 100, 0)  # Définis la couleur de l'épingle
        couleurs[couleur_region.hex] = region
        dessine_epingle(region_x, region_y, couleur_region)
        valeur_rouge -= 1


run()
