import pygame
from model import constantes
from model import personnages
from model import niveau
from model import menu

class Zompy():
    def __init__(self):
        #Initialisation
        pygame.init()
        pygame.mixer.init() #Si on veux ajouter du son
        self.fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.running = True
        self.ennemis = pygame.sprite.Group()
        self.spriteGroup = pygame.sprite.Group()
        self.balles = pygame.sprite.Group()
        self.joueur = personnages.Hero()
        self.niveau1 = niveau.Niveau(8)
        self.niveau2 = niveau.Niveau(25)
        self.niveau2.start()
        for i in range(8):
            self.spriteGroup.add(self.niveau2.get_listeEnnemis())
            self.ennemis.add(self.niveau2.get_listeEnnemis())
        self.spriteGroup.add(self.joueur)

    # Fonction a integrer a la classe du Jeu
    def drawScore(self, surf, score):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 24)
        text_surface = font.render("Score: " + score, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (constantes.LARGEUR/2, 0)
        surf.blit(text_surface, text_rect)

    # Demarre une partie
    def jouer(self):
        while(self.running):
            # FPS
            self.clock.tick(constantes.FPS)
            # Evenements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        balle = self.joueur.shoot()
                        self.spriteGroup.add(balle)
                        self.balles.add(balle)

            # Update
            self.spriteGroup.update()

            # Verifie si une balle a touche un ennemi
            hits = pygame.sprite.groupcollide(self.ennemis, self.balles, True, True)
            # Si oui, on le regenere
            for hit in hits:
                self.score += 1
                e = personnages.Ennemi()
                self.spriteGroup.add(e)
                self.ennemis.add(e)

            # Verifie si le joueur s'est fait toucher
            hits = pygame.sprite.spritecollide(self.joueur, self.ennemis, False)
            if hits:
                self.running = False

            # Dessiner
            self.fenetre.fill((56, 26, 164))
            self.spriteGroup.draw(self.fenetre)
            self.drawScore(self.fenetre, str(self.score))

            # A faire apres avoir tout dessiner
            pygame.display.flip()

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
        zompy = Zompy()
        zompy.jouer()
        menu.run()

pygame.quit()
