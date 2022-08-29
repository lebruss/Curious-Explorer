
location_list = ['Serbia', 'Albania', 'Helsingfors', 'Holy Roman Empire', 'the Hanseatic League', 'Prussia',
                 'Iceland', 'Tallinn', 'Estonia', 'Oklahoma', 'Colorado', 'Missouri', 'Viet Nam', 'Somalia', 'Prag', 'the Library',
                  'Scotland', 'Jõhvi', 'a cozy cave', 'the ocean', 'your family home', 'Corpus Cristi',
                   'Japanese Korea', 'the European Union', 'Helsinki', 'Jüri', 'Dagö', 'the Cherokee Nation', 'Haapsalu Castle', 'Greece',
                   'Iran', 'Iraq', 'Uzbekistan', 'Tajikistan', 'Samarkhand', 'Trondheim', 'Istanbul', 'Barcelona', 'Croatia',
                   'the Cyclades', 'Cyprus', 'Brazil', 'Angola', 'Kongo', 'Babylon', 'the River Styx', 'Tasmania', 'Viimsi', 'Hungary']

#locations list, experimental. I want to give different attributes to locations, so I am trying a Class
locations = []
class Location:
    languages = []
    forenames = []
    surnames = []
    def __init__(self, name):
        self.name = name
        locations.append(self)



Albania = Location("Albania")
Albania.languages=['Albanian', 'Greek', 'Latin', 'Italian', 'Turkish']
Albania.forenames=['Klajd', 'Tonibler', 'Shpeta', 'Florian', 'Besa']
Albania.surnames=['Hoxhaj', 'Ismajli', 'Jashari', 'Basha', 'Bogdana', 'Shaqiri', 'Spahija']
locations.append(Albania)

Serbia = Location("Serbia")
Serbia.languages=['Serbian', 'German', 'Hungarian', 'Latin']
locations.append(Serbia)

Helsingfors = Location("Helsingfors")
Helsingfors.languages = ['Swedish', 'Finnish']
locations.append(Helsingfors)

HolyRomanEmpire = Location("Holy Roman Empire")
HolyRomanEmpire.languages=['German', 'Latin']

Hansa = Location("the Hanseatic League")
Hansa.languages=['German']

Prussia = Location("Prussia")
Prussia.languages=['German']

Iceland = Location("Iceland")
Iceland.languages=['Icelandic', 'Danish']

Tallinn = Location("Tallinn")
Tallinn.languages=['Danish', 'Estonian', 'German', 'Russian', 'Swedish']

Estonia = Location("Estonia")
Estonia.languages=['Danish', 'Estonian', 'German', 'Russian', 'Swedish']

Oklahoma = Location("Oklahoma")
Oklahoma.languages=['Choctaw', 'Cree', 'Cado', 'Cherokee', 'English', 'Chickasaw', 'Muscogee']

EuropeanUnion = Location("the European Union")
EuropeanUnion.languages=['German', 'Dutch', 'Polish', 'Estonian', 'Spanish', 'English', 'Albanian', 'Portuguese', 'Latvian', 'Lithuanian',
                            'French', 'Italian', 'Slovene', 'Croatian', 'Hungarian', 'Serbian', 'Swedish', 'Danish', 'Czech', 'Slovak',
                            'Maltese']

print(Serbia.name)
print(Serbia.languages) 

print(Albania.surnames)