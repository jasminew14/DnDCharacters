import random


class Character(object):

    def __init__(self, name):  # # Creating a character with random attributes
        self.name = name
        races = ["Elf", "Dwarf", "Orc", "Human", "Gnome", "Dragonborn"]
        self.race = random.choice(races)
        self.intelligence = random.randint(1, 20)
        self.strength = random.randint(1, 20)
        self.luck = random.randint(1, 20)
        self.dexterity = random.randint(1, 20)
        self.health = random.randint(50, 100)
        self.characterList = []

    def getattributes(self):   # # Making a method that returns attribute in a one line separated by commas
        return self.name + "," + self.race + "," + str(self.health) + "," + str(self.luck) + "," +\
               str(self.strength) + "," + str(self.intelligence) + "," + str(self.dexterity)

    def __str__(self):   # # Printing character so the user can see
        return "You are " + self.name + " the " + self.race + "\n Your stats are \n Strength: " + str(self.strength) + \
               "\n Intelligence: " + str(self.intelligence) + "\n Luck: " + str(self.luck) + \
               "\n Dexterity: " + str(self.dexterity) + "\n Health: " + str(self.health)
