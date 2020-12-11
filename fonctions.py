# -*-coding:Latin-1 -*
from random import choice

liste_mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

def choix():
    a=choice(liste_mots)
    return a

def afficherMot(motHasard,liste):
    motAffiche = ""
    for i in motHasard:
        if i in liste:
            motAffiche += i
        else:
            motAffiche += "*"
    return motAffiche