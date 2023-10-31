from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage

import random


def pop_ennemi() -> Ennemi:

    ennemis = [
        {"nom": "Gobelin",
         "pv": 50,
         "dega_min": 10,
         "dega_max": 20},
        {"nom": "Orc",
         "pv": 75,
         "dega_min": 10,
         "dega_max": 20},
        {"nom": "Dragon",
         "pv": 100,
         "dega_min": 10,
         "dega_max": 20},
    ]

    ennemi_number = random.randint(0, len(ennemis)-1)
    ennemi = Ennemi(ennemis[ennemi_number]["nom"], ennemis[ennemi_number]["pv"],
                    ennemis[ennemi_number]["dega_min"], ennemis[ennemi_number]["dega_max"])
    return ennemi


def main():

    personnage = Personnage("Hero")
    print(personnage)

    ennemi = pop_ennemi()
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
