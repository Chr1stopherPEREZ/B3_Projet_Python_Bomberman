# Importation des modules internes et externes nécessaires pour le jeu
import core.board as board
import entities.player as player
import entities.bomb as bomb
import entities.enemies as enemies
import utils.settings as settings
import pygame

# Initialisation de Pygame (nécessaire avant d'utiliser ses fonctionnalités)
pygame.init()

# Définir la taille de la fenêtre en fonction de la taille des cases et du nombre de cases (13x13)
Window_Size = settings.Box_size * 13
screen = pygame.display.set_mode((Window_Size, Window_Size))
pygame.display.set_caption("B3_Projet_Python_Bomberman")

# Définir la police pour l'affichage du score
font = pygame.font.Font(None, 12)

# Initialisation du plateau de jeu et des entités
nb_line, nb_column = 13, 13
# Créer le plateau de jeu avec des briques placées aux positions spécifiées
game_plate = board.starting_plate(nb_line, nb_column, bricks=[(2, 6), (0, 5), (2, 2)])
player_position = (6, 6)
enemy_positions = enemies.initialize_enemies()

# Initialisation des variables pour le score et les pénalités
score = 1000
down_score = 10

# Configuration pour le déplacement des ennemis
enemy_move_delay = 1000
last_enemy_move_time = pygame.time.get_ticks()

# Variable de contrôle pour la boucle du jeu
run = True

# Boucle principale du jeu
while run:
    # Gestion des événements (clavier, fermeture de fenêtre, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # Déplacement du joueur selon la touche pressée (z, s, q, d pour haut, bas, gauche, droite)
            if event.key in [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]:
                direction = {
                    pygame.K_z: "z",
                    pygame.K_s: "s",
                    pygame.K_q: "q",
                    pygame.K_d: "d",
                }[event.key]
                # Mettre à jour la position du joueur en fonction de la direction choisie
                player_position = player.move_player(
                    player_position, direction, game_plate
                )
                score -= down_score
            elif event.key == pygame.K_b:
                bomb.add_bomb(player_position)

            # Vérifier si le joueur entre en collision avec un ennemi après le déplacement
            if player.check_collision(player_position, enemy_positions):
                print("Vous avez perdu, va falloir retenter :')")
                run = False

    # Gérer le déplacement des ennemis toutes les `enemy_move_delay` millisecondes
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_move_time > enemy_move_delay:
        # Déplacer chaque ennemi
        enemy_positions = [
            enemies.move_enemy(pos, game_plate) for pos in enemy_positions
        ]
        last_enemy_move_time = current_time

        # Vérifier si un ennemi a atteint la position du joueur
        if player.check_collision(player_position, enemy_positions):
            print("Vous avez perdu, va falloir retenter :')")
            run = False

    # Effacer l'écran avant de redessiner (pour éviter des superpositions)
    screen.fill(settings.Color_background)

    # Afficher le plateau de jeu, le joueur, et les ennemis sur la fenêtre
    board.view_plate(screen, game_plate, player_position, enemy_positions)

    # Vérifier si tous les ennemis ont été éliminés
    if not enemy_positions:
        print("Félicitation vous avez gagné !")
        run = False

    # Afficher le score à l'écran
    if score != 0:
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (2, 2))
    else:
        print("Votre score est à zéro, va falloir retenter :')")
        run = False

    # Mettre à jour l'état des bombes (explosions, dégâts, etc...)
    if bomb.update_bombs(
        screen, game_plate, enemy_positions, player_position, nb_line, nb_column
    ):
        print("Votre bombe vous a explosé à la gueule, va falloir retenter :')")
        run = False

    # Mettre à jour l'affichage de la fenêtre
    pygame.display.flip()

# Quitter Pygame une fois la boucle terminée
pygame.quit()

# main.py
