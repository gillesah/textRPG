from modules.personnage import Personnage
from modules.utils import (
    pop_ennemi,
    continuer,
    show_title,
    declare_defeat,
    declare_victory,
)
import time

ennemi = pop_ennemi()


def jeu():
    # annonce le jeu
    show_title()
    print(
        "\nDans ce jeu, vous allez affronter des ennemis formidables. \nA chaque tour, vous allez choisir entre attaquer, chercher un objet ou utiliser un objet.\nLes objets possibles sont : \nPotion - augmente vos points de vie par 20 points. Vous n'êtes pas attaqué par l'ennemi avant votre prochain tour.\nÉpée - vous permet d'enlever 15 points de l'ennemi avant de l'attaquer.\nSi vous gagnez une bataille et il vous reste des objets, vous les gardez pour la prochaine bataille. Si vous perdez, vos objets sont perdus.\n"
    )

    # créer le personnage de l'joueur
    nom_personnage = input("Donnez un nom à votre personnage : ")
    personnage = Personnage(nom_personnage)
    print(f"\nBonjour {personnage.nom}!")
    print(personnage.show_XP())
    time.sleep(2)

    # créer et introduire l'ennemi
    ennemi = pop_ennemi()
    print(f"{personnage.nom} va affronter\n {ennemi.intro}")
    print(ennemi)
    print("**")

    # commencer la bataille avec un boucle qui continue tant que l'joueur ne choisit pas de quitter le jeu
    while True:
        user_ask = input(
            "Que voulez-vous faire : \n A - Attaquer \n B - Rechercher un objet \n C - Utiliser un objet \n REPONSE :  "
        ).lower()
        if user_ask == "a":
            # attaquer l'ennemi
            personnage.attaquer(ennemi)
            if ennemi.check_life():
                # si l'ennemi est mort, déclarer la victoire et demander à continuer
                declare_victory()
                personnage.add_xp()
                ennemi = continuer(
                    personnage
                )  # permet de changer l'ennemi si le joueur décide de continuer
            else:
                # si l'ennemi n'est pas mort, il attaque
                time.sleep(1)
                print("**** Oh non... l'ennemi vous attaque !!!!!! ****")
                ennemi.attaquer(personnage)

        elif user_ask == "b":
            # le personnage cherche un objet et l'ennemi attaque ensuite
            personnage.search_object()
            time.sleep(1)
            print("**** Oh non... l'ennemi vous attaque !!!!!! ****")
            ennemi.attaquer(personnage)

        elif user_ask == "c":
            # choisir et puis utiliser un objet de l'inventaire
            choix_objet = personnage.choose_object()
            personnage.use_object(choix_objet, ennemi)
            if ennemi.check_life():
                # si l'ennemi est mort, déclarer la victoire et demander à continuer
                declare_victory()
                personnage.add_xp()
                ennemi = continuer(
                    personnage
                )  # permet de changer l'ennemi si le joueur décide de continuer
            continue

        else:
            # si la réponse de l'joueur n'est pas valide, demandez à nouveau
            print("Merci d'entrer une valeur A, B ou C")
            continue

        time.sleep(1)

        if personnage.check_life():
            # vérifie si le personnage est en vie et si il est mort,
            # déclarer la défaite et proposer à continuer
            declare_defeat()
            personnage.remove_xp()
            time.sleep(1)
            ennemi = continuer(
                personnage
            )  # permet de changer l'ennemi si le joueur décide de continuer
        else:
            # si le personnage est en vie, afficher l'état actuel des deux combatants
            print("*" * 8)
            print(personnage)
            print(ennemi)
            print("*" * 8)
        time.sleep(1)


jeu()
