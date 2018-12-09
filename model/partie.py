import pygame
from . import constantes
from . import personnages
from . import niveau
from . import equipments

class Partie():
    """
    Classe represantant une partie dans le jeu Zompy
    """
    def __init__(self,imagePerso):
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
        self.joueur = personnages.Hero("cedrik",100,[equipments.Canon(),equipments.DefaultPistol()],imagePerso,(0,0),0)
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

    def drawCurrentWeapon(self,surf,equipment_name):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 24)
        text_surface = font.render("Current weapon : " + equipment_name, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midbottom = (constantes.LARGEUR/1.25, constantes.HAUTEUR-30)
        surf.blit(text_surface, text_rect)

    # Inscris le compte a rebours avant le prochain niveau
    def drawTime(self, surf, time):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 24)
        text_surface = font.render("Prochain niveau dans: " + str(10 - int(time)), True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (constantes.LARGEUR-145, 0)
        surf.blit(text_surface, text_rect)

    # Demarre une partie
    def jouer(self):
        niveauTermine = False
        nivActuel = 0
        timer = 0
        # On demarre le premier niveau
        self.niveau = niveau.Niveau(self.listeNbEnnemis[nivActuel])
        self.niveau.start()
        ennemis = self.niveau.get_listeEnnemis()
        self.spriteGroup.add(ennemis)
        self.ennemis.add(ennemis)

        while(self.running):
            # Si le niveau actuel est termine, on demarre le niveau suivant
            if(niveauTermine):
                timer = (pygame.time.get_ticks() - timerstart) / 1000
                if(timer >= constantes.interval_niveaux):
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
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        balle = self.joueur.shoot()
                        self.spriteGroup.add(balle)
                        self.balles.add(balle)
                    if event.key == pygame.K_q:
                        self.joueur.setCurrentEquipment()

            # Update
            self.spriteGroup.update()

            # Verifie si une balle a touche un ennemi
            hits = pygame.sprite.groupcollide(self.ennemis, self.balles, True, True)
            # Si oui, on le regenere
            for hit in hits:
                self.score += 1
                # Verifie si le niveau est termine
                if(len(self.ennemis) == 0):
                    niveauTermine = True
                    timerstart = pygame.time.get_ticks()

            # Verifie si le joueur s'est fait toucher
            hits = pygame.sprite.spritecollide(self.joueur, self.ennemis, False)
            if hits:
                self.running = False
                return self.score

            # Dessiner
            self.fenetre.fill((56, 26, 164))
            self.spriteGroup.draw(self.fenetre)
            self.drawCurrentWeapon(self.fenetre,self.joueur.getCurrentEquipment().name)
            self.drawScore(self.fenetre, str(self.score))
            if(niveauTermine):
                self.drawTime(self.fenetre, timer)

            # A faire apres avoir tout dessiner
            pygame.display.flip()
