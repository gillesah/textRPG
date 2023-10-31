from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage


def main():
    personnage = Personnage("Hero", 150, 10, 20)
    print(personnage)
    ennemi = Ennemi("Gobelin", 150, 10, 20)
    print(ennemi)

    while True:
        personnage.attaquer(ennemi)
        personnage.search_object()
        print(personnage.inventaire["potion"])
        if ennemi.check_life():
            break
        ennemi.attaquer(personnage)
        if personnage.check_life():
            break


main()
