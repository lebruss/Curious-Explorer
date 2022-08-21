#to-do is in github commit history
#libraries
import time #for making the game "wait"
import random #for random numbers, choosing random name from a list, etc
import PySimpleGUI as SG #graphic user interface for making the game run in a window
import json #usd for save and load game data
#from locations import * #locations.py for game locations, their languages, culture etc
#functions
def clearScreen():#prints a looot of new lines to "clear" the terminal
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def mainMenu():#The game's main menu; user can navigate into and out of its options
    while True:
    #menu options
        clearScreen()
        print("Opportunities:\n")
        print("1. Check in with friends")#statistics of the player and their group of NPC friends
        print("2. Go somewhere")#travel
        print("3. What do we have?")#check inventory
        print("4. Socialize")#Try to meet another NPC in the current location
        print("5. Exit")#Exit the game completely
        print("- - - - -")
        menuChoice = input()

        #party stats
        if menuChoice == "1":
            clearScreen()
            print("Party stats: \n")
            for member in party:#for each Character in the party[] list, print their statistics with member.stats()
                member.stats()
            print("- - - - -")
            input("Press any key to continue.")

        #move - not functional, yet. map locations to neighboring locations?
        if menuChoice == "2":
            moveChoice = 0
            while moveChoice != "5":#Keep this menu open until the user chooses Option 5 for exiting the Move menu
                clearScreen()
                print("\n1. North")
                print("\n2. South")
                print("\n3. East")
                print("\n4. West")
                print("\n5. Stay put")
                print("- - - - -")
                moveChoice = input()

        #Inventory: show the Inventory item of each Character in the user's party[]
        if menuChoice == "3":
            clearScreen()
            print("Inventory:")
            for member in party:
                member.inventory()#print Inventory items in list for each party[] member
            input("Press any key to continue")
        
        #socialize - I want to depthen this one with chances, etc.
        if menuChoice == "4":
            clearScreen()
            print("Socialize")
            friend = Character(random.choice(first_names))#Create a new NPC character from "socializing" at this place
            party.append(friend)#add this new NPC character to your user party[]; they join your adventure
            time.sleep(random.randint(1,4))#wait, we are socializing
            print(friend.first_name + " has decided to tag along with y'all!")
            input("Press any key to stop socializing")
            #to-do: add some functionality about the player, or player's party, only able to welcome a new NPC if there is a common language

        #exit
        if menuChoice == "5":
            clearScreen()
            print("Goodbye!")
            time.sleep(1)
            break

#locations - Possible locations in the game, including the user's random starting location
location_list = ['Serbia', 'Albania', 'Helsingfors', 'Holy Roman Empire', 'the Hanseatic League', 'Prussia',
                 'Iceland', 'Tallinn', 'Estonia', 'Oklahoma', 'Colorado', 'Missouri', 'Viet Nam', 'Somalia', 'Prag', 'the Library',
                  'Scotland', 'Jõhvi', 'a cozy cave', 'the ocean', 'your family home', 'Corpus Cristi',
                   'Japanese Korea', 'the European Union', 'Helsinki', 'Jüri', 'Dagö', 'the Cherokee Nation', 'Haapsalu Castle', 'Greece',
                   'Iran', 'Iraq', 'Uzbekistan', 'Tajikistan', 'Samarkhand', 'Trondheim', 'Istanbul', 'Barcelona', 'Croatia',
                   'the Cyclades', 'Cyprus', 'Brazil', 'Angola', 'Kongo', 'Babylon', 'the River Styx', 'Tasmania', 'Viimsi', 'Hungary']                 
startLocation = random.choice(location_list)#User begins the game in a random location from the list

