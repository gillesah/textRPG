from modules.personnage import Personnage
from modules.utils import pop_ennemi, continuer
import time

ennemi = pop_ennemi()


def jeu():
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
    nom_personnage = input("Donnez un nom à votre personnage : ")
    personnage = Personnage(nom_personnage)
    print(f"\nBonjour {personnage.nom}!")
    print(personnage.show_XP())
    time.sleep(2.5)
    print(f"{personnage.nom} va affronter\n {ennemi.intro}")
    print(ennemi)
    print("**")
    while True:
        user_ask = input(
            "Que voulez-vous faire : \n A - Attaquer \n B - Rechercher un objet \n C - Utiliser un objet \n REPONSE :  "
        ).lower()
        if user_ask == "a":
            personnage.attaquer(ennemi)
            if ennemi.check_life():
                personnage.add_xp()
                print(f"vous avez {personnage.xp} XP")
                continuer(personnage)

        # l'ennemi attaque juste après

        elif user_ask == "b":
            personnage.search_object()

        elif user_ask == "c":
            if not personnage.use_potion():
                continue

        else:
            print("Merci d'entrer une valeur A, B ou C")
            user_ask = input(
                "Que voulez-vous faire : \n A - Attaquer \n B - Rechercher un objet \n C - Utiliser un objet \n REPONSE :  "
            ).lower()

        time.sleep(1)
        print("**** Oh non... l'ennemi vous attaque !!!!!! ****")
        ennemi.attaquer(personnage)

        time.sleep(1)
        if personnage.check_life():
            personnage.remove_xp()
            time.sleep(1)
            continuer(personnage)
        else:
            print("*" * 8)
            print(personnage)
            print(ennemi)
            print("*" * 8)

        time.sleep(1)


jeu()
