from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage
from modules.utils import pop_ennemi, continuer, rejouer
import time

ennemi = pop_ennemi()


def jeu():
    nom_personnage = input("Donnez un nom à votre personnage : ")
    personnage = Personnage(nom_personnage)
    print(f"Bonjour {personnage.nom}!")
    print(personnage)
    print(ennemi)
    print("**")
    while True:
        user_ask = input(
            "Que voulez-vous faire : \n A - Attaquer \n B - rechercher un objet \n C - utiliser un objet \n REPONSE :  "
        ).lower()
        if user_ask == "a":
            personnage.attaquer(ennemi)
            if ennemi.check_life():
                personnage.add_xp()
                print(f"vous avez {personnage.xp} XP")
                continuer()

        # l'ennemi attaque juste après

        elif user_ask == "b":
            personnage.search_object()

        elif user_ask == "c":
            personnage.use_potion()

        else:
            print("merci d'entrer une valeur A, B ou C")
            user_ask = input(
                "que voulez-vous faire : \n A - Attaquer \n B - rechercher un objet \n C - utiliser un objet \n REPONSE :  "
            ).lower()

        time.sleep(1)
        print("Oh non... l'ennemi vous attaque !!!!!! ****")
        ennemi.attaquer(personnage)

        time.sleep(1)
        print("*" * 8)
        print(personnage)
        print(ennemi)
        print("*" * 8)

        time.sleep(1)
        if personnage.check_life():
            personnage.remove_xp()
            time.sleep(1)
            rejouer(personnage)


jeu()
