import pygame
from . import constantes
from . import personnages
from . import niveau

class Partie():
    """
    Classe represantant une partie dans le jeu Zompy
    """
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
        self.listeNbEnnemis = [5, 9, 12, 15, 19, 22, 25, 27, 30, 35]
        self.spriteGroup.add(self.joueur)

    # Inscris le score actuel
    def drawScore(self, surf, score):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 24)
        text_surface = font.render("Score: " + score, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (constantes.LARGEUR/2, 0)
        surf.blit(text_surface, text_rect)

    # Demarre une partie
    def jouer(self):
        niveauTermine = False
        nivActuel = 0
        # On demarre le premier niveau
        self.niveau = niveau.Niveau(self.listeNbEnnemis[nivActuel])
        self.niveau.start()
        ennemis = self.niveau.get_listeEnnemis()
        self.spriteGroup.add(ennemis)
        self.ennemis.add(ennemis)

        # On affecte l'evenement qui va se declencher quand le temps entre les niveaux sera ecouler
        tempsecoulerEvent = pygame.USEREVENT + 1 # On met +1 pour qu'il n'y ait pas de conflits entre les evenements

        while(self.running):
            # Si le niveau actuel est termine, on demarre le niveau suivant
            if(niveauTermine and pygame.event.get(tempsecoulerEvent)):
                for event in pygame.event.get():
                    if event == tempsecoulerEvent:
                        nivActuel += 1
                        # On retire les ennemis du niveau precedant des spriteGroup
                        self.spriteGroup.remove(ennemis)
                        self.ennemis.remove(ennemis)
                        # On regenere le nouveau niveau
                        self.niveau = niveau.Niveau(self.listeNbEnnemis[nivActuel])
                        self.niveau.start()
                        # On ajoute les nouveaux ennemis aux spriteGroups
                        ennemis = self.niveau.get_listeEnnemis()
                        self.spriteGroup.add(ennemis)
                        self.ennemis.add(ennemis)
                        niveauTermine = False

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
                if(len(self.ennemis) == 0):
                    pygame.time.set_timer(tempsecoulerEvent, 10000)
                    niveauTermine = True

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