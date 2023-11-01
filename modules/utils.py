import random
from modules.ennemi import Ennemi
from modules.personnage import Personnage
import time


def pop_ennemi() -> Ennemi:
    ennemis = [
        {"nom": "Gobelin", "pv": 50, "dega_min": 10, "dega_max": 20},
        {"nom": "Orc", "pv": 75, "dega_min": 10, "dega_max": 20},
        {"nom": "Dragon", "pv": 100, "dega_min": 10, "dega_max": 20},
    ]

    ennemi_number = random.randint(0, len(ennemis) - 1)
    ennemi = Ennemi(
        ennemis[ennemi_number]["nom"],
        ennemis[ennemi_number]["pv"],
        ennemis[ennemi_number]["dega_min"],
        ennemis[ennemi_number]["dega_max"],
    )
    return ennemi


def continuer():
    while True:
        continuer = input("Voulez-vous continuer à jouer ? (O/N) :  ").lower()
        if continuer == "o":
            print("changement de l'ennemi")
            ennemi = pop_ennemi()
            print(f" Attention, voici {ennemi}")
            return "continue"

        elif continuer == "n":
            print("ciao")
            time.sleep(1)
            return "break"
        else:
            print("merci de rentrer quelque chose dAe valide")


def rejouer(personnage):
    while True:
        rejouer = input("Voulez-vous rejouer ? (O/N) :  ").lower()
        if rejouer == "o":
            print("changement de l'ennemi")
            personnage.pv = 100
            personnage.inventaire["potion"] = 0
            ennemi = pop_ennemi()
            print(f" Attention, voici {ennemi}")
            return "continue"

        elif rejouer == "n":
            print("ciao")
            time.sleep(1)
            return "break"
        else:
            print("merci de choisir O (oui) ou N (non)")
