"""
	Module Equipments
"""

import pygame


class Equipment():

    def __init__(self, name, timelapse, image):
        """
		Constructeur de la classe Equipment
		"""
        self._name = name
        self._timelapse = timelapse
        self._image = image

    @property
    def name(self):
        print("fndui")
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def timelapse(self):
        return self._timelapse

    @timelapse.setter
    def timelapse(self, timelapse):
        self._timelapse = timelapse

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image


class Weapon(Equipment):
    """
	Classe Weapon representant un arme
	"""

    def __init__(self, name, timelapse, image, firePower):
        super().__init__(name, timelapse, image)
        self._firePower = firePower

    def attack(self):
        raise NotImplementedError


class DefaultPistol(Weapon):
    """
	Classe representant le pistolet par defaut pour les personnages
	"""

    def __init__(self, name="defaultEquipment", timelapse=100, image="", firePower=100):
        super().__init__(name, timelapse, image, firePower)

    def attack(self):
        raise NotImplementedError


class FlameThrower(Weapon):
    """
	Classe representant un lance flame utilises par les personnages
	"""

    def __init__(self, name="defaultEquipment", timelapse=100, image="", firePower=100):
        super().__init__(name, timelapse, image, firePower)

    def attack(self):
        raise NotImplementedError


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # On detruit si la balle est hors de la fenetre
        if self.rect.bottom < 0:
            self.kill()
