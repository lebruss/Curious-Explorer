#items
def printHi():
    print("Hi")
    input()

itemsList = []#list of game items

class Item:
    def __init__(self, name):
        self.name = name
        itemsList.append(self)#add the item to the itemsList[]

BlackShoes = Item("black shoes")

Sword = Item("sword")

Paper = Item("paper")

Ink = Item("ink")

