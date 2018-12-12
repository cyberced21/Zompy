

if __name__ == "__main__" or __name__ == "Magasin":
    import equipments
    import pygame
    import constantes
    import random
else:
    from . import equipments
    from . import constantes
    import random
    import pygame

class Crate(pygame.sprite.Sprite):
    """
    Represents a crate object which contains an equipment and has a set price
    """
    def __init__(self,price,equipment):
        pygame.sprite.Sprite.__init__(self)
        self.image = constantes.crate_canon
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300
        self._equipment = equipment
        self._price = price

    @property
    def equipment(self):
        """
        Faite par cedrik blais

        >>> lol=Crate(12,equipments.DefaultPistol())
        >>> lol.equipment.name
        'Default Pistol'
        """
        return self._equipment

    @equipment.setter
    def equipment(self,new_equip):
        self._equipment = new_equip

    @property
    def price(self):
        """
        Faite par cedrik blais

        >>> lol=Crate(12,equipments.DefaultPistol())
        >>> lol.price
        12
        """
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = new_price

    def buyCrate(self,money):
        """
        Faite par cedrik blais

        >>> lol=Crate(12,equipments.DefaultPistol())
        >>> buy_equip = lol.buyCrate(20)
        >>> buy_equip.name
        'Default Pistol'
        >>> lol.buyCrate(5)
        Traceback (most recent call last):
            File "Magasin.py", line 52, in <module>
                print(lol.buyCrate(5).name)
            File "Magasin.py", line 47, in buyCrate
            raise ValueError("you dont have enough money")
        ValueError: you dont have enough money
        """
        if self._price <= money:
            return self._equipment
        raise ValueError("you dont have enough money")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
