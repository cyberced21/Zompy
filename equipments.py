"""
    Module Equipments
"""

from Image import Image

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
        raise NotImplementedException()

class DefaultPistol(Weapon):
    """
    Classe representant le pistolet par defaut pour les personnages
    """
    def __init__(self, name="defaultEquipment", timelapse=100, image=Image(), firePower=100):
        super().__init__(name, timelapse, image, firePower)

    def attack(self):
        raise NotImplementedException()


class FlameThrower(Weapon):
    """
    Classe representant un lance flame utilises par les personnages
    """
    def __init__(self, name="defaultEquipment", timelapse=100, image=Image(), firePower=100):
        super().__init__(name, timelapse, image, firePower)

    def attack(self):
        raise NotImplementedException()
