from modules.characters import Characters
from modules.ennemi import Ennemi
from modules.personnage import Personnage


def check_life(character: Characters):
    if character.pv < 0:
        print(f"{character.nom} est mort")
        return True


def main():
    personnage = Personnage("Hero", 150, 10, 20)
    ennemi = Ennemi("Gobelin", 150, 10, 20)

    while True:
        personnage.attaquer(ennemi)
        if check_life(ennemi):
            break
        ennemi.attaquer(personnage)
        if check_life(personnage):
            break


main()
