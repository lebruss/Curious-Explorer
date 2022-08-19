#To-do:
#       x, y coordinates
#libraries
import time, random

#functions
def clearScreen():#"CLEAR" TERMINAL SCREEN
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def mainMenu():#MAIN MENU LOOP
    while True:
    #menu options
        clearScreen()
        print("Opportunities:\n")
        print("1. Check in with friends")
        print("2. Go somewhere")
        print("3. What do we have?")
        print("4. Socialize")
        print("5. Exit")
        print("- - - - -")
        menuChoice = input()

        #party stats
        if menuChoice == "1":
            clearScreen()
            print("Party stats: \n")
            for member in party:
                member.stats()
            print("- - - - -")
            input("Press any key to continue.")

        #move - not functional, yet. map locations to neighboring locations?
        if menuChoice == "2":
            moveChoice = 0
            while moveChoice != "5":
                clearScreen()
                print("\n1. North")
                print("\n2. South")
                print("\n3. East")
                print("\n4. West")
                print("\n5. Stay put")
                print("- - - - -")
                moveChoice = input()

        #inventory
        if menuChoice == "3":
            clearScreen()
            print("Inventory:")
            for member in party:
                member.inventory()
            input("Press any key to continue")
        
        #socialize
        if menuChoice == "4":
            clearScreen()
            print("Socialize")
            friend = Character(random.choice(first_names))
            party.append(friend)
            input("Press any key to stop socializing")

        #exit
        if menuChoice == "5":
            clearScreen()
            print("Goodbye!")
            time.sleep(1)
            break

#locations
location_list = ['Serbia', 'Albania', 'Helsingfors', 'Holy Roman Empire', 'the Hanseatic League', 'Prussia',
                 'Iceland', 'Tallinn', 'Estonia', 'Oklahoma', 'Colorado', 'Missouri', 'Viet Nam', 'Somalia', 'Prag', 'the Library',
                  'Scotland', 'Jõhvi', 'a cozy cave', 'the ocean', 'your family home', 'Corpus Cristi',
                   'Japanese Korea', 'the European Union', 'Helsinki', 'Jüri', 'Dagö', 'the Cherokee Nation', 'Haapsalu Castle', 'Greece',
                   'Iran', 'Iraq', 'Uzbekistan', 'Tajikistan', 'Samarkhand', 'Trondheim', 'Istanbul', 'Barcelona', 'Croatia',
                   'the Cyclades', 'Cyprus', 'Brazil', 'Angola', 'Kongo', 'Babylon', 'the River Styx', 'Tasmania', 'Viimsi', 'Hungary']                 
startLocation = random.choice(location_list)
# dict.items() -> [(Serbia, (0, 0)),]
# dict.keys() -> [Serbia, Albania, ...]
# dict.values() -> [(0, 0), (10,10), ...]

#names
first_names = ['Daniel', 'Dante', 'Borges', 'Lukas', 'Henri', 'Robert', 'Dalisa', 'Abdulhakim', 'Griffin', 'Cole', 'Jonsch', 'Jacob', 'Mark', 'Jackie', 'Martha', 'Rozhan', 'Gvantsa', 'Mati', 'Artur',
                'Gabriel', 'Tanya', 'Thanh', 'Tamar', 'Saba', 'Ngabo', 'Shpeta', 'Florian', 'Ott', 'Aili', 'Tom', 'Ann', 'Hans', 'Hayder',
                 'Valdimaar', 'Amadeus', 'Todd', 'Markko', 'Lil Al', 'Stefan', 'Klajd', 'Tonibler', 'Joonas', 'Peeter', 'Düüri',
                 'Arpad', 'Denis', 'Ädu', 'Vlad', 'Tristan', 'Hiroki', 'Bohdan', 'Stone', 'River', 'Harry', 'Jesse', 'Jason', 'Liam', 'Siim']
last_names = ['al Sharif', 'Hughes', 'Replogle', 'Thunderstone', 'Birdwatcher', 'Kivimägi', 'Khachapuridze', 'Kebabian', 'Russell', 'Janssen',
                'Gustafsson', 'Lepp', 'Cluff', 'Schröder', 'Pätt', 'Muzzini', 'Türi', 'Põder', 'Nemec', 'Pärt', 'Šuligoj', 'Salieri',
                 'Sarić', 'Đorđević', 'Smiljić', 'Pavlović Carevac', 'Čkalja', 'Nyary', 'Daniels', 'McClellan', 'Tostodoro',]

#MAP_SIZE = {"x": 1000, "y": 1000}

#conditions
conditions = ['tired', 'mad', 'angry', 'drunk', 'excited', 'happy', 'generous', 'wakeful', 'vengeful', 'ambitious', 'curious', 'creative',
                '', 'absentminded', 'sorrowful', 'ruminating', 'paralyzed']

#Character template - players and NPCs
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = random.choice(last_names)
        self.x = 0
        self.y = 0
        self.money = 1
        self.level = 1
        self.age = random.randint(18, 90)
        self.possessions = ["clothes", "shoes"]
        self.languages = []
        self.hometown = random.choice(location_list)
        self.condition = random.choice(conditions)
    #show character stats
    def stats(self):
        print("----------" + str(self.first_name) + " " + str(self.last_name) + " from " + str(self.hometown))
        #print("Location: (" + str(self.x) + "," + str(self.y) + ")")
        print("Money    : " + str(self.money))
        print("Level    : " + str(self.level))
        print("Age      : " + str(self.age) + " years old")
        print("Condition: " + str(self.condition))
        #return self.first_name, self.level

    #inventory
    def inventory(self):
        print("---------" + str(self.first_name) + " " + str(self.last_name))
        for item in self.possessions:
            print(str(item))

    #add money to character
    def add_money(self, amount):
        self.money += amount

    #not in use at the moment    
    def move(self, move_x, move_y):
        x = self.x + move_x
        y = self.y + move_y
        #if (x < 0 or x > MAP_SIZE["x"] or y < 0 or y > MAP_SIZE["y"]):
            #print("YOU WILL FALL OFF THE FLAT EARTH! DONT GO THERE")
            #return
        
        self.x = x
        self.y = y
        print("NEW POSITION: ", self.x, self.y)

#year
year = random.randrange(700,2080,1)

#start
clearScreen()
print("- - - - -")
print("Curious Explorer, by Caleb")
print("- - - - -")
time.sleep(2)
clearScreen()
print("Welcome to " + startLocation + ".")
time.sleep(1)
print("The year is " + str(year) + ".")
time.sleep(2)
first_name = input("What is your name, traveler?\n")
me = Character(first_name)
party = []
party.append(me)
time.sleep(1)

#How many friends
while True:
    try:
        partysize = int(input("\nHow many friends are with you? "))
        break
    except ValueError:
        print("Please enter an integer so we can continue.")
time.sleep(1)
clearScreen()
#make party
for i in range(partysize):
    friend = Character(random.choice(first_names))
    party.append(friend)
    

#print an example Character with all stats
#me.stats()

#move
#print("LETS SEE SOME MOVEMENT")
#me.move(300, 200)
#me.move(10000, 19292)


#Main Menu
mainMenu()