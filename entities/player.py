# Importation du module random pour mélanger les directions des ennemis
import random

# Dictionnaire définissant les mouvements possibles pour le joueur avec les touches "q", "d","z", "s"
moves = {"q": (0, -1), "d": (0, 1), "z": (-1, 0), "s": (1, 0)}


def move_player(player_position, direction, plate):
    position_x, position_y = player_position
    if direction in moves:
        move_x, move_y = moves[direction]
        new_position_x = position_x + move_x
        new_position_y = position_y + move_y
        # Vérifie que la nouvelle position est dans les limites du plateau et que la case est vide
        if (
            0 <= new_position_x < len(plate)
            and 0 <= new_position_y < len(plate[0])
            and plate[new_position_x][new_position_y] == " "
        ):
            return new_position_x, new_position_y
    return position_x, position_y


def check_collision(player_position, enemies):
    return (
        player_position in enemies
    )  # Retourne True si la position du joueur est dans la liste des ennemis


def move_enemy(enemy_position, plate):
    position_x, position_y = enemy_position
    directions = list(moves.values())
    random.shuffle(directions)

    for move_x, move_y in directions:
        new_position_x = position_x + move_x
        new_position_y = position_y + move_y
        # Vérifie que la nouvelle position est dans les limites du plateau et que la case est vide
        if (
            0 <= new_position_x < len(plate)
            and 0 <= new_position_y < len(plate[0])
            and plate[new_position_x][new_position_y] == " "
        ):
            # Retourne la nouvelle position de l'ennemi
            return new_position_x, new_position_y
    # Si aucune direction n'est valide, l'ennemi reste à sa position actuelle
    return position_x, position_y


# Player.py
