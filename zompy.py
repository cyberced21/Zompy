import pygame
import os
from model import constantes
from model import personnages
from model import niveau

#Initialisation
pygame.init()
pygame.mixer.init() #Si on veux ajouter du son
fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
fond = pygame.image.load(os.path.join(constantes.repertoire_images, "space.png")).convert()
clock = pygame.time.Clock()
score = 0

ennemis = pygame.sprite.Group()
spriteGroup = pygame.sprite.Group()
balles = pygame.sprite.Group()
joueur = personnages.Hero()
niveau1 = niveau.Niveau(8)
niveau2 = niveau.Niveau(25)
niveau2.start()
for i in range(8):
    spriteGroup.add(niveau2.get_listeEnnemis())
    ennemis.add(niveau2.get_listeEnnemis())
spriteGroup.add(joueur)

# Fonction a integrer a la classe du Jeu
def drawScore(surf, score):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 24)
    text_surface = font.render("Score: " + score, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (constantes.LARGEUR/2, 0)
    surf.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    # FPS
    clock.tick(constantes.FPS)

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                balle = joueur.shoot()
                spriteGroup.add(balle)
                balles.add(balle)

    # Update
    spriteGroup.update()

    # Verifie si une balle a touche un ennemi
    hits = pygame.sprite.groupcollide(ennemis, balles, True, True)
    # Si oui, on le regenere
    for hit in hits:
        score += 1
        e = personnages.Ennemi()
        spriteGroup.add(e)
        ennemis.add(e)

    # Verifie si le joueur s'est fait toucher
    hits = pygame.sprite.spritecollide(joueur, ennemis, False)
    if hits:
        running = False

    # Dessiner
    fenetre.blit(fond, [0, 0])
    spriteGroup.draw(fenetre)
    drawScore(fenetre, str(score))

    # A faire apres avoir tout dessiner
    pygame.display.flip()

pygame.quit()
