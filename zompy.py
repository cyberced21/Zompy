import pygame
from model import constantes
from model import personnages
from model import niveau
from model import menu
from model import selectionPersonnage
from model.partie import Partie

#########################################
#               Game loop               3
#########################################

imagePerso = constantes.perso1
menu = menu.Menu()
selectMenu = selectionPersonnage.SelectionPersonnage()
action = ""
clock = pygame.time.Clock()
while True:
    clock.tick(constantes.FPS)
    menu.run()
    action = menu.run()

    if(action == "quitter"):
        pygame.quit()
    elif(action == "score"):
        menu.run()
    elif(action == "jouer"):
        action = selectMenu.run()

        if(action == "perso1"):
            imagePerso = constantes.perso1

        elif(action == "perso2"):
            imagePerso = constantes.perso2

        elif(action == "perso3"):
            imagePerso = constantes.perso3

        partie = Partie(imagePerso)
        partie.jouer()

pygame.quit()
quit()
