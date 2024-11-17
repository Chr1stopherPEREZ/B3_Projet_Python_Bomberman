import random  # Importation du module random pour générer des mouvements aléatoires

# Dictionnaire contenant les mouvements possibles pour les ennemis
# Chaque direction est définie par un déplacement en (ligne, colonne)
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def move_enemy(enemy_position, plate):
    # Décomposer la position actuelle de l'ennemi en coordonnées x et y
    position_x, position_y = enemy_position

    # Extraire les valeurs du dictionnaire 'moves' pour obtenir une liste des directions possibles
    directions = list(moves.values())

    # Mélanger la liste des directions pour que le mouvement soit aléatoire
    random.shuffle(directions)

    # Essayer de déplacer l'ennemi dans chaque direction possible
    for direction_x, direction_y in directions:
        # Calculer la nouvelle position en ajoutant la direction choisie
        new_position_x = position_x + direction_x
        new_position_y = position_y + direction_y

        # Vérifier si la nouvelle position est valide :
        # - Elle doit être dans les bornes du plateau
        # - Elle doit être une case vide (représentée par " ")
        if (
            0 <= new_position_x < len(plate)
            and 0 <= new_position_y < len(plate[0])
            and plate[new_position_x][new_position_y] == " "
        ):
            # Si la nouvelle position est valide, l'ennemi se déplace vers cette position
            return new_position_x, new_position_y

    # Si aucun déplacement n'est possible, l'ennemi reste à sa position actuelle
    return position_x, position_y


def initialize_enemies():
    # Retourne une liste de positions initiales pour les ennemis (3 enemis)
    return [(0, 0), (12, 12), (0, 12)]


# Enemies.py
