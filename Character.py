import random

class Character(object):

    def __init__(self, name):
        self.name = name
        self.intelligence = random.randint(1, 20)
        self.strength = random.randint(1, 20)
        self.luck = random.randint(1, 20)
        self.dexterity = random.randint(1, 20)
        self.health = random.randint(50, 100)
        self.characterList = []

    """def nameDuplicate(self):
        if len(self.characterList) > 0:
            while True:
                for character in len(self.characterList):
                    if self.characterList[character] == self.characterID():
                        if self.characterList[character] == self.name:
                            True
                        else:

                            False"""

    def __str__(self):
        return "Your name is " + self.name + " Your stats are \n Strength: " + str(self.strength) + "\n Intelligence: "\
               + str(self.intelligence) + "\n Luck: " + str(self.luck) + \
               "\n Dexterity: " + str(self.dexterity) + "\n Health: " + str(self.health)