#names - possible names of Characters
first_names = ['Daniel', 'Dante', 'Borges', 'Lukas', 'Henri', 'Robert', 'Dalisa', 'Abdulhakim', 'Griffin', 'Cole', 'Jonsch', 'Jacob', 'Mark', 'Jackie', 'Martha', 'Rozhan', 'Gvantsa', 'Mati', 'Artur',
                'Gabriel', 'Tanya', 'Thanh', 'Tamar', 'Saba', 'Ngabo', 'Shpeta', 'Florian', 'Ott', 'Aili', 'Tom', 'Ann', 'Hans', 'Hayder',
                 'Valdimaar', 'Amadeus', 'Todd', 'Markko', 'Lil Al', 'Stefan', 'Klajd', 'Tonibler', 'Joonas', 'Peeter', 'Düüri',
                 'Arpad', 'Denis', 'Ädu', 'Vlad', 'Tristan', 'Hiroki', 'Bohdan', 'Stone', 'River', 'Harry', 'Jesse', 'Jason', 'Liam', 'Siim']
last_names = ['al Sharif', 'Hughes', 'Replogle', 'Thunderstone', 'Birdwatcher', 'Kivimägi', 'Khachapuridze', 'Kebabian', 'Russell', 'Janssen',
                'Gustafsson', 'Lepp', 'Cluff', 'Schröder', 'Pätt', 'Muzzini', 'Türi', 'Põder', 'Nemec', 'Pärt', 'Šuligoj', 'Salieri',
                 'Sarić', 'Đorđević', 'Smiljić', 'Pavlović Carevac', 'Čkalja', 'Nyary', 'Daniels', 'McClellan', 'Tostodoro',]

#conditions - mood / health attirbutes experienced by characters
conditions = ['tired', 'mad', 'angry', 'drunk', 'excited', 'happy', 'generous', 'wakeful', 'vengeful', 'ambitious', 'curious', 'creative',
                '', 'absentminded', 'sorrowful', 'ruminating', 'paralyzed', 'normal']

#Character template - user's and NPC's attributes, statistics, information about them used in the game
class Character:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = random.choice(last_names)
        self.x = 0
        self.y = 0
        self.money = 1
        self.level = 1
        self.age = random.randint(18, 90)#Character's age is between 18 and 90 years old
        self.possessions = ["clothes", "shoes"]#possessions[] is the Character's inventory
        self.languages = []#first language comes from Character's hometown; more can be added to list later during game
        self.hometown = random.choice(location_list)
        #self.hometown = (random.choice(locationList)).name
        self.condition = "normal"
    #show character stats
    def stats(self):
        print("----------" + str(self.first_name) + " " + str(self.last_name) + " from " + str(self.hometown))#e.g. Leb Jones from Tallinn
        #print("Location: (" + str(self.x) + "," + str(self.y) + ")")
        print("Money    : " + str(self.money))
        print("Level    : " + str(self.level))
        print("Age      : " + str(self.age) + " years old")
        print("Condition: " + str(self.condition))
        #return self.first_name, self.level

    #inventory
    def inventory(self):
        print("---------" + str(self.first_name) + " " + str(self.last_name))
        for item in self.possessions:#for each item in the character's possessions[] list, print it
            print(str(item))

    #add money to character
    def add_money(self, amount):
        self.money += amount

    #move() function; not in use yet.
    def move(self, move_x, move_y):
        x = self.x + move_x
        y = self.y + move_y
        #if (x < 0 or x > MAP_SIZE["x"] or y < 0 or y > MAP_SIZE["y"]):
            #print("YOU WILL FALL OFF THE FLAT EARTH! DONT GO THERE")
            #return
        #print("LETS SEE SOME MOVEMENT")
        #me.move(300, 200)
        #me.move(10000, 19292)
        self.x = x
        self.y = y
        print("NEW POSITION: ", self.x, self.y)


#year
year = random.randrange(700,2080,1)#Game year begins between 700 and 2080.

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
party.append(me)#add the user's character to the Party list of characters.
time.sleep(1)

#How many friends
while True:
    try:
        partysize = int(input("\nHow many friends are with you? "))
        break
    except ValueError:#if user doesn't enter a valid integer input for partysize variable, prompt the user until input is acceptable
        print("Please enter an integer so we can continue.")
time.sleep(1)
clearScreen()
#make party
for i in range(partysize):#create a user character party that is the size of partysize variable (including the user character me)
    friend = Character(random.choice(first_names))#generate a friend Character with a random first name.
    party.append(friend)

#Main Menu
mainMenu()
