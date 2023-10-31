
from abc import ABC, abstractmethod
import random


class Characters(ABC):
    def __init__(self, nom: str, pv: int, dega_min: int, dega_max: int) -> None:
        self.nom = nom
        self.pv = pv
        self.dega_min = dega_min
        self.deg_max = dega_max

    def attaquer(self, cible):
        pa = random.randint(cible.dega_min, cible.deg_max)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {pa}")
        cible.pv -= pa
        
    def check_life(self):
        if self.pv < 0:
            print(f"{self.nom} est mort")
            return True
