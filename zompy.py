import pygame
from model import constantes
from model import personnages
from model import niveau
from model import menu
from model.partie import Partie

#########################################
#               Game loop               3
#########################################
menu = menu.Menu()
action = ""
clock = pygame.time.Clock()
while True:
    clock.tick(constantes.FPS)
    action = menu.run()
    if(action == "quitter"):
        pygame.quit()
    elif(action == "score"):
        menu.run()
    elif(action == "jouer"):
        partie = Partie()
        partie.jouer()
        menu.run()

pygame.quit()
