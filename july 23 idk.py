#To-do:
"""
Put the X,Y coordinates and Events with Locations back in
Save the game state / player's progress onto a file. maybe JSON
battle system
methods
certain character names give certain stats
items
inventory per player
maybe a GUI in tkinter where the game displays in a terminal, and within the same window there is a .png homemade art of the current location idk
"""
#libraries
import time, random

#locations
location_list = ['Serbia', 'Albania', 'Helsingfors', 'Holy Roman Empire', 'Hanseatic League', 'Prussia',
                 'Iceland', 'Tallinn', 'Estonia', 'Oklahoma', 'Colorado', 'Missouri', 'Viet Nam', 'Somalia', 'Prag', 'the Library']
location = random.choice(location_list)

#names
first_names = ['Daniel', 'Robert', 'Dalisa', 'Abdulhakim', 'Griffin', 'Cole', 'Jonsch', 'Jacob', 'Mark', 'Jackie', 'Martha', 'Rozhan', 'გვანცა', 'Mati', 'Artur',
                'Gabriel', 'Tanya', 'თამარ', 'საბა', 'Ngabo', 'Shpeta', 'Florian', 'Ott', 'Aili', 'Tom', 'Ann', 'Hans', 'Hayder']
last_names = ['al Sharif', 'Hughes', 'Replogle', 'Thunderstone', 'Birdwatcher', 'Kivimägi', 'ხაჭაპურიძე']
#Character template - players and NPCs
class Character:
    def __init__(self, name, x, y, money, level):
        self.name = "name"
        self.x = 0
        self.y = 0
        self.money = 1
        self.level = 1

#year
year = random.randrange(700,2080,1)


#welcome
print("Welcome to " + location + ".\n" + "Thank you for being here!\n\n\n")
#time.sleep(2)
print("The year is " + str(year) + ".")

#start
me = Character("name", 0, 0, 1, 1)
me.name = input("What is your name, traveler?")
#print(me.name)
#time.sleep(5)

#name / character generation
i = 1
while True:
    #NPC_name = random.choice(first_names) + random.choice(last_names)
    print(i)
    print(random.choice(first_names))
    print(random.choice(last_names))
    i += 1
    time.sleep(2)