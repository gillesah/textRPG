from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage

import random


def pop_ennemi():
    ennemi_number = random.randint(0, 2)
    return ennemi_number


def main():

    ennemis = [
        {"nom": "Gobelin",
         "pv": 150,
         "dega_min": 10,
         "dega_max": 20},
        {"nom": "Orc",
         "pv": 150,
         "dega_min": 10,
         "dega_max": 20},
        {"nom": "Dragon",
         "pv": 150,
         "dega_min": 10,
         "dega_max": 20},
    ]

    personnage = Personnage("Hero", 150, 10, 20)
    print(personnage)

    ennemi_number = pop_ennemi()
    ennemi = Ennemi(ennemis[ennemi_number]["nom"], ennemis[ennemi_number]["pv"],
                    ennemis[ennemi_number]["dega_min"], ennemis[ennemi_number]["dega_max"])
    print(ennemi)

    while True:
        # attaque / chercher un objet / utiliser un objet
        personnage.attaquer(ennemi)
        personnage.search_object()
        print(personnage.inventaire["potion"])
        if ennemi.check_life():
            break
        ennemi.attaquer(personnage)
        if personnage.check_life():
            break


main()
