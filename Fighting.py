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

    @staticmethod
    def roll_dice():
        return random.randint(1, 20)

    def strength_competition(self, character1, character2):
        management_object = Management     # # Creating a management object
        character1_health = management_object.load_character_health(character1)     # # Loading character1 health
        character2_health = management_object.load_character_health(character2)     # # Loading character2 health
        character1_strength = management_object.load_character_strength(character1)     # # Loading character1 strength
        character2_strength = management_object.load_character_strength(character2)     # # Loading character1 strength
        character1_luck = management_object.load_character_luck(character1)     # # Loading character1 luck
        character2_luck = management_object.load_character_luck(character2)     # # Loading character1 luck
        print(character1 + "'s starting health is " + str(character1_health))     # # Printing starting health
        print(character2 + "'s starting health is " + str(character2_health))
        while True:
            character1_dice_roll = self.roll_dice()     # # Dice roll object
            character2_dice_roll = self.roll_dice()
            print("It's " + character1 + "'s turn")
            if character1_dice_roll >= 10:
                character2_health = character2_health - character1_strength     # # Taking character health away
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()     # # Luck roll gives you a chance to dodge
                if luck_roll == character2_luck:
                    character2_health = character2_health + character1_strength     # # If roll equal luck you dodge
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2_health))
                else:
                    print(character2 + " couldn't dodge")     # # If you can't dodge your health is damaged
                    print(character2 + "'s health is now " + str(character2_health))     # # Showing characters health
                    if character2_health <= 0:      # # If character2 health is less than 2 character1 wins
                        print(character1 + " is the winner")
                        increment1()      # # Incrementing wins
                        return False
            if character1_dice_roll < 10:     # # If dice roll is less than 10 characters missed
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2_dice_roll >= 10:
                character1_health = character1_health - character2_strength
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()
                if luck_roll == character1_luck:
                    character1_health = character1_health + character2_strength
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1_health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1_health))
                    if character1_health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2_dice_roll < 10:
                print(character2 + " missed")

    def intelligence_competition(self, character1, character2):      # # Similar to strength competition
        management_object = Management
        character1_health = management_object.load_character_health(character1)
        character2_health = management_object.load_character_health(character2)
        character1_intelligence = management_object.load_character_intelligence(character1)
        character2_intelligence = management_object.load_character_intelligence(character2)
        character1_luck = management_object.load_character_luck(character1)
        character2_luck = management_object.load_character_luck(character2)
        print(character1 + "'s starting health is " + str(character1_health))
        print(character2 + "'s starting health is " + str(character2_health))
        while True:
            character1_dice_roll = self.roll_dice()
            character2_dice_roll = self.roll_dice()
            print("It's " + character1 + "'s turn")
            if character1_dice_roll >= 10:
                character2_health = character2_health - character1_intelligence
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()
                if luck_roll == character2_luck:
                    character2_health = character2_health + character1_intelligence
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2_health))
                else:
                    print(character2 + " couldn't dodge")
                    print(character2 + "'s health is now " + str(character2_health))
                    if character2_health <= 0:
                        print(character1 + " is the winner")
                        increment1()
                        return False
            if character1_dice_roll < 10:
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2_dice_roll >= 10:
                character1_health = character1_health - character2_intelligence
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()
                if luck_roll == character1_luck:
                    character1_health = character1_health + character2_intelligence
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1_health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1_health))
                    if character1_health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2_dice_roll < 10:
                print(character2 + " missed")

    def dexterity_competition(self, character1, character2):     # # Similar to strength competition
        management_object = Management
        character1_health = management_object.load_character_health(character1)
        character2_health = management_object.load_character_health(character2)
        character1_dexterity = management_object.load_character_dexterity(character1)
        character2_dexterity = management_object.load_character_dexterity(character2)
        character1_luck = management_object.load_character_luck(character1)
        character2_luck = management_object.load_character_luck(character2)
        print(character1 + "'s starting health is " + str(character1_health))
        print(character2 + "'s starting health is " + str(character2_health))
        while True:
            character1_dice_roll = self.roll_dice()
            character2_dice_roll = self.roll_dice()
            print("It's " + character1 + "'s turn")
            if character1_dice_roll >= 10:
                character2_health = character2_health - character1_dexterity
                print(character1 + " hits " + character2)
                print(character2 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()
                if luck_roll == character2_luck:
                    character2_health = character2_health + character1_dexterity
                    print(character2 + " dodges")
                    print(character2 + "'s health is still " + str(character2_health))
                else:
                    print(character2 + " couldn't dodge")
                    print(character2 + "'s health is now " + str(character2_health))
                    if character2_health <= 0:
                        print(character1 + " is the winner")
                        increment1()
                        return False
            if character1_dice_roll < 10:
                print(character1 + " missed")

            print("It's " + character2 + "'s turn")
            if character2_dice_roll >= 10:
                character1_health = character1_health - character2_dexterity
                print(character2 + " hits " + character1)
                print(character1 + " gets a chance to roll again to dodge")
                luck_roll = self.roll_dice()
                if luck_roll == character1_luck:
                    character1_health = character1_health + character2_dexterity
                    print(character1 + " dodges")
                    print(character1 + "'s health is still " + str(character1_health))
                else:
                    print(character1 + " couldn't dodge")
                    print(character1 + "'s health is now " + str(character1_health))
                    if character1_health <= 0:
                        print(character2 + " is the winner")
                        increment2()
                        return False
            if character2_dice_roll < 10:
                print(character2 + " missed")

    def fighting_tournament(self, character1, character2):
        management_object = Management
        if character1 != character2:     # # Checking that two characters aren't the same
            if management_object.checkifexists(character1,character2):     # # Checking that characters exist
                print("Your first character is " + character1)
                time.sleep(1)      # # Setting a delay
                print("Your second character is " + character2)
                time.sleep(1)
                print("The there will be three rounds ")
                print("The winner will be the character with the most wins")
                time.sleep(1)
                print("Round 1 is a test of Strength ")
                time.sleep(3)
                self.strength_competition(self, character1, character2)     # # Strength competition
                print("Round 2 is a test of Intelligence ")
                time.sleep(3)
                self.intelligence_competition(self, character1, character2)     # # Intelligence competition
                print("Round 3 is a test of Dexterity ")
                time.sleep(3)
                self.dexterity_competition(self, character1, character2)     # # Dexterity competition
                time.sleep(3)
                if character1wins > character2wins:
                    # # Showing who won out of three rounds
                    print(character1 + " is the ultimate winner, winning " + str(increment1() - 1) + " out of 3 rounds")
                    reset()
                else:
                    print(character2 + " is the ultimate winner, winning " + str(increment2() - 1) + " out of 3 rounds")
                    reset()
            else:
                print("One or more characters do not exist.")
        else:
            print("You must enter two different characters")
