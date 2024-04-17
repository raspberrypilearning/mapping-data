#!/bin/python3
from p5 import *
from regions import get_region_coords

liste_regions = []
couleurs = {}


def preload():
    global carte
    carte = load_image('mercator_bw.png')

# Mets le code à exécuter une seule fois ici


def setup():
    size(991, 768)
    charge_donnees('carbon.csv')
    print(liste_regions)
    image(
        carte,  # L'image à dessiner
        0,  # Le x du coin supérieur gauche
        0,  # Le y du coin supérieur gauche
        width,  # La largeur de l'image
        height  # La hauteur de l'image
    )
    dessine_donnees()


def dessine_epingle(x, y, couleur):
    no_stroke()
    fill(couleur)
    triangle(x-10, y-5, x, y+10, x+10, y-5)
    triangle(x-10, y+5, x, y-10, x+10, y+5)


def dessine_donnees():
    valeur_rouge = 255  # Définis une valeur de départ pour le rouge
    valeur_bleu = 0
    valeur_vert = 255
    for region in liste_regions:
        nom_region = region['region']  # Récupère le nom de la région
        # Utilise le nom pour obtenir les coordonnées
        region_coords = get_region_coords(nom_region)
        region_x = region_coords['x']  # Récupère la coordonnée x
        region_y = region_coords['y']  # Récupère la coordonnée y
        # print(nom_region, region_x, region_y)
        # Utilise la valeur rouge dans la couleur
        couleur_region = Color(valeur_rouge, valeur_vert, valeur_bleu)
        couleurs[couleur_region.hex] = region
        dessine_epingle(region_x, region_y, couleur_region)  # Dessine l'épingle
        valeur_rouge -= 1  # Change la valeur rouge
        valeur_vert += 1  # Changer la valeur verte
        valeur_bleu -= 1  # Change la valeur bleue


# Place ici le code à exécuter lorsque la souris est cliquée
def mouse_pressed():
    # Place ici le code à exécuter lorsque la souris est cliquée
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex
    if couleur_pixel in couleurs:
        faits = couleurs[couleur_pixel]
        print(faits['region'])
        print(faits['total carbone'])
        print(faits['carbone par personne'])
    else:
        print('Région non détectée')


def charge_donnees(nom_fichier):
    with open(nom_fichier) as f:
        for ligne in f:
            # print(ligne)
            info = ligne.split(',')
            dico_regions = {
                'region': info[0],
                'total carbone': info[1],
                'carbone par personne': info[2]
            }
            liste_regions.append(dico_regions)


run()
