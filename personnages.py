"""
Classe representant un Personnage dans le jeu Zompy
"""

from Image import Image

class Personnage():
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
        self._name = name
        self._life = life
        self._equipments = equipments
        self._image = image
        self._position = position
        super().__init__()

    @abstractmethod
    def move(self):
        """
        Methode abstraite qui deplace le personnage
        """
        raise NotImplementedError

    @abstractmethod
    def attack(self):
        """
        Methode abstraite qui fait attaquer le personnage
        """
        raise NotImplementedError

    @property
    def equipment(self):
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

    def __init__(self):
        super().__init__()

    def move(self):
        raise NotImplementedError

    def attack(self):
        raise NotImplementedError



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
            raise NotImplementedError

        def attack(self):
            raise NotImplementedError
