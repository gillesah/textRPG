from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage
import time


def main():
    personnage = Personnage("Hero", 150, 10, 20)
    print(personnage)
    ennemi = Ennemi("Gobelin", 150, 10, 20)
    print(ennemi)

    while True:
        # attaque / chercher un objet / utiliser un objet
        user_ask = input(
            "que voulez-vous faire : \n A - Attaquer \n B - rechercher un objet \n C - utiliser un objet \n REPONSE :  ").lower()
        if user_ask == "a":
            personnage.attaquer(ennemi)
            time.sleep(3)

            print("Oh non... l'ennemi vous attaque !!!!!! ***************************")
            ennemi.attaquer(personnage)

        elif user_ask == "b":
            personnage.search_object()
            print("Oh non... l'ennemi vous attaque !!!!!!")
            ennemi.attaquer(personnage)

        time.sleep(3)


main()
