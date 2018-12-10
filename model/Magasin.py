import equipments

class Magasin():
    """
    Reprensente un magasin, qui va contenir les crate qui permettent d'acheter des choses
    """
    def __init__(self,crate_list):
        self._crate_list = crate_list

class Crate():
    """
    Represents a crate object which contains an equipment and has a set price
    """
    def __init__(self,price,equipment):
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
        if self._price <= money
            return self._equipment
        raise ValueError("you dont have enough money")

    
