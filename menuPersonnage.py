import pygame
from model import constantes

pygame.init()


fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
clock_tick_rate=20

son = pygame.mixer.Sound(constantes.sonMenuChemin)


def text_objects(text, font):
    textSurface = font.render(text, True, constantes.white)
    return textSurface, textSurface.get_rect()


class button():
    
    def __init__(self,msg,x,y,w,h,ic,ac,action=None):
            
        #msg: What do you want the button to say on it.

        #x: The x location of the top left coordinate of the button box.

        #y: The y location of the top left coordinate of the button box.

        #w: Button width.

        #h: Button height.

        #ic: Inactive color (when a mouse is not hovering).

        #ac: Active color (when a mouse is hovering).

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(fenetre, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(fenetre, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        fenetre.blit(textSurf, textRect)


def game_loop():
        
    print("Hello world")
    

def game_score():
        
    print("Score de joueur")
    

def quitgame():
    pygame.quit()
    quit()


class Menu():

    def __init__(self):

        dead=False
        #fenetre = pygame.display.set_mode((constantes.LARGEUR, constantes.HAUTEUR))
        clock = pygame.time.Clock()
        background_image = constantes.fondMenu
        #constantes.sonMenu.play()
        son.play()
        

        while(dead==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True

            fenetre.blit(background_image, [0, 0])

            #Texte du menu
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects("Choisir un Personnage", largeText)
            TextRect.center = ((constantes.LARGEUR/2),(constantes.HAUTEUR/4))
            fenetre.blit(TextSurf, TextRect)

            fenetre.blit(constantes.perso1,(85,250))
            button("Selectionner",50,450,150,50,constantes.blue,constantes.bright_blue,game_loop)
            fenetre.blit(constantes.perso2,(360,250))
            button("Selectionner",325,450,150,50,constantes.blue,constantes.bright_blue,game_score)
            fenetre.blit(constantes.perso3,(635,250))
            button("Selectionner",600,450,150,50,constantes.blue,constantes.bright_blue,quitgame)

            pygame.display.flip()
            clock.tick(clock_tick_rate)



print("Salut")
Menu()
pygame.quit()
quit()
