import random
from modules.ennemi import Ennemi


def pop_ennemi() -> Ennemi:
    ennemis = [
        {"nom": "Gobelin", "pv": 50, "dega_min": 10, "dega_max": 20},
        {"nom": "Orc", "pv": 75, "dega_min": 10, "dega_max": 20},
        {"nom": "Dragon", "pv": 100, "dega_min": 10, "dega_max": 20},
    ]

    ennemi_number = random.randint(0, len(ennemis) - 1)
    ennemi = Ennemi(
        ennemis[ennemi_number]["nom"],
        ennemis[ennemi_number]["pv"],
        ennemis[ennemi_number]["dega_min"],
        ennemis[ennemi_number]["dega_max"],
    )
    return ennemi

