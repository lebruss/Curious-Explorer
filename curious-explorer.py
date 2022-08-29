#to-do is in github commit history
#import python libraries and other files from Curious Explorer directory
import time #for making the game "wait"
import random #for random numbers, choosing random name from a list, etc
import PySimpleGUI as SG #graphic user interface for making the game run in a window
import json #used for save and load game data
import CEItems# items used in the game; CEItems.py
'''IDK how to do splash screens yet
from PIL import Image#for opening photo files
splashScreen = Image.open('art1.png')
splashScreen.show()
time.sleep(1)
splashScreen.close()
'''
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

        #Check in with friends
        if menuChoice == "1":
            clearScreen()
            print("Party stats: \n")
            for member in party:#for each Character in the party[] list, print their statistics with member.stats()
                member.stats()
                time.sleep(1)
            print("- - - - -")
            input("Press any key to continue.")

        #Go somewhere
        if menuChoice == "2":
            moveChoice = 0
            while moveChoice != "5":#exit this menu if input = 5
                clearScreen()
                #main menu for moving
                print(me.first_name + " and the others are at: " + str(me.myCoordinate.printCoordinate()))#print character's coordinate
                print("\n1. North")
                print("\n2. South")
                print("\n3. East")
                print("\n4. West")
                print("\n5. Stay put")
                print("- - - - -")
                moveChoice = input()
                if str(moveChoice) =="1":#move North
                    print("You move north.")
                    for player in party:
                        player.myCoordinate.y = player.myCoordinate.y + 1
                    time.sleep(1)
                if str(moveChoice) =="2":#move South
                    print("You move south.")
                    for player in party:
                        player.myCoordinate.y = player.myCoordinate.y - 1
                    time.sleep(1)
                if str(moveChoice) =="3":#move East
                    print("You move east.")
                    for player in party:
                        player.myCoordinate.x = player.myCoordinate.x + 1
                    time.sleep(1)
                if str(moveChoice) =="4":#move West
                    print("You move west.")
                    for player in party:
                        player.myCoordinate.x = player.myCoordinate.x - 1
                    time.sleep(1)

        #Inventory: show the Inventory item of each Character in the user's party[]
        if menuChoice == "3":
            clearScreen()
            print("Inventory:")
            for member in party:
                member.inventory()#print Inventory items in list for each party[] member
            input("Press any key to continue")
        
        #socialize - Add a new randomized NPC to your party!
        if menuChoice == "4":
            clearScreen()
            print("Socializing...")
            friend = Character.Friend()#Create a new NPC character from "socializing" at this place
            friend.hometown = Location(random.choice(location_list))
            friend.languages.append(random.choice(friend.hometown.languages))
            friend.possessions.append(CEItems.Item(random.choice(CEItems.itemsList)))
            party.append(friend)#add this new NPC character to your user party[]; they join your adventure
            time.sleep(random.randint(1,4))#wait, we are socializing
            print(friend.first_name + " has decided to tag along with y'all!")
            randomGiftChance = random.randint(1,10)
            if randomGiftChance > 5:#random gift from new friend
                randomGift = random.choice(CEItems.itemsList)#gift from NPC is a random item from itemsList in CEITEMS.py
                me.possessions.append(randomGift)#add the randomGift to the player's possessions[]
                print(friend.first_name + " gives you a token of appreciation!: " + str(randomGift.name))
                time.sleep(1)
            input("Press ENTER to continue")
            #to-do: add some functionality about the player, or player's party, only able to welcome a new NPC if there is a common language

        #exit
        if menuChoice == "5":
            clearScreen()
            print("Goodbye!")
            time.sleep(1)
            break

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printCoordinate(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")


#Constants
party = []#player party with self and NPCs
partysize = 1
year = random.randrange(700,2080,1)#Game year begins between 700 and 2080.
                
#Languages in the game. Used by locations and Characters
language_list = []
class Language:
    def __init__(self, name):
        self.name = name
        language_list.append(self)

location_list = []
class Location:
    name = ""
    capital = Coordinate(0, 0)#gets assigned during the game
    languages = []
    forenames = []
    surnames = []
    def __init__(self):
        location_list.append(self)


#Serbia
Serbia = Location()
Serbia.name = "Serbia"
Serbian = Language("Serbian")
Serbia.languages.append(Serbian)

#Albania
Albania = Location()
Albania.name = "Albania"
Albanian = Language("Albanian")
Albania.languages.append(Albanian)

#Helsingfors
Helsingfors = Location()
Helsingfors.name = "Helsingfors"
Swedish = Language("Swedish")
Helsingfors.languages.append(Swedish)
Finnish = Language("Finnish")
Helsingfors.languages.append(Finnish)

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

startLocation = random.choice(location_list)
startLocation.capital = Coordinate(0,0)

#Character Class - user's and NPC's attributes, statistics, information about them used in the game
class Character:
    def __init__(self):
        self.first_name = ""
        self.last_name = random.choice(last_names)
        self.myCoordinate = Coordinate(0, 0)
        self.money = 1
        self.level = 1
        self.age = random.randint(18, 90)#Character's age is between 18 and 90 years old
        self.possessions = []#possessions[] is the Character's inventory
        self.hometown = random.choice(location_list)
        self.languages = []#first language comes from Character's hometown; more can be added to list later during game
        self.languages.append(Language(random.choice(self.hometown.languages)))
        self.condition = "normal"
    #show character stats
    def stats(self):
        print("----------" + str(self.first_name) + " " + str(self.last_name) + " from " + str(self.hometown.name))#e.g. Leb Jones from Tallinn
        #print("Location: (" + str(self.x) + "," + str(self.y) + ")")
        print("Money    : " + str(self.money))
        print("Level    : " + str(self.level))
        print("Age      : " + str(self.age) + " years old")
        print("Condition: " + str(self.condition))
        print("Languages: ")
        for language in self.languages:
            print(str(language.name))

    #inventory
    def inventory(self):
        print("---------" + str(self.first_name) + " " + str(self.last_name))
        for item in self.possessions:#for each item in the character's possessions[] list, print it
            print(str(item.name))

    #add money to character
    def add_money(self, amount):
        self.money += amount

    #move() function; not in use yet. am working on Coordinate class instead.
    def move(self, move_x, move_y):
        x = self.x + move_x
        y = self.y + move_y
        self.x = x
        self.y = y
        print("NEW POSITION: ", self.x, self.y)

    class Friend():
        friendliness = 1#filler variable. not sure how I'll use this NPC class yet
        def __init__(self):
            self.first_name = random.choice(first_names)
            self.last_name = random.choice(last_names)
            self.hometown = random.choice(location_list)
        
#start
clearScreen()
print("- - - - -")
print("Curious Explorer, by Caleb")
print("- - - - -")
time.sleep(2)
clearScreen()
print("Welcome to " + str(startLocation.name) + ".")
time.sleep(1)
print("The year is " + str(year) + ".")
time.sleep(2)
me = Character()#Generate player's character using Character Class and first_name input.
me.first_name = input("What is your name, traveler?\n")
me.languages.append((random.choice(me.hometown.languages)))
me.hometown = startLocation
party.append(me)#add the user's character to the party[] list of characters.
time.sleep(1)
while True:#How many friends are with you?
    try:
        partysize = int(input("\nHow many friends are with you? "))
    except ValueError:#if user doesn't enter a valid integer input for partysize variable, prompt the user until input is acceptable
        print("Please try again with an integer.")
    clearScreen()
    #make party
    for i in range(partysize):#create a user character party; size is partysize variable
        friend = Character.Friend()
        party.append(Character.Friend())
    break

mainMenu()#run the main menu loop
