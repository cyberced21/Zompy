import pygame
from model import constantes
from model import personnages
from model import niveau
from model import menu
from model import selectionPersonnage
from model import score
from model.partie import Partie

#########################################
#               Game loop               3
#########################################

son = pygame.mixer.Sound(constantes.sonMenuChemin)
imagePerso = constantes.perso1
menu = menu.Menu()
selectMenu = selectionPersonnage.SelectionPersonnage()
score = score.Score()
action = ""
clock = pygame.time.Clock()
while True:
    son.play()
    clock.tick(constantes.FPS)
    menu.run()
    action = menu.run()

    if(action == "quitter"):
        son.stop()
        pygame.quit()
    elif(action == "score"):
        action = score.afficherScore()
        son.stop()
        menu.run()
    elif(action == "jouer"):
        action = selectMenu.run()

        if(action == "perso1"):
            imagePerso = constantes.perso1

        elif(action == "perso2"):
            imagePerso = constantes.perso2

        elif(action == "perso3"):
            imagePerso = constantes.perso3

        son.stop()
        partie = Partie(imagePerso)
        pointage = partie.jouer()
        score.ajouterScore(pointage)

pygame.quit()
quit()
