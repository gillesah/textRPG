from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage
from main import pop_ennemi
import time


def main():
    personnage = Personnage("Hero")
    print(personnage)
    ennemi = pop_ennemi()
    print(ennemi)

    while True:
        # attaque / chercher un objet / utiliser un objet
        user_ask = input(
            "que voulez-vous faire : \n A - Attaquer \n B - rechercher un objet \n C - utiliser un objet \n REPONSE :  ").lower()
        if user_ask == "a":
            personnage.attaquer(ennemi)
            if ennemi.check_life():
                personnage.add_xp
                print(f"vous avez {personnage.xp} XP")
                continuer = input(
                    "Voulez-vous continuer à jouer ? (O/N) :  ").lower()
                if continuer == "o":
                    print("changement de l'ennemi")
                    ennemi = pop_ennemi()
                    print(f" Attention, voici {ennemi}")

                    continue
                elif continuer == "n":
                    print("ciao")
                    time.sleep(1)
                    break
                else:
                    print("merci de rentrer quelque chose de valide")

        # l'ennemi attaque juste après

        elif user_ask == "b":
            personnage.search_object()

        else:
            print("merci d'entrer une valeur A, B ou C")
            user_ask = input(
                "que voulez-vous faire : \n A - Attaquer \n B - rechercher un objet \n C - utiliser un objet \n REPONSE :  ").lower()

        time.sleep(1)
        print("Oh non... l'ennemi vous attaque !!!!!! ****")
        ennemi.attaquer(personnage)

        time.sleep(1)
        print("*"*8)
        print(personnage)
        print(ennemi)
        print("*"*8)

        time.sleep(1)
        if personnage.check_life():
            personnage.remove_xp()
            # faire rejouer


main()
