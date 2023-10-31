from modules.characters import Characters
import random


class Personnage(Characters):

    def __init__(self, nom: str, pv: int, dega_min: int, dega_max: int) -> None:
        super().__init__(nom, pv, dega_min, dega_max)
        self.inventaire = {"potion": 0}
        self.xp = 0
        self.niveau = 1

    def search_object(self) -> None:
        if random.randint(0, 100) > 70:
            self.inventaire["potion"] += 1
            print("Tu as trouvé une potion")
        else:
            print("Tu n'as rien trouvé")
            
    def add_xp(self):
        self.xp += 20
        #augmenter le niveau pour chaque 100pts XP
        if self.xp / self.niveau >= 100:
            self.niveau +=1
            
