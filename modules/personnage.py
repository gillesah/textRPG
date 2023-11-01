from modules.characters import Characters
import random


class Personnage(Characters):
    """_summary_

    Args:
        Characters (_type_): _description_
    """

    def __init__(self, nom: str) -> None:
        super().__init__(nom, pv=100, dega_min=10, dega_max=20)
        self.inventaire = {"potion": 0}
        self.xp = 0
        self.niveau = 1

    def show_XP(self):
        return f"{super().__str__()} \n{self.nom} a {self.xp} points d'expérience et il est au niveau {self.niveau}.\n"

    # rechercher un objet (potion pour le moment)
    def search_object(self) -> None:
        if random.randint(0, 100) > 50:
            self.inventaire["potion"] += 1
            print(f"{self.nom} a trouvé une potion")
        else:
            print(f"{self.nom} n'a rien trouvé")

    # utiliser une potion

    def use_potion(self):
        if self.inventaire["potion"] >= 1:
            print(f"{self.nom} utilise une potion.")
            self.pv += 20
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.inventaire["potion"] -= 1
            print(f"{self.nom} a maintenant {self.pv} points de vie")
            return True
        else:
            print(f"{self.nom} n'a pas assez de potion... désolé")

    # ajout d'XP si le personnage a gagné

    def add_xp(self):
        self.xp += 20
        # augmenter le niveau pour chaque 100pts XP
        if self.xp - self.niveau * 100 >= 100:
            self.niveau += 1
            print(f"\nFélicitations {self.nom} a monté au niveau {self.niveau}!\n")
            self.pv += 20
            self.pv_max += 20
            print(
                f"{self.nom} a gagné 20 points de vie en bonus! Il a {self.pv} points de vie et peut avoir jusqu'à {self.pv_max} points de vie.\n"
            )

    # suppression d'XP si le personnage perd
    def remove_xp(self):
        self.xp -= 20
        if self.xp < 0:
            self.xp = 0
            print(f"\n{self.nom} a 0 points d'expérience et reste à niveau 1.\n")
            return
        print(
            f"{self.nom} a perdu 20 points d'expérience. Il lui reste {self.xp} points."
        )
        # vérifier si le jouer descendre d'un niveau
        if self.xp < self.niveau * 100 and self.niveau is not 1:
            self.niveau -= 1
            print(
                f"\nDommage, {self.nom} a perdu un niveau. _\n{self.nom} est de retour au niveau {self.niveau}!\n"
            )
