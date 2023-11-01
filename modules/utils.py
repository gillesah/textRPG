import random
from modules.ennemi import Ennemi
import time

# l'ennemi est choisi en random


def pop_ennemi() -> Ennemi:
    ennemis = [
        {
            "nom": "Gobelin",
            "pv": 50,
            "dega_min": 10,
            "dega_max": 20,
            "intro": """
   ___      _          _ _       
  / _ \___ | |__   ___| (_)_ __  
 / /_\/ _ \| '_ \ / _ \ | | '_ \ 
/ /_\\\\ (_) | |_) |  __/ | | | | |
\____/\___/|_.__/ \___|_|_|_| |_|
                                 
""",
        },
        {
            "nom": "Orc",
            "pv": 75,
            "dega_min": 10,
            "dega_max": 20,
            "intro": """
   ___          
  /___\_ __ ___ 
 //  // '__/ __|
/ \_//| | | (__ 
\___/ |_|  \___|
                
""",
        },
        {
            "nom": "Dragon",
            "pv": 100,
            "dega_min": 10,
            "dega_max": 20,
            "intro": """

    ___                             
   /   \_ __ __ _  __ _  ___  _ __  
  / /\ / '__/ _` |/ _` |/ _ \| '_ \ 
 / /_//| | | (_| | (_| | (_) | | | |
/___,' |_|  \__,_|\__, |\___/|_| |_|
                  |___/             

""",
        },
    ]

    ennemi_number = random.randint(0, len(ennemis) - 1)
    ennemi = Ennemi(
        ennemis[ennemi_number]["nom"],
        ennemis[ennemi_number]["pv"],
        ennemis[ennemi_number]["dega_min"],
        ennemis[ennemi_number]["dega_max"],
        ennemis[ennemi_number]["intro"],
    )
    return ennemi


# fonction continuer le joue en fin de partie
def continuer(personnage):
    while True:
        rejouer = input("Voulez-vous rejouer ? (O/N) :  ").lower()
        if rejouer == "o":
            print("changement de l'ennemi")
            if personnage.pv <= 0:
                personnage.inventaire["potion"] = 0
                personnage.inventaire["epee"] = 0
            personnage.pv = personnage.pv_max
            ennemi = pop_ennemi()
            print(f" Attention, voici \n{ennemi.intro}\n{ennemi}")
            return ennemi

        elif rejouer == "n":
            print(
                f"\nVous terminez le jeu avec {personnage.xp} points d'expérience au niveau {personnage.niveau}.\n"
            )
            print(
                """
   _     _                              _           _            
  /_\   | | __ _   _ __  _ __ ___   ___| |__   __ _(_)_ __   ___ 
 //_\\\\  | |/ _` | | '_ \| '__/ _ \ / __| '_ \ / _` | | '_ \ / _ \\
/  _  \ | | (_| | | |_) | | | (_) | (__| | | | (_| | | | | |  __/
\_/ \_/ |_|\__,_| | .__/|_|  \___/ \___|_| |_|\__,_|_|_| |_|\___|
                  |_|                                            
                  ___       _        _ _ _                       
                 / __\ __ _| |_ __ _(_) | | ___                  
                /__\/// _` | __/ _` | | | |/ _ \                 
               / \/  \ (_| | || (_| | | | |  __/                 
               \_____/\__,_|\__\__,_|_|_|_|\___|                 
                                                                 
                  """
            )
            time.sleep(1)
            exit()
        else:
            print("Merci de choisir O (oui) ou N (non)")


def show_title():
    print(
        """
          
          

   __           ___       _        _ _ _      
  / /  __ _    / __\ __ _| |_ __ _(_) | | ___ 
 / /  / _` |  /__\/// _` | __/ _` | | | |/ _ \\
/ /__| (_| | / \/  \ (_| | || (_| | | | |  __/
\____/\__,_| \_____/\__,_|\__\__,_|_|_|_|\___|
     _                                        
  __| | ___  ___    /\  /\___ _ __ ___  ___   
 / _` |/ _ \/ __|  / /_/ / _ \ '__/ _ \/ __|  
| (_| |  __/\__ \ / __  /  __/ | | (_) \__ \  
 \__,_|\___||___/ \/ /_/ \___|_|  \___/|___/  
                                              

"""
    )


def declare_victory():
    print(
        """
        _      _        _           
 /\   /(_) ___| |_ ___ (_)_ __ ___  
 \ \ / / |/ __| __/ _ \| | '__/ _ \ 
  \ V /| | (__| || (_) | | | |  __/ 
   \_/ |_|\___|\__\___/|_|_|  \___|                        

"""
    )


def declare_defeat():
    print(
        """
          

   ___       _        _ _ _      
  / __\ __ _| |_ __ _(_) | | ___ 
 /__\/// _` | __/ _` | | | |/ _ \\
/ \/  \ (_| | || (_| | | | |  __/
\_____/\__,_|\__\__,_|_|_|_|\___|
   ___             _             
  / _ \___ _ __ __| |_   _  ___  
 / /_)/ _ \ '__/ _` | | | |/ _ \ 
/ ___/  __/ | | (_| | |_| |  __/ 
\/    \___|_|  \__,_|\__,_|\___| 
                                 

"""
    )
