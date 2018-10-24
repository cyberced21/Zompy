"""
 Classe representrant un niveau dans le jeu Zompy
"""

from model import personnages

class Niveau():
    def __init__(self, nbEnnemis):
        self.ennemis = []
        self.nbEnnemis = nbEnnemis

    def get_listeEnnemis(self):
        return self.ennemis

    def start(self):
        for i in range(self.nbEnnemis):
            self.ennemis.append(personnages.Ennemi())

    def stop(self):
        return NotImplementedError
