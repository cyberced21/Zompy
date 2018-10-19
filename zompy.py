import pygame
from model import constantes
from model import personnages
from model import niveau

#Initialisation
pygame.init()
pygame.mixer.init() #Si on veux ajouter du son
fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
clock = pygame.time.Clock()

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
        e = personnages.Ennemi()
        spriteGroup.add(e)
        ennemis.add(e)

    # Verifie si le joueur s'est fait toucher
    hits = pygame.sprite.spritecollide(joueur, ennemis, False)
    if hits:
        running = False

    # Dessiner
    fenetre.fill((56, 26, 164))
    spriteGroup.draw(fenetre)

    # A faire apres avoir tout dessiner
    pygame.display.flip()

pygame.quit()
