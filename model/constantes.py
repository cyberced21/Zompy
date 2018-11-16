##################################################
# Fichier contenant toutes les constantes du jeu #
##################################################
import pygame
import os

LARGEUR = 800
HAUTEUR = 600
FPS = 60

# Chemin du repertoire du jeu
repertoire_jeu = os.path.join(os.path.dirname(__file__), os.pardir)

# Chemin du repertoire des images
repertoire_images = os.path.join(repertoire_jeu, "image")

# Chemin du repertoire des sons
repertoire_son = os.path.join(repertoire_jeu, "son")

# Mise en place de l'image du menu
fondMenuChemin = os.path.join(repertoire_images, "pixel_space.png")
fondMenu = pygame.image.load(fondMenuChemin)
fondMenu = pygame.transform.scale(fondMenu, (LARGEUR, HAUTEUR))

# Couleurs
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (30,144,255)

# Son
sonMenuChemin = os.path.join(repertoire_son, "pixel-adenture.wav")
#sonMenu = pygame.mixer.Sound(sonMenuChemin)
