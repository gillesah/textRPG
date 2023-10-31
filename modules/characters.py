from abc import ABC, abstractmethod


class Characters(ABC):
    def __init__(self, nom: str, pv: int) -> None:
        self.nom = nom
        self.pv = pv

    def attaquer(self):
        pass
