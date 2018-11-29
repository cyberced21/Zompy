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

imagePerso = ""
menu = menu.Menu()
selectMenu = selectionPersonnage.SelectionPersonnage()
action = ""
action2 = ""
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
        #clock.tick(constantes.FPS)
        selectMenu.run()
        action2 = selectMenu.run()

        if(action2 == "perso1"):
            imagePerso = constantes.perso1

        elif(action2 == "perso2"):
            imagePerso = constantes.perso2

        elif(action2 == "perso3"):
            imagePerso = constantes.perso3

        partie = Partie()
        partie.jouer()
        #menu.run()

pygame.quit()
