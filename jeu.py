from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage


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
            print(f"{personnage.name} a attaqué {ennemi.name} !")
            print(ennemi)

            if ennemi.check_life():
                print(f"{ennemi.name} est mort ! Vous avez gagné !")
                break

            ennemi.attaquer(personnage)
            print(f"{ennemi.name} a attaqué {personnage.name} !")
            print(personnage)
            if personnage.check_life():
                print(f"{personnage.name} est mort ! Vous avez perdu !")
                break


main()
