from modules.characters import Characters


class Personnage(Characters):

    def __init__(self, nom: str, pv: int, dega_min: int, dega_max: int) -> None:
        super().__init__(nom, pv, dega_min, dega_max)

    def __str__(self) -> str:
        return f"// le {self.nom} a {self.pv} de points de vie"
