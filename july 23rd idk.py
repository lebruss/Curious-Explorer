#To-do:
#       x, y coordinates
#libraries
import time, random
party = []
#locations
location_list = ['Serbia', 'Albania', 'Helsingfors', 'Holy Roman Empire', 'Hanseatic League', 'Prussia',
                 'Iceland', 'Tallinn', 'Estonia', 'Oklahoma', 'Colorado', 'Missouri', 'Viet Nam', 'Somalia', 'Prag', 'the Library']
                 

# dict.items() -> [(Serbia, (0, 0)),]
# dict.keys() -> [Serbia, Albania, ...]
# dict.values() -> [(0, 0), (10,10), ...]

location = random.choice(location_list)

#names
first_names = ['Daniel', 'Robert', 'Dalisa', 'Abdulhakim', 'Griffin', 'Cole', 'Jonsch', 'Jacob', 'Mark', 'Jackie', 'Martha', 'Rozhan', 'გვანცა', 'Mati', 'Artur',
                'Gabriel', 'Tanya', 'თამარ', 'საბა', 'Ngabo', 'Shpeta', 'Florian', 'Ott', 'Aili', 'Tom', 'Ann', 'Hans', 'Hayder']
last_names = ['al Sharif', 'Hughes', 'Replogle', 'Thunderstone', 'Birdwatcher', 'Kivimägi', 'ხაჭაპურიძე']

MAP_SIZE = {"x": 1000, "y": 1000}


#Character template - players and NPCs
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = random.choice(last_names)
        self.x = 0
        self.y = 0
        self.money = 1
        self.level = 1

    #show character stats
    def stats(self):
        print("Name: " + str(self.first_name) + " " + str(self.last_name))
        print("Position: (" + str(self.x) + "," + str(self.y) + ")")
        print("Money: " + str(self.money))
        print("Level: " + str(self.level))
        #return self.first_name, self.level
        
    def add_money(self, amount):
        self.money += amount
        
    def move(self, move_x, move_y):
        x = self.x + move_x
        y = self.y + move_y
        if (x < 0 or x > MAP_SIZE["x"] or y < 0 or y > MAP_SIZE["y"]):
            print("YOU WILL FALL OFF THE FLAT EARTH! DONT GO THERE")
            return
        
        self.x = x
        self.y = y
        print("NEW POSITION: ", self.x, self.y)

#year
year = random.randrange(700,2080,1)

#welcome
print("Welcome to " + location + ".\n" + "Thank you for being here!\n\n\n")
#time.sleep(2)
print("The year is " + str(year) + ".")

#start

first_name = input("What is your name, traveler?\n")
me = Character(first_name)
me.add_money(90000)
party.append(me)
time.sleep(1)
partysize = input("\nHow many friends are with you? ")#change this to only accept integer
partysize = int(partysize) + 1
time.sleep(1)

#make party
for i in range(partysize):
    friend = Character(random.choice(first_names))
    party.append(friend)
    

#print an example Character with all stats
me.stats()

print("LETS SEE SOME MOVEMENT")
me.move(300, 200)
me.move(10000, 19292)


#Main Menu
while True:
    #menu options
    print("\n1 Stats.")
    print("\n2. Move")
    print("\n3.")
    print("\n4.")
    print("\n5.")
    print("- - - - -")
    menuChoice = input()
    
    #party stats
    if menuChoice == "1":
        for member in party:
            member.stats()
        print("- - - - -")
    #move
    if menuChoice == "2":
        moveChoice = 0
        while moveChoice != "5":
            print("\n1. North")
            print("\n2. South")
            print("\n3. East")
            print("\n4. West")
            print("\n5. Stay put")
            print("- - - - -")
            moveChoice = input()