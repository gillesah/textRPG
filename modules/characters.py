
from abc import ABC, abstractmethod
import random


class Characters(ABC):
    def __init__(self, nom: str, pv: int, dega_min: int, dega_max: int) -> None:
        self.nom = nom
        self.pv = pv
        self.dega_min = dega_min
        self.deg_max = dega_max

    def attaquer(self, character):
        pa = random.randint(character.dega_min, character.deg_max)
        print(f"{self.nom} attaque {character.nom} et lui inflige {pa}")
        character.pv -= pa
