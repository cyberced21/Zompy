import pygame
import json
import operator
from ast import literal_eval
from pprint import pprint
from . import constantes
from pygame.locals import *
from operator import itemgetter

pygame.init()

fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
clock_tick_rate=20

def saisiNom():
    pygame.init()
    screen = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
    name = ""
    font = pygame.font.Font('freesansbold.ttf', 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    return name
                    False
            elif evt.type == QUIT:
                False
        screen.fill ((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Entrez votre nom", largeText)
        TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/4))
        screen.blit(TextSurf, TextRect)
        pygame.display.flip()

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


class Score():

    def __init__(self):

        self.dead=False
        self.clock = pygame.time.Clock()
        self.background_image = constantes.fondMenu
        
        self.bOk = Button("OK",700,500,50,50,constantes.blue,constantes.bright_blue,"ok")


    def afficherScore(self):

        score = []
        name = []
        json_data=open('score.json').read()
        data = literal_eval(json_data)

        for valeur in data["people"]:
            name.append(valeur.get("name"))
            score.append(valeur.get("score"))

        l = len(name)

        scorePasTrier = [[0]*2 for i in range(l)]
        scoreTrier = [[0]*2 for i in range(l)]

        i = 0;
        for valeur in name:
            scorePasTrier[i][0]=name[i]
            scorePasTrier[i][1]=score[i]
            i += 1

        scoreTrier = list(sorted(sorted(scorePasTrier, key=itemgetter(1)),key=itemgetter(1),reverse = True))

        while (len(scoreTrier)>10):
            if(len(scoreTrier)>10):
                scoreTrier.pop()
            else:
                False

        while(self.dead==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            fenetre.blit(self.background_image, [0, 0])

            #Texte du menu
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Score", largeText)
            TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/4))
            fenetre.blit(TextSurf, TextRect)
            
            x = 0
            i = 0
            #Affiche le nom
            for valeur in scoreTrier:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects(scoreTrier[i][0], largeText)
                TextRect.center = ((constantes.LARGEUR/4),(constantes.HAUTEUR/2+x))
                fenetre.blit(TextSurf, TextRect)
                x += 30
                i += 1
                
            x = 0
            i = 0
            #Affiche le score   
            for valeur in scoreTrier:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects(json.dumps(scoreTrier[i][1]), largeText)
                TextRect.center = ((constantes.LARGEUR/4+400),(constantes.HAUTEUR/2+x))
                fenetre.blit(TextSurf, TextRect)
                x += 30
                i += 1

            if(self.bOk.draw() == "ok"):
                dead = True
                return "ok"
        

            pygame.display.flip()
            self.clock.tick(clock_tick_rate)


    def ajouterScore(self, jscore):

        score = []
        name = []
        json_data=open('score.json').read()
        data = literal_eval(json_data)

        for valeur in data["people"]:
            name.append(valeur.get("name"))
            score.append(valeur.get("score"))

        l = len(name)

        scorePasTrier = [[0]*2 for i in range(l)]
        scoreTrier = [[0]*2 for i in range(l)]

        i = 0;
        for valeur in name:
            scorePasTrier[i][0]=name[i]
            scorePasTrier[i][1]=score[i]
            i += 1

        scoreTrier = list(sorted(sorted(scorePasTrier, key=itemgetter(1)),key=itemgetter(1),reverse = True))


        jnom = saisiNom()

        scorePasTrier.append([jnom,jscore])

        scoreTrier = list(sorted(sorted(scorePasTrier, key=itemgetter(1)),key=itemgetter(1),reverse = True))


        while (len(scoreTrier)>10):
            if(len(scoreTrier)>10):
                scoreTrier.pop()
            else:
                False

        while(self.dead==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            fenetre.blit(self.background_image, [0, 0])

            #Texte du menu
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Score", largeText)
            TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/4))
            fenetre.blit(TextSurf, TextRect)
            
            x = 0
            i = 0
            #Affiche le nom
            for valeur in scoreTrier:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects(scoreTrier[i][0], largeText)
                TextRect.center = ((constantes.LARGEUR/4),(constantes.HAUTEUR/2+x))
                fenetre.blit(TextSurf, TextRect)
                x += 30
                i += 1
                
            x = 0
            i = 0
            #Affiche le score   
            for valeur in scoreTrier:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects(json.dumps(scoreTrier[i][1]), largeText)
                TextRect.center = ((constantes.LARGEUR/4+400),(constantes.HAUTEUR/2+x))
                fenetre.blit(TextSurf, TextRect)
                x += 30
                i += 1

            if(self.bOk.draw() == "ok"):
                i = 0
                donnee = []
                for valeur in scoreTrier:
                     donnee.append(dict(name = scoreTrier[i][0], score = scoreTrier[i][1]))
                     i += 1

                print(donnee)
                donneeDict = dict(people=donnee)
                
                with open("score.json",'w') as f:
                    f.write(json.dumps(donneeDict))
                dead = True
                return "ok"
        

            pygame.display.flip()
            self.clock.tick(clock_tick_rate)
