"""
Classe representant un Personnage dans le jeu Zompy
"""

import os
import pygame
import random
from . import constantes
from . import equipments

class Personnage(pygame.sprite.Sprite):
    """
    Attributs:
       int: life
       Equipment[]: equipment
       Image : image  
       tuple : position
       String : name
    Methodes:
       move: Deplace le personnage
       attack: Attaque du personnage
       addEquipment: Ajoute un equipement a la liste d'equipements
       removeEquipment: Retire un equipement de la liste d'equipements
    """

    def __init__(self, name, life, equipments, image, position):
        """
        Constructeur par defaut du personnage
        """
        pygame.sprite.Sprite.__init__(self)
        self._name = name
        self._life = life
        self._equipments = equipments
        self.image = pygame.image.load(os.path.join(constantes.repertoire_images, "p1_jump.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self._position = position
        self.speedX = 0
        self.speedY = 0

    def update(self):
        pass

    @property
    def equipment(self):
        """
        >>> p = Hero()
        >>> p.addEquipment("a")
        >>> p.addEquipment("b")
        >>> p.equipment
        ['a', 'b']
        >>> p.removeEquipment()
        >>> p.equipment
        ['a']
        """
        return self._equipments

    def addEquipment(self, equipment):
        self._equipments.append(equipment)

    def removeEquipment(self):
        self._equipments.pop()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life):
        self._life = life

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, path):
        self._image = path

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    

"""
Classe representant un hero du jeu Zompy
"""

class Hero(Personnage):
    """
    Classe Hero heritant de Personnage
    """

    def __init__(self, name="Default", life=100, equipments=[], image="", position=(0, 0)):
        super().__init__(name, life, equipments, image, position)
        self.rect.centerx = constantes.LARGEUR / 2
        self.rect.bottom = constantes.HAUTEUR - 50

    def update(self):
        self.speedX = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedX = -5
        if keystate[pygame.K_d]:
            self.speedX = 5
        if keystate[pygame.K_w]:
            self.speedY = -5
        if keystate[pygame.K_s]:
            self.speedY = 5
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.right >= constantes.LARGEUR:
            self.rect.right = constantes.LARGEUR
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > constantes.HAUTEUR:
            self.rect.bottom = constantes.HAUTEUR

    def shoot(self):
        """
        Cree une balle et la retourne
        """
        balle = equipments.Bullet(self.rect.centerx, self.rect.top)
        return balle


"""
Classe representant un ennemi du jeu Zompy
"""

class Ennemi(Personnage):
    """
    Classe Ennemi heritant de Personnage
    """

    def __init__(self, name="Default", life=100, equipments=[], image="", position=(0, 0)):
        super().__init__(name, life, equipments, image, position)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(constantes.LARGEUR - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > constantes.HAUTEUR + 30 or self.rect.left < -25 or self.rect.right > constantes.LARGEUR + 20:
            self.rect.x = random.randrange(constantes.LARGEUR - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)