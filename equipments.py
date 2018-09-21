"""
    Module Equipments
"""

from abc import ABC
from Image import Image

class Equipment(ABC):
    """
    Classe abstraite equipment    
    """
    def __init__(self, name="defaultEquipment", timelapse=100, image=Image()):
        """
        Constructeur de la classe Equipment
        """
        self.name = name
        self.timelapse = timelapse
        self.image = image
        
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def timelapse(self):
        return self.timelapse

    @timelapse.setter
    def timelapse(self, timelapse):
        self.timelapse = timelapse

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, image):
        self.image = image




class Weapon(Equipment, ABC):
"""
Classe Weapon representant un arme
"""

    def __init__(self, name="defaultEquipment", timelapse=100, image=Image(), firePower=100):
        super(Weapon, self).__init__(name, timelapse, image)
        self.firePower = firePower 

    def attack(self):
        pass
