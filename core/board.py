import pygame
import utils.settings as settings


# Fonction pour créer le plateau de jeu
def starting_plate(nb_line, nb_column, bricks):
    # Création du plateau : une grille où les cases sont soit vides, soit une brique (cassable ou non)
    plate = [
        [
            " " if row_index % 2 == 0 else ("X" if col_index % 2 != 0 else " ")
            for col_index in range(nb_column)
        ]
        for row_index in range(nb_line)
    ]

    # Placement des briques cassables sur le plateau
    for x, y in bricks:
        if 0 <= x < nb_line and 0 <= y < nb_column:
            plate[x][y] = "B"

    return plate  # Retourne le plateau avec les briques placées


# Fonction pour afficher le plateau et ses éléments (joueur, ennemis, briques)
def view_plate(screen, plate, player_position, enemys):
    for row_index, row in enumerate(plate):
        for col_index, case in enumerate(row):
            # Défini les dimensions du rectangle représentant la case actuelle
            rect = (
                col_index * settings.Box_size,
                row_index * settings.Box_size,
                settings.Box_size,
                settings.Box_size,
            )

            # Dessine les éléments en fonction de leur type
            if (row_index, col_index) == player_position:
                pygame.draw.rect(screen, settings.Color_player, rect)
            elif (row_index, col_index) in enemys:
                pygame.draw.rect(screen, settings.Color_enemy, rect)
            elif case == "X":
                pygame.draw.rect(screen, settings.Color_unbreakable_brick, rect)
            elif case == "B":
                pygame.draw.rect(screen, settings.Color_breakable_brick, rect)
            else:
                pygame.draw.rect(screen, settings.Color_board, rect)


# Board.py
