##################################################
# Fichier contenant toutes les constantes du jeu #
##################################################

import os

LARGEUR = 1000
HAUTEUR = 700
FPS = 60

# Chemin du repertoire du jeu
repertoire_jeu = os.path.join(os.path.dirname(__file__), os.pardir)

# Chemin du repertoire des images
repertoire_images = os.path.join(repertoire_jeu, "image")

# Vitesse de rotation du joueur
VITESSE_ROTATION = 50