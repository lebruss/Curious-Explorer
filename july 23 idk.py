#To-do:
#       x, y coordinates
#libraries
import time, random
party = []
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
    def __init__(self):
        self.first_name = random.choice(first_names)
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

#year
year = random.randrange(700,2080,1)

#welcome
print("Welcome to " + location + ".\n" + "Thank you for being here!\n\n\n")
#time.sleep(2)
print("The year is " + str(year) + ".")

#start
me = Character()
me.first_name = input("What is your name, traveler?\n")
party.append(me)
time.sleep(1)
partysize = input("\nHow many friends are with you? ")#change this to only accept integer
partysize = int(partysize) + 1
time.sleep(1)

#make party
i = 1
while i < partysize:
    friend = Character()
    party.append(Character)
    i = i + 1

#print an example Character with all stats
stats(me)

input()