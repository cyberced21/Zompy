"""
 Classe representrant un niveau dans le jeu Zompy
"""

if __name__ == "__main__":
    import os
    import pygame
    import personnages
    import partie
    import constantes

else:

    from model import personnages

class Niveau():
    def __init__(self, nbEnnemis):
        self.ennemis = []
        self.nbEnnemis = nbEnnemis

    def get_listeEnnemis(self):
        """
        Tests par Samuel

        >>> a=Niveau(0)
        >>> a.get_listeEnnemis()
        []
        >>> b=Niveau(5)
        >>> b.start()
        >>> b.get_listeEnnemis()
        [<Ennemi sprite(in 0 groups)>, <Ennemi sprite(in 0 groups)>, <Ennemi sprite(in 0 groups)>, <Ennemi sprite(in 0 groups)>, <Ennemi sprite(in 0 groups)>]
        >>> c=Niveau(-1)
        >>> c.get_listeEnnemis()
        []
        """
        return self.ennemis

    def start(self):
        for i in range(self.nbEnnemis):
            self.ennemis.append(personnages.Ennemi())

    def stop(self):
        return NotImplementedError

if __name__ == "__main__":
    import doctest
    doctest.testmod()
