

import time #for making the game "wait"
import random #for random numbers, choosing random name from a list, etc
import PySimpleGUI as SG #graphic user interface for making the game run in a window
import json #used for save and load game data
import CEItems# items used in the game; CEItems.py

'''

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

'''

# Functions 
def clearScreen(): #prints a looot of new lines to "clear" the terminal
    print('\n'*30)

def mainMenu(): #The game's main menu; user can navigate into and out of its options
    while True:
    #menu options
        clearScreen()

        try:
            menuChoice = int(
                input(
                f'Opportunities:\n'
                f'1. Check in with friends\n' # Player and NPC friends statistics
                f'2. Go somewhere\n' # travel
                f'3. What do we have?\n' # inventory
                f'4. Socialize\n' # Try to meet another NPC in the current location
                f'5. Exit\n' # Exit the game completely
                f'- - - - -\n'
                ))
            time.sleep(2)

        except ValueError:
            print('- - - - -\nPlease try again with an integer.\n')
            menuChoice = 0   
            time.sleep(2)        

        #Check in with friends
        if menuChoice == 1:
            clearScreen()

            print("Party stats:")
            for member in party:# for each Character in party[] list, print stats
                member.stats()
                time.sleep(1)
            input("- - - - -\n'ENTER' to continue.\n")

        #Go somewhere
        if menuChoice == 2:
            moveChoice = 0

            #main menu for moving
            while moveChoice != "5":# exit this menu if input = 5
                clearScreen()

                # print character's coordinate and move choices
                try:
                    moveChoice = int(input(
                        f'{me.first_name} and the others are at: '
                        f'{me.myCoordinate.printCoordinate()}\n'
                        f'\n1. North\n'
                        f'2. South\n'
                        f'3. East\n'
                        f'4. West\n'
                        f'5. Stay put\n'
                        f'- - - - -\n'
                        ))
                    time.sleep(1) 

                except ValueError:
                    print('- - - - -\nPlease try again with an integer.\n')
                    time.sleep(2) 
                
                if moveChoice == 1: #move North
                    print("You move north.")
                    for player in party:
                        player.myCoordinate.y += 1
                    time.sleep(1)

                if moveChoice == 2: #move South
                    print("You move south.")
                    for player in party:
                        player.myCoordinate.y -= 1
                    time.sleep(1)

                if moveChoice == 3: #move East
                    print("You move east.")
                    for player in party:
                        player.myCoordinate.x += 1
                    time.sleep(1)

                if moveChoice == 4: #move West
                    print("You move west.")
                    for player in party:
                        player.myCoordinate.x -= 1
                    time.sleep(1)


        #Inventory: show the Inventory item of each Character in the user's party[]
        if menuChoice == 3:
            clearScreen()
            print("Inventory:")
            for member in party:
                member.inventory()#print Inventory items in list for each party[] member
            input("Press any key to continue")
        
        #socialize - Add a new randomized NPC to your party!
        if menuChoice == 4:
            clearScreen()
            print("Socializing...")
            friend = Character.Friend() # Create a new NPC character from "socializing" at this place
            friend.hometown = Location(random.choice(location_list))
            friend.languages.append(random.choice(friend.hometown.languages))
            friend.possessions.append(CEItems.Item(random.choice(CEItems.itemsList)))
            party.append(friend) # add this new NPC character to your user party[]; they join your adventure
            
            time.sleep(random.randint(1,4)) # wait, we are socializing
            
            print(friend.first_name + " has decided to tag along with y'all!")
            randomGiftChance = random.randint(1,10)
            
            if randomGiftChance > 5: # random gift from new friend
                randomGift = random.choice(CEItems.itemsList) # ift from NPC is a random item from itemsList in CEITEMS.py
                me.possessions.append(randomGift) # add the randomGift to the player's possessions[]
                print(friend.first_name + " gives you a token of appreciation!: " + str(randomGift.name))
                time.sleep(1)
            
            input("Press ENTER to continue")
            # to-do: add some functionality about the player, or player's party, only able to welcome a new NPC if there is a common language

        # exit
        if menuChoice == 5:
            clearScreen()
            print("Goodbye!")
            time.sleep(1)
            break

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printCoordinate(self):
        return f'(X: {self.x}, Y: {self.y})'


# Constants
party = [] # player party with self and NPCs
partysize = 1
year = random.randrange(700,2080,1) # Game year begins between 700 and 2080.
                
# Languages in the game. Used by locations and Characters
language_list = []
class Language:
    def __init__(self, name):
        self.name = name
        language_list.append(self.name)


location_list = []
class Location:
    # Parent class with default attributes
    # to work out self.capital

    def __init__(self):
        self.name = ""
        self.capital = Coordinate(0, 0)# gets assigned during the game
        self.languages = []
        self.forenames = []
        self.surnames = []
   
# Serbia        
class Serbia(Location):
    # Serbia child class

    def __init__(self):
        # inherits all parent class attributes
        super().__init__()

        # overwrites given attributes
        self.name = 'Serbia'
        self.Serbian = Language("Serbian")
        self.languages.append(self.Serbian)

# Albania
class Albania(Location):
    def __init__(self):
        super().__init__()
        self.name = 'Albania'
        self.Albanian = Language("Albanian")
        self.languages.append(self.Albanian)

