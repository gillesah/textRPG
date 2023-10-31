from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage

import random


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
