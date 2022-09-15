import time  # for making the game "wait"
import random  # for random numbers, choosing random name from a list, etc
import PySimpleGUI as sg  # graphic user interface for making the game run in a window
import json  # used for save and load game data
import CEItems  # items used in the game; CEItems.py
import CERndnames_conditions as rnc

'''

'''

# Functions
def clearScreen():  # prints a looot of new lines to "clear" the terminal
    print('\n ' * 30)


def mainMenu():  # The game's main menu; user can navigate into and out of its options
    while True:
        try:  # Opportunities GUI, menu options
            layout = [
                [sg.Text(
                    '1. Check in with friends\n'  # Player /NPC statistics
                    '2. Go somewhere\n'  # travel
                    '3. What do we have?\n'  # inventory
                    '4. Socialize\n'  # Meet another NPC in the current location
                    '5. Exit')],  # Exit Game
                [sg.InputText('')],
                [sg.Ok()]
            ]

            window = sg.Window('Opportunities:', layout)
            event = window.read()
            window.close()

            menuChoice = int((event[1])[0])

        except ValueError:
            sg.popup('Please try again with an integer.')
            menuChoice = 0

            # Check in with friends
        if menuChoice == 1:
            for member in party:  # for each Character in party[] list, print stats
                member.stats()

        # Go somewhere
        if menuChoice == 2:
            # main menu for moving
            while True:  # exit this menu if input = 5
                try:  # print character's coordinate and move choices
                    layout = [
                        [sq.Text(
                            f'{me.first_name} and the others are at: '
                            f'{me.myCoordinate.printCoordinate()}\n'
                            '\n1. North\n'
                            '2. South\n'
                            '3. East\n'
                            '4. West\n'
                            '5. Stay put\n')],
                        [sg.InputText()]
                        [sg.Ok()]
                    ]

                    window = sg.Window('Location', layout)
                    value = window.read()
                    window.close()

                    moveChoice = int((value[1])[0])

                except ValueError:
                    sg.popup('Please try again with an integer.')

                if moveChoice == 1:  # move North
                    sg.popup('You move north.')
                    for player in party:
                        player.myCoordinate.y += 1

                if moveChoice == 2:  # move South
                    sg.popup('You move south.')
                    for player in party:
                        player.myCoordinate.y -= 1

                if moveChoice == 3:  # move East
                    sg.popup('You move east.')
                    for player in party:
                        player.myCoordinate.x += 1

                if moveChoice == 4:  # move West
                    sg.popup('You move west.')
                    for player in party:
                        player.myCoordinate.x -= 1

                if moveChoice == 5:
                    sg.popup('You stay put.')
                    break

        # Inventory: show the Inventory item of each Character in the user's party[]
        if menuChoice == 3:
            for member in party:
                member.inventory()  # print items in list for each party[] member
            input("Press any key to continue")

        # socialize - Add a new randomized NPC to your party!
        if menuChoice == 4:
            clearScreen()

            print("Socializing...")
            friend_npc = Character()  # Create a new NPC character from "socializing" at this place
            friend_npc.first_name = random.choice(rnc.first_names)
            friend_npc.languages.append(random.choice(friend_npc.hometown.languages))
            friend_npc.possessions.append(CEItems.Item(random.choice(CEItems.itemsList)))
            party.append(friend_npc)  # add new NPC character to user party[]

            time.sleep(random.randint(1, 4))  # wait, we are socializing

            print(f"{friend_npc.first_name} has decided to tag along with y'all!")
            randomGiftChance = random.randint(1, 10)

            if randomGiftChance > 5:  # random gift from new friend
                randomGift = random.choice(CEItems.itemsList)  # gift is random item from CEItems.py
                me.possessions.append(randomGift)  # add the randomGift to the player's possessions[]
                print(f'{friend_npc.first_name} gives you a token of appreciation!: {randomGift.name}')

                time.sleep(1)

            input("Press ENTER to continue")
            # to-do: add some functionality about the player, or player's party, only able to welcome a new
            # NPC if there is a common language

        # exit
        if menuChoice == 5:
            clearScreen()
            print("Goodbye!")

            time.sleep(1)
            break

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Constants
party = []  # player party with self and NPCs
partysize = 1
year = random.randrange(700, 2080, 1)  # Game year begins between 700 and 2080.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Classes Coordinates, Language, Location, Serbia(Location), Albania(Location), Helsingfors(Location)
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printCoordinate(self):
        return f'(X: {self.x}, Y: {self.y})'


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
        self.capital = Coordinate(0, 0)  # gets assigned during the game
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


