import pygame
from . import constantes

pygame.init()


fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
clock_tick_rate=20

son = pygame.mixer.Sound(constantes.sonMenuChemin)


def text_objects(text, font):
    textSurface = font.render(text, True, constantes.white)
    return textSurface, textSurface.get_rect()


class Button():

    def __init__(self,msg,x,y,w,h,ic,ac,action=None):

        #msg: What do you want the button to say on it.

        #x: The x location of the top left coordinate of the button box.

        #y: The y location of the top left coordinate of the button box.

        #w: Button width.

        #h: Button height.

        #ic: Inactive color (when a mouse is not hovering).

        #ac: Active color (when a mouse is hovering).

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.msg = msg
        self.action = action

    def draw(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.x+self.w > self.mouse[0] > self.x and self.y+self.h > self.mouse[1] > self.y:
            pygame.draw.rect(fenetre, self.ac,(self.x,self.y,self.w,self.h))
            if self.click[0] == 1 and self.action != None:
                return self.action
        else:
            pygame.draw.rect(fenetre, self.ic,(self.x,self.y,self.w,self.h))

        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = ( (self.x+(self.w/2)), (self.y+(self.h/2)) )
        fenetre.blit(textSurf, textRect)


class Menu():

    def __init__(self):

        self.dead=False
        #fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
        self.clock = pygame.time.Clock()
        self.background_image = constantes.fondMenu
        self.bJouer = Button("GO!",150,450,100,50,constantes.green,constantes.bright_green,"jouer")
        self.bScore = Button("Score",350,450,100,50,constantes.blue,constantes.bright_blue,"score")
        self.bQuitter = Button("Quit",550,450,100,50,constantes.red,constantes.bright_red,"quitter")

    def run(self):
        son.play()
        while(self.dead==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.dead = True

            fenetre.blit(self.background_image, [0, 0])

            #Texte du menu
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("SpacePy", largeText)
            TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/2))
            fenetre.blit(TextSurf, TextRect)

            if(self.bJouer.draw() == "jouer"):
                son.stop()
                return "jouer"
                dead = True
            if(self.bScore.draw() == "score"):
                son.stop()
                dead = True
                return "score"
            if(self.bQuitter.draw() == "quitter"):
                son.stop()
                dead = True
                return "quitter"

            pygame.display.flip()
            self.clock.tick(clock_tick_rate)
