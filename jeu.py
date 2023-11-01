from modules.personnage import Personnage
from modules.utils import (
    pop_ennemi,
    continuer,
    show_title,
    declare_defeat,
    declare_victory,
)
import time

ennemi = pop_ennemi()


def jeu():
    show_title()
    nom_personnage = input("Donnez un nom à votre personnage : ")
    personnage = Personnage(nom_personnage)
    print(f"\nBonjour {personnage.nom}!")
    print(personnage.show_XP())
    time.sleep(2.5)
    ennemi = pop_ennemi()
    print(f"{personnage.nom} va affronter\n {ennemi.intro}")
    print(ennemi)
    print("**")
    while True:
        user_ask = input(
            "Que voulez-vous faire : \n A - Attaquer \n B - Rechercher un objet \n C - Utiliser un objet \n REPONSE :  "
        ).lower()
        if user_ask == "a":
            personnage.attaquer(ennemi)
            if ennemi.check_life():
                declare_victory()
                personnage.add_xp()
                ennemi = continuer(personnage)

        # l'ennemi attaque juste après

        elif user_ask == "b":
            personnage.search_object()

        elif user_ask == "c":
            if not personnage.use_potion():
                continue

        else:
            print("Merci d'entrer une valeur A, B ou C")
            user_ask = input(
                "Que voulez-vous faire : \n A - Attaquer \n B - Rechercher un objet \n C - Utiliser un objet \n REPONSE :  "
            ).lower()

        time.sleep(1)
        print("**** Oh non... l'ennemi vous attaque !!!!!! ****")
        ennemi.attaquer(personnage)

        time.sleep(1)
        if personnage.check_life():
            declare_defeat()
            personnage.remove_xp()
            time.sleep(1)
            ennemi = continuer(personnage)
        else:
            print("*" * 8)
            print(personnage)
            print(ennemi)
            print("*" * 8)

        time.sleep(1)


jeu()
