import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640,480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

perso = pygame.image.load("perso.png").convert_alpha()
positionPerso = perso.get_rect()
fenetre.blit(perso, positionPerso)

pygame.display.flip()
pygame.key.set_repeat(400, 30)


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                positionPerso = positionPerso.move(0, 10)
            if event.key == K_UP:
                positionPerso = positionPerso.move(0,-10)
            if event.key == K_LEFT:
                positionPerso = positionPerso.move(-10, 0)
            if event.key == K_RIGHT:
                positionPerso = positionPerso.move(10, 00)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[1] < 100:
                    print("Zone dangereuse !")
        
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, positionPerso)
    pygame.display.flip()

