
# items
def printHi():
    print("Hi")
    input()


itemsList = []  # list of game items
weaponsList = []  # list of game weapons
clothesList = []  # list of wearable items


class Item:
    def __init__(self, name):
        self.name = name
        itemsList.append(self)  # add the item to the itemsList[]

    class Weapon:
        def __init__(self, name, power, isMelee, isRanged):
            self.name = name
            self.power = power
            self.isMelee = False
            self.isRanged = False
            weaponsList.append(self)

    class Clothing:
        def __init__(self, name, power):
            self.name = name
            self.power = power
            self.coldResistance = 1
            self.fashionrating = 1
            clothesList.append(self)


BlackShoes = Item.Clothing("black shoes", 1)

Sword = Item.Weapon("sword", 5, True, False)

Paper = Item("paper")

Ink = Item("ink")

Dagger = Item.Weapon("dagger", 3, True, False)

Crossbow = Item.Weapon("crossbow", 3, False, True)
