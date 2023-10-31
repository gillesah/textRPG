from modules.characters import Characters
import random


class Personnage(Characters):

    def __init__(self, nom: str ) -> None:
        super().__init__(nom)
        self.pv: int = 100 
        self.dega_min: int = 10 
        self.dega_max: int = 20
        self.inventaire = {"potion": 0}
        self.xp = 0
        self.niveau = 1
        
    def __str__(self):
        return f"{super().__str__()} \nVous avez {self.xp} points d'expérience et vous êtes au niveau {self.niveau}.\n"

    def search_object(self) -> None:
        if random.randint(0, 100) > 70:
            self.inventaire["potion"] += 1
            print("Tu as trouvé une potion")
        else:
            print("Tu n'as rien trouvé")
            
    def add_xp(self):
        self.xp += 20
        # augmenter le niveau pour chaque 100pts XP
        if self.xp - self.niveau*100 >= 100:
            self.niveau +=1
            print(f"\nFélicitations vous avez monté au niveau {self.niveau}!\n")
            self.pv += 20
            print(f"\Vous avez gagné 20 points de vie en bonus! Vous avez {self.pv} points de vie.\n")
            
            
    def remove_xp(self):
        self.xp -= 20
        # vérifier si le jouer descendre d'un niveau
        if self.xp < self.niveau * 100: 
            self.niveau -=1
            print(f"\nDommage, vous avez perdu un niveau. _\nVous êtes de retour au niveau {self.niveau}!\n")