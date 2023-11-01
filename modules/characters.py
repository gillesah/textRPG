from abc import ABC, abstractmethod
import random


class Characters(ABC):
    def __init__(self, nom: str, pv: int, dega_min: int, dega_max: int) -> None:
        self.nom = nom
        self.pv = pv
        self.pv_max = pv
        self.dega_min = dega_min
        self.deg_max = dega_max

    def __str__(self):
        return f"{self.nom} a {self.pv} points de vie restants et {self.nom} peut infliger des dégats jusqu'à {self.deg_max}."

    def attaquer(self, cible):
        """_summary_
        Génére un niveau de dégats aléatoire entre le max et min de l'attaquant et les envlève des points de vie de son cible
        """
        pa = random.randint(cible.dega_min, cible.deg_max)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {pa}")
        cible.pv -= pa

    def check_life(self) -> bool:
        """_summary_
        Vérifie les points de vie de l'instance et affiche un message et return True si l'instance est mort
        """
        if self.pv <= 0:
            print(f"{self.nom} est mort")
            return True
