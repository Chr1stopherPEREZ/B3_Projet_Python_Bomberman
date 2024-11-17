import time
import pygame
import utils.settings as settings

# Liste globale qui stocke toutes les bombes placées sur le plateau
bombs = []


def add_bomb(position):
    # "
    # Ajoute une bombe à la liste `bombs` avec sa position et le temps auquel elle a été placée.
    # La position est un tuple (x, y), et le temps est capturé avec `time.time()` pour savoir quand l'explosion doit se produire.
    # "
    bombs.append({"position": position, "time": time.time()})


def update_bombs(screen, game_plate, enemies, player_position, nb_line, nb_column):

    # "
    # Met à jour l'état des bombes : vérifie si elles explosent, dessine les bombes restantes,
    # et gère les explosions en fonction du temps écoulé.

    # - Vérifie si chaque bombe a explosé (2 secondes après son ajout).
    # - Dessine les bombes qui sont encore en jeu.
    # - Si une bombe explose, elle affecte le joueur, les ennemis et les briques.

    # Retourne un booléen `player_hit` qui indique si le joueur a été touché par une explosion.
    # "

    # Récupère le temps actuel
    current_time = time.time()
    # Vérifie si une bombe a explosé (2 secondes après son ajout)
    player_hit = any(
        explode_bomb(
            bomb["position"], game_plate, enemies, player_position, nb_line, nb_column
        )
        for bomb in bombs
        if current_time - bomb["time"] >= 2
    )

    # Supprime les bombes qui ont explosé (celles dont le temps d'explosion est passé)
    bombs[:] = [bomb for bomb in bombs if current_time - bomb["time"] < 2]

    # Dessine les bombes restantes à l'écran
    for bomb in bombs:
        x, y = bomb["position"]
        # Calcule les coordonnées pour afficher la bombe en utilisant la taille de la case définie dans les paramètres
        box = (
            y * settings.Box_size,
            x * settings.Box_size,
            settings.Box_size,
            settings.Box_size,
        )
        pygame.draw.rect(
            screen, settings.Color_bomb, box
        )  # Dessine un carré représentant la bombe

    return player_hit  # Retourne si le joueur a été touché par une explosion


def explode_bomb(position, game_plate, enemies, player_position, nb_line, nb_column):

    # "
    # Gère l'explosion d'une bombe à une position donnée. L'explosion affecte les briques cassables,
    # les ennemis, et vérifie si le joueur est touché.

    # L'explosion touche les cases adjacentes (haut, bas, gauche, droite) à la bombe.
    # Si la bombe touche un ennemi, il est retiré de la liste des ennemis.
    # Si la bombe touche une brique cassable, elle est détruite.
    # Si le joueur est dans la zone d'explosion, il est marqué comme touché.

    # Retourne un booléen `player_hit` qui indique si le joueur a été touché par l'explosion.
    # "

    x, y = position
    # Détermine la zone d'explosion (cases adjacentes à la bombe)
    explosion_area = [(x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    player_hit = False

    # Parcourt toutes les cases affectées par l'explosion
    for explosion_x, explosion_y in explosion_area:
        # Vérifie que la case est dans les limites du plateau
        if 0 <= explosion_x < nb_line and 0 <= explosion_y < nb_column:
            # Si la position de l'explosion touche le joueur
            if (explosion_x, explosion_y) == player_position:
                player_hit = True
            # Si la case contient une brique cassable, elle est détruite
            if game_plate[explosion_x][explosion_y] == "B":
                game_plate[explosion_x][explosion_y] = " "
            # Si la case contient un ennemi, l'ennemi est éliminé
            elif (explosion_x, explosion_y) in enemies:
                enemies.remove((explosion_x, explosion_y))
    # Retourne True si le joueur a été touché par l'explosion
    return player_hit


# Bomb.py
