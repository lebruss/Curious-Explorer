#To-do:
#       x, y coordinates
#libraries
from easygui import *
import time, random

#functions



def mainMenu():#MAIN MENU LOOP
    while True:
    #menu options

        msg ='What to do?'
        title = 'Opportunities'
        choices = ['Check in with friends', 'Go somewhere',  'What do we have?', 'Socialize', 'Exit']
        menuChoice = choicebox(msg, title, choices)

        #party stats
        if menuChoice == choices[0]:
            for member in party:
                member.stats()

        #move - not functional, yet. map locations to neighboring locations?
        if menuChoice == choices[1]:
            moveChoice = 0
            while moveChoice != '5':
                 
                print('\n1. North')
                print('\n2. South')
                print('\n3. East')
                print('\n4. West')
                print('\n5. Stay put')
                print('- - - - -')
                moveChoice = input()

        #inventory
        if menuChoice == choices[2]:
             
            print('Inventory:')
            for member in party:
                member.inventory()
            input('Press any key to continue')
        
        #socialize
        if menuChoice == choices[3]:
             
            print('Socialize')
            friend = Character(random.choice(first_names))
            party.append(friend)
            input('Press any key to stop socializing')

        #exit
        if menuChoice == choices[4]:
             
            print('Goodbye!')
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

#MAP_SIZE = {'x': 1000, 'y': 1000}

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
        self.possessions = ['clothes', 'shoes']
        self.languages = []
        self.hometown = random.choice(location_list)
        self.condition = random.choice(conditions)
        
    #show character stats
    def stats(self):
        text = f'''{self.first_name} {self.last_name} from {self.hometown}\n
Money: {self.money}\nLevel: {self.level}\nAge: {self.age} years old
Condition: {self.condition}'''
        
        msgbox(text, title='Stats')

    #inventory
    def inventory(self):
        print('---------' + str(self.first_name) + ' ' + str(self.last_name))
        for item in self.possessions:
            print(str(item))

    #add money to character
    def add_money(self, amount):
        self.money += amount

    #not in use at the moment    
    def move(self, move_x, move_y):
        x = self.x + move_x
        y = self.y + move_y
        #if (x < 0 or x > MAP_SIZE['x'] or y < 0 or y > MAP_SIZE['y']):
            #print('YOU WILL FALL OFF THE FLAT EARTH! DONT GO THERE')
            #return
        
        self.x = x
        self.y = y
        print('NEW POSITION: ', self.x, self.y)

#year
year = random.randrange(700,2080,1)

#start

image = 'logo.png'
msgbox('',image=image)

first_name = enterbox(f'Welcome to {startLocation}.\nThe year is {year}.\nWhat is your name, traveler?\n') 

me = Character(first_name)
party = []
party.append(me)

#How many friends
while True:
    try:
        partysize = enterbox('How many friends are with you?')
        break
    except ValueError:
        partysize = enterbox('Please enter an integer so we can continue.')
 
#make party
for i in range(int(partysize)):
    friend = Character(random.choice(first_names))
    party.append(friend)
    

#print an example Character with all stats
#me.stats()

#move
#print('LETS SEE SOME MOVEMENT')
#me.move(300, 200)
#me.move(10000, 19292)


#Main Menu
mainMenu()