# Appends
location_list.append(Serbia())
location_list.append(Albania())
location_list.append(Helsingfors())

# startLocation
startLocation = random.choice(location_list)
startLocation.capital = Coordinate(0, 0)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Character Class - user's and NPC's attributes, statistics, information about them used in the game
class Character:
    def __init__(self):
        self.first_name = ""
        self.last_name = random.choice(rnc.last_names)
        self.myCoordinate = Coordinate(0, 0)
        self.money = 1
        self.level = 1
        self.age = random.randint(18, 90)  # Character's age is between 18 and 90 years old
        self.possessions = []  # possessions[] is the Character's inventory
        self.hometown = random.choice(location_list)
        self.languages = []  # first language from Character's hometown; more can be added to list during game
        self.languages.append(random.choice(self.hometown.languages))
        self.condition = "normal"

    # show character stats
    def stats(self):
        # e.g. Leb Jones from Tallinn
        # f'Location\t {self.x}, {self.y}'
        layout = [
            [sg.Text(
                f'\n--- {self.first_name} {self.last_name} from {self.hometown.name} ---\n'
                f'Money\t\t: {self.money}\n'
                f'Level\t\t: {self.level}\n'
                f'Age\t\t\t: {self.age} years old\n'
                f'Condition\t: {self.condition}\n'
                f'Languages\t: {self.languages}\n'
                f'Location\t: {self.myCoordinate.printCoordinate()}')],
            [sg.Ok()]
        ]

        # for language in self.languages:
        #     print(f'\t\t{language.name}')

        window = sg.Window('Party stats:', layout)
        window.read()
        window.close()

    # inventory
    def inventory(self):
        print("Inventory:")
        print(f' - - - {self.first_name} {self.last_name}')
        for item in self.possessions:  # for each item in the character's possessions[] list, print it
            print(item)

    # add money to character
    def add_money(self, amount):
        self.money += amount


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# START
clearScreen()

# simple popup windows with text, buttons and images

layout = [[sg.Image(r'art1.png')],  # every element is on its own separate line. Image*
          [sg.Text('- - by Caleb & Friends - -')],  # Text*
          [sg.Ok()]]  # button 'Ok'. returns str 'Ok' from window.read() 'Ok' button press

window = sg.Window('Curious Explorer', layout)
window.read()  # returns  event, value = ('Ok', {0: 'name'}) | event = 'ok', value = {0: 'name'}
window.close() # Always close()

# just a simple popup with text
sg.popup(f'Welcome to {startLocation.name}.\n'
         f'The year is {year}.')

layout = [[sg.InputText('')],
          [sg.Ok()]]

window = sg.Window('What is your name, traveler?', layout)
values = window.read()
window.close()

# Generate player's character using Character Class.
me = Character()
me.first_name = (values[1])[0]  # window return values -> name
me.languages.append((random.choice(me.hometown.languages)))
me.hometown = startLocation
party.append(me)  # add the user's character to the party[].


while True:  # How many friends are with you?
    try:
        layout = [[sg.InputText('')],
                  [sg.Ok()]]

        window = sg.Window('How many friends are with you?', layout)
        values = window.read()
        window.close()

        partysize = int((values[1])[0])
        # time.sleep(2)
        break

    except ValueError:  # if ValuError print msg, sleep and restart while loop
        sg.popup('Please try again with an integer.')

# make party
for i in range(partysize):  # create a user character party; size is partysize variable
    friend = Character()
    party.append(friend)

mainMenu()  # run the main menu loop
