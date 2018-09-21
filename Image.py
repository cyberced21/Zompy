"""
    Classe representant une image dans le jeu Zompy
"""

class Image:
    """
        Attributs:
            String: path
        Methodes:
            getPath: Retourne le chemin de l'image
    """

    def __init__(self, path = ""):
        self.path = path

    def getPath(self):
        return self.path
