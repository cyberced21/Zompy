import pygame
from . import constantes

pygame.init()

fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
clock_tick_rate=20

son = pygame.mixer.Sound(constantes.sonMenuChemin)

imagePerso = ""

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


class SelectionPersonnage():

    def __init__(self):

        self.dead=False
        self.clock = pygame.time.Clock()
        self.background_image = constantes.fondMenu
        self.bPerso1 = Button("Selectionner",50,350,150,50,constantes.blue,constantes.bright_blue,"perso1")
        self.bPerso2 = Button("Selectionner",325,350,150,50,constantes.blue,constantes.bright_blue,"perso2")
        self.bPerso3 = Button("Selectionner",600,350,150,50,constantes.blue,constantes.bright_blue,"perso3")

    def run(self):
        son.play()
        while(self.dead==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.dead = True

            fenetre.blit(self.background_image, [0, 0])
            fenetre.blit(constantes.perso1,(85,250))
            fenetre.blit(constantes.perso2,(360,250))
            fenetre.blit(constantes.perso3,(635,250))


            #Texte du menu
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Choisir un Personnage", largeText)
            TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/4))
            fenetre.blit(TextSurf, TextRect)

            if(self.bPerso1.draw() == "perso1"):
                son.stop()
                dead = True
                #imagePerso = constantes.perso1
                return "perso1"
            if(self.bPerso2.draw() == "perso2"):
                son.stop()
                dead = True
                #imagePerso = constantes.perso2
                return "perso2"
            if(self.bPerso3.draw() == "perso3"):
                son.stop()
                dead = True
                #imagePerso = constantes.perso3
                return "perso3"

            pygame.display.flip()
            self.clock.tick(clock_tick_rate)
