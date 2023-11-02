from modules.characters import Characters
import random


class Personnage(Characters):
    """_summary_
    Classe pour le personnage controlée par l'utilisateur
    Enfant de la classe Characters
    """

    def __init__(self, nom: str) -> None:
        super().__init__(nom, pv=100, dega_min=10, dega_max=20)
        self.inventaire = {"potion": 0, "epee": 0}
        self.xp = 0  # points d'expérience
        self.niveau = 1

    def show_XP(self):
        """Afficher les points d'expérience et le niveau"""
        return f"{super().__str__()} \n{self.nom} a {self.xp} points d'expérience et il est au niveau {self.niveau}.\n"

    # rechercher un objet (potion ou épée pour le moment)
    def search_object(self) -> None:
        """
        Un int aléatoire est utiliser pour donner 50% de chance à trouver un objet.
        Si l'int entre 50 et 99 est pair, une potion est trouvée. Si l'int entre 50 et 99 est impair, une épée est trouvée.
        Tout objet trouvé est ajouté à l'inventaire de le personnage et la résultat est affichée.
        """
        random_chance = random.randint(0, 100)
        if random_chance >= 50 and random_chance % 2 == 0:
            self.inventaire["potion"] += 1
            print(f"{self.nom} a trouvé une potion")
            print(
                f"""
                     °
                    °                  
                    ===
                    |°|
                    |~|
                   (___)
                  
                  """
            )
        elif random_chance >= 50:
            self.inventaire["epee"] += 1
            print(f"{self.nom} a trouvé une épée")
            print(
                f"""
                    ()
                  __)(__
                  '-<>-'
                    )(  
                    ||  
                    || 
                    ||
                    ||
                    || 
                    ||  
                    ||
                    ||  
                    \/
                  
                  """
            )
        else:
            print(f"{self.nom} n'a rien trouvé")

    # choisir une potion à utiliser

    def choose_object(self) -> str:
        """_summary_
        Affiche l'inventaire de le personnage et lui demande de choisir entre une potione et une épee.
        Return:
            La fonctionne retourne un string de l'objet choixi par le joueur
        """
        print(
            f"\nVous avez {self.inventaire['potion']} potions et {self.inventaire['epee']} épees.\n"
        )
        object = input(
            "Quel objet voulez-vous utiliser ?\n A - Potion\n B - Épée\nREPONSE : "
        ).lower()
        if object == "a":
            return "potion"
        elif object == "b":
            return "epee"
        else:
            print("Merci d'entrer une valeur A ou B\n")
            return self.choose_object()

    # utiliser l'objet choisi

    def use_object(self, object: str, ennemi) -> bool:
        """_summary_


        Args:
            object (str): l'objet choixi (potion ou epee)
            ennemi (str, optional): un objet ennemi est nécessaire pour utiliser
            l'épée qui réduit les PV de l'énnemi.

        Returns:
            _type_: bool True si l'objet est utilisé et Faux si le personnage n'en a pas assez
        """
        if self.inventaire[object] >= 1:
            print(f"{self.nom} utilise une {object}.")
            self.inventaire[object] -= 1
        else:
            print(f"{self.nom} n'a pas assez de potion... désolé")
            return False  # à tester si c'est ok
        if object == "potion":
            self.pv += 20
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            print(f"{self.nom} a maintenant {self.pv} points de vie")
            return True
        elif object == "epee":
            print(
                f"\n{ennemi.nom} perd 15 points de vie avant que {self.nom} l'attaque.\n"
            )
            ennemi.pv -= 15
            self.attaquer(ennemi)
            return True

    # ajout d'XP si le personnage a gagné

    def add_xp(self):
        """_summary_
        Augmente les points d'expérience quand le personnage gagne. Le nivea est également augmenté chaque fois que le personnage
        dépasse les 100 points et les points de vie maximale augmente avec le niveau.
        """
        self.xp += 20
        print(f"Vous avez {self.xp} XP")

        # augmenter le niveau pour chaque 100pts XP
        if self.xp - self.niveau * 100 >= 0:
            self.niveau += 1
            print(
                """
     __ _                               
  /\ \ (_)_   _____  __ _ _   _     _   
 /  \/ / \ \ / / _ \/ _` | | | |  _| |_ 
/ /\  /| |\ V /  __/ (_| | |_| | |_   _|
\_\ \/ |_| \_/ \___|\__,_|\__,_|   |_|  
                                        
"""
            )
            print(f"\nFélicitations {self.nom} a monté au niveau {self.niveau}!\n")
            self.pv += 20
            self.pv_max += 20
            print(
                f"{self.nom} a gagné 20 points de vie en bonus! Il peut désormais avoir jusqu'à {self.pv_max} points de vie.\n"
            )

    # suppression d'XP si le personnage perd
    def remove_xp(self):
        """_summary_
        Si le personnage perd les XP sont réduits sans pouvoir allez en dessous de 0.
        Le niveau est également décrementé si nécessaire (les niveaux changent tous les 100 XP).
        """
        self.xp -= 20
        if self.xp < 0:
            self.xp = 0
            print(f"\n{self.nom} a 0 points d'expérience et reste à niveau 1.\n")
            return
        print(
            f"{self.nom} a perdu 20 points d'expérience. Il lui reste {self.xp} points."
        )
        # vérifier si le jouer descendre d'un niveau
        if self.xp < self.niveau * 100 and self.niveau != 1:
            self.niveau -= 1
            self.pv_max -= 20
            print(
                """
   __   _                               
  /\ \ (_)_   _____  __ _ _   _        
 /  \/ / \ \ / / _ \/ _` | | | |  _____ 
/ /\  /| |\ V /  __/ (_| | |_| | |_____|
\_\ \/ |_| \_/ \___|\__,_|\__,_|     
                                        
"""
            )
            print(
                f"\nDommage, {self.nom} a perdu un niveau. \n{self.nom} est de retour au niveau {self.niveau}!\n"
            )