# Helsingfors
class Helsingfors(Location):
    def __init__(self):
        super().__init__()
        self.name = 'Helsingfors'
        self.Swedish = Language("Swedish")
        self.Finnish = Language("Finnish")

        self.languages.append(self.Swedish)
        self.languages.append(self.Finnish)

# appends 
location_list.append(Serbia())
location_list.append(Albania())
location_list.append(Helsingfors())


# names - possible names of Characters
first_names = [
    'Daniel', 'Dante', 'Borges', 'Lukas', 'Henri', 'Robert', 
    'Dalisa', 'Abdulhakim', 'Griffin', 'Cole', 'Jonsch', 'Jacob', 
    'Mark', 'Jackie', 'Martha', 'Rozhan', 'Gvantsa', 'Mati', 
    'Artur', 'Gabriel', 'Tanya', 'Thanh', 'Tamar', 'Saba', 
    'Ngabo', 'Shpeta', 'Florian', 'Ott', 'Aili', 'Tom', 
    'Ann', 'Hans', 'Hayder', 'Valdimaar', 'Amadeus', 'Todd', 
    'Markko', 'Lil Al', 'Stefan', 'Klajd', 'Tonibler', 'Joonas', 
    'Peeter', 'Düüri', 'Arpad', 'Denis', 'Ädu', 'Vlad', 
    'Tristan', 'Hiroki', 'Bohdan', 'Stone', 'River', 'Harry', 
    'Jesse', 'Jason', 'Liam', 'Siim'
    ]

last_names = [
    'al Sharif', 'Hughes', 'Replogle', 'Thunderstone', 'Birdwatcher', 'Kivimägi', 
    'Khachapuridze', 'Kebabian', 'Russell', 'Janssen', 'Gustafsson', 'Lepp', 
    'Cluff', 'Schröder', 'Pätt', 'Muzzini', 'Türi', 'Põder', 
    'Nemec', 'Pärt', 'Šuligoj', 'Salieri', 'Sarić', 'Đorđević', 
    'Smiljić', 'Pavlović Carevac', 'Čkalja', 'Nyary', 'Daniels', 'McClellan', 
    'Tostodoro',
    ]

# conditions - mood / health attirbutes experienced by characters
conditions = [
    'tired', 'mad', 'angry', 'drunk', 'excited', 'happy', 
    'generous', 'wakeful', 'vengeful', 'ambitious', 'curious', 'creative', 
    '', 'absentminded', 'sorrowful', 'ruminating', 'paralyzed', 'normal'
    ]

startLocation = random.choice(location_list)
startLocation.capital = Coordinate(0,0)

# Character Class - user's and NPC's attributes, statistics, information about them used in the game
class Character:
    def __init__(self):
        self.first_name = ""
        self.last_name = random.choice(last_names)
        self.myCoordinate = Coordinate(0, 0)
        self.money = 1
        self.level = 1
        self.age = random.randint(18, 90) # Character's age is between 18 and 90 years old
        self.possessions = [] # possessions[] is the Character's inventory
        self.hometown = random.choice(location_list)
        self.languages = [] # first language comes from Character's hometown; more can be added to list later during game
        self.languages.append(random.choice(self.hometown.languages))
        self.condition = "normal"
    
    # show character stats
    def stats(self):
        ## e.g. Leb Jones from Tallinn
        # f'Location\t {self.x}, {self.y}'
        print(
            f'\n---------- {self.first_name} {self.last_name} from {self.hometown.name}\n'
            f'Money\t\t: {self.money}\n'
            f'Level\t\t: {self.level}\n'
            f'Age\t\t: {self.age} years old\n'
            f'Condition\t: {self.condition}\n'
            f'Languages\t: '
            )
        
        for language in self.languages:
            print(f'\t\t{language.name}')

    # inventory
    def inventory(self):
        print(f'--------- {self.first_name} {self.last_name}')
        for item in self.possessions: # for each item in the character's possessions[] list, print it
            print(str(item.name))

    # add money to character
    def add_money(self, amount):
        self.money += amount

# --- --- --- --- --- --- --- --- ---

# START
clearScreen()

print(f'- - - - -\nCurious Explorer\nby Caleb\n- - - - -')

time.sleep(1)

clearScreen()

print(f'Welcome to {startLocation.name}.')

time.sleep(1)

print(f'The year is {year}.')

time.sleep(1)

# Generate player's character using Character Class and first_name input.
me = Character()
me.first_name = input("What is your name, traveler?\n")
me.languages.append((random.choice(me.hometown.languages)))
me.hometown = startLocation
party.append(me) # add the user's character to the party[] list of characters.

time.sleep(1)

while True: # How many friends are with you?
    try:
        partysize = int(input("\nHow many friends are with you?\n"))
        time.sleep(2)
        break

    except ValueError: # if user doesn't enter a valid integer input for partysize variable, prompt the user until input is acceptable
        print("Please try again with an integer.")
        time.sleep(2)

    clearScreen()

# make party
for i in range(partysize): # create a user character party; size is partysize variable
    friend = Character()
    party.append(friend)

mainMenu() # run the main menu loop
