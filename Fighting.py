from Management import Management
import time
import random

character1wins = 0
character2wins = 0


def increment1():
    global character1wins
    character1wins = character1wins + 1
    return character1wins


def increment2():
    global character2wins
    character2wins = character2wins + 1
    return character2wins

def reset():
    global character1wins
    global character2wins
    character1wins = 0
    character2wins = 0

class Fighting(object):


    def rolldice(self):
        return random.randint(1, 20)

    def stregntghcompetition(self, character1, character2):
        managementObject = Management
        character1Health = managementObject.loadcharacterhealth(None, character1)
        character2Health = managementObject.loadcharacterhealth(None, character2)
        character1Strength = managementObject.loadcharacterstrength(None,character1)
        character2Strength = managementObject.loadcharacterstrength(None,character2)
        character1Luck = managementObject.loadcharacterluck(None,character1)
        character2Luck = managementObject.loadcharacterluck(None,character2)
        print(character1 + "'s starting health is " + str(character1Health))
        print(character2 + "'s starting health is " + str(character2Health))
        while True:
            character1DiceRoll = self.rolldice(None)
            character2DiceRoll = self.rolldice(None)
            print("It's " + character1 + "'s turn")
            if character1DiceRoll >= 10:
                character2Health = character2Health - character1Strength
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character2Luck:
                    character2Health = character2Health + character1Strength
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2Health))
                else:
                    print(character2 + " couldn't dodge")
                    print(character2 + "'s health is now " + str(character2Health))
                    if character2Health <= 0:
                        print(character1 + " is the winner")
                        increment1()
                        return False
            if character1DiceRoll < 10:
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2DiceRoll >= 10:
                character1Health = character1Health - character2Strength
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character1Luck:
                    character1Health = character1Health + character2Strength
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1Health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1Health))
                    if character1Health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2DiceRoll < 10:
                print(character2 + " missed")


    def intelligencecompetition(self, character1, character2):
        managementObject = Management
        character1Health = managementObject.loadcharacterhealth(None, character1)
        character2Health = managementObject.loadcharacterhealth(None, character2)
        character1Intelligence = managementObject.loadcharacterintelligence(None,character1)
        character2Intelligence = managementObject.loadcharacterintelligence(None,character2)
        character1Luck = managementObject.loadcharacterluck(None,character1)
        character2Luck = managementObject.loadcharacterluck(None,character2)
        print(character1 + "'s starting health is " + str(character1Health))
        print(character2 + "'s starting health is " + str(character2Health))
        while True:
            character1DiceRoll = self.rolldice(None)
            character2DiceRoll = self.rolldice(None)
            print("It's " + character1 + "'s turn")
            if character1DiceRoll >= 10:
                character2Health = character2Health - character1Intelligence
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character2Luck:
                    character2Health = character2Health + character1Intelligence
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2Health))
                else:
                    print(character2 + " couldn't dodge")
                    print(character2 + "'s health is now " + str(character2Health))
                    if character2Health <= 0:
                        print(character1 + " is the winner")
                        increment1()
                        return False
            if character1DiceRoll < 10:
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2DiceRoll >= 10:
                character1Health = character1Health - character2Intelligence
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character1Luck:
                    character1Health = character1Health + character2Intelligence
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1Health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1Health))
                    if character1Health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2DiceRoll < 10:
                print(character2 + " missed")

    def dexterityncecompetition(self, character1, character2):
        managementObject = Management
        character1Health = managementObject.loadcharacterhealth(None, character1)
        character2Health = managementObject.loadcharacterhealth(None, character2)
        character1Dexterity = managementObject.loadcharacterdexterity(None,character1)
        character2Dexterity = managementObject.loadcharacterdexterity(None,character2)
        character1Luck = managementObject.loadcharacterluck(None,character1)
        character2Luck = managementObject.loadcharacterluck(None,character2)
        print(character1 + "'s starting health is " + str(character1Health))
        print(character2 + "'s starting health is " + str(character2Health))
        while True:
            character1DiceRoll = self.rolldice(None)
            character2DiceRoll = self.rolldice(None)
            print("It's " + character1 + "'s turn")
            if character1DiceRoll >= 10:
                character2Health = character2Health - character1Dexterity
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character2Luck:
                    character2Health = character2Health + character1Dexterity
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2Health))
                else:
                    print(character2 + " couldn't dodge")
                    print(character2 + "'s health is now " + str(character2Health))
                    if character2Health <= 0:
                        print(character1 + " is the winner")
                        increment1()
                        return False
            if character1DiceRoll < 10:
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2DiceRoll >= 10:
                character1Health = character1Health - character2Dexterity
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luckRoll = self.rolldice(None)
                if luckRoll == character1Luck:
                    character1Health = character1Health + character2Dexterity
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1Health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1Health))
                    if character1Health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2DiceRoll < 10:
                print(character2 + " missed")

    def fightingtournement(self, character1, character2):
        managementObject = Management
        if character1 != character2:
            if managementObject.checkifexists(None, character1,character2):
                print("Your first character is " + character1)
                time.sleep(1)
                print("Your second character is " + character2)
                time.sleep(1)
                print("The there will be three rounds ")
                print("The winner will be the character with the most wins")
                time.sleep(1)
                print("Round 1 is a test of Strength ")
                time.sleep(3)
                self.stregntghcompetition(self, character1, character2)
                print("Round 2 is a test of Intelligence ")
                time.sleep(3)
                self.intelligencecompetition(self, character1, character2)
                print("Round 3 is a test of Dexterity ")
                time.sleep(3)
                self.dexterityncecompetition(self, character1, character2)
                time.sleep(3)
                if character1wins > character2wins:
                    print(character1 + " is the ultimate winner, winning " + str(increment1() - 1) + " out of 3 rounds")
                    reset()
                else:
                    print(character2 + " is the ultimate winner, winning " + str(increment2() - 1) + " out of 3 rounds")
                    reset()
            else:
                print("One or more characters do not exist.")
        else:
            print("You must enter two different characters")


