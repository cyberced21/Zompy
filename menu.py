# import pygame
import pygame

img = pygame.image.load("image\pixel_space.png")
img = pygame.transform.scale(img, (800, 600))

# initialize game engine
pygame.init()

window_width=800
window_height=600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (30,144,255)


animation_increment=10
clock_tick_rate=20

son = pygame.mixer.Sound("pixel-adenture.wav")

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("ZompyMenu")


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    
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
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_intro():
    dead=False

    clock = pygame.time.Clock()
    background_image = img
    son.play()
    

    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        #Texte du menu
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("SpacePy", largeText)
        TextRect.center = ((window_width/2),(window_height/2))
        screen.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Score",350,450,100,50,blue,bright_blue,game_score)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.flip()
        clock.tick(clock_tick_rate)

def game_loop():
    
    print("Hello world")

def game_score():
    
    print("Score de joueur")

def quitgame():
    pygame.quit()
    quit()
    #print("Fermer le jeu")

game_intro()
pygame.quit()
quit()
