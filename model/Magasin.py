from . import equipments
import pygame
import random
from . import constantes

class Crate(pygame.sprite.Sprite):
    """
    Represents a crate object which contains an equipment and has a set price
    """
    def __init__(self,price,equipment):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((215, 205, 145))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300
        self._equipment = equipment
        self._price = price

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self,new_equip):
        self._equipment = new_equip

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = new_price

    def buyCrate(self,money):
        if self._price <= money:
            return self._equipment
        raise ValueError("you dont have enough money")
