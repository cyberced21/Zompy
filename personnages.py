"""
Classe abstraite representant un Personnage dans le jeu Zompy
"""

from abc import ABC, abstractmethod
from Image import Image

class Personnage(ABC):
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

    def __init__(self, name="Default", life=100, equipments=[], image=Image(), position=(0, 0)):
        """
        Constructeur par defaut du personnage
        """
        self.name = name
        self.life = life
        self.equipments = equipments
        self.image = image
        self.position = position
        super().__init__()

    @abstractmethod
    def move(self):
        """
        Methode abstraite qui deplace le personnage
        """
        pass

    @abstractmethod
    def attack(self):
        """
        Methode abstraite qui fait attaquer le personnage
        """
        pass

    def addEquipment(self, equipment):
        self.equipments.append(equipment)
    
    def removeEquipment(self):
        self.equipments.pop()

    def getEquipment(self):
        return self.equipments



"""
Classe representant un hero du jeu Zompy
"""

class Hero(Personnage):
    """
    Classe Hero heritant de Personnage
    """

    def __init__(self):
        super().__init__()

    def move(self):
        pass

    def attack(self):
        pass



"""
Classe representant un ennemi du jeu Zompy
"""

class Ennemi(Personnage):
    """
    Classe Ennemi heritant de Personnage
    """

    def __init__(self):
        super().__init__()

        def move(self):
            pass

        def attack(self):
            pass
