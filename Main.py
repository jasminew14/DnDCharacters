from Character import Character
import pickle
import json
print("Welcome to your character creator")



def save(objectName,fileName):
    object = objectName
    file = open(fileName, 'wb')
    pickle.dump(object, file)
    file.close()

def load(fileName):
    filehandler = open(fileName, 'rb')
    object = pickle.load(filehandler)
    print(object)
    filehandler.close()
def saveJson(objectName,fileName):
    object = objectName
    file = open(fileName, 'wb')
    pickle.dump(object, file)
    file.close()

def loadJson(fileName):
    filehandler = open(fileName, 'rb')
    object = pickle.load(filehandler)
    print(object)
    filehandler.close()


def main():
    while True:
        characterList = []
        print("Enter A to create character")
        print("Enter B to view file or print characters")
        print("Enter C to have characters fight")
        print("Enter D to quit")
        choice = input("Enter choice: ").upper()
        if choice == "A":
            name = input("Enter a character name: ")
            name = name.lower()
            name = name.capitalize()
            objectName = Character(name)
            """if len(characterList)>0:
                while True:
                    for character in len(characterList):
                        if characterList[character] == name:
                            name = input("Enter a new character name: ")
                            if characterList[character] == name:
                                True
                            else:
                                False"""
            print(objectName)
            print("Do you want to save character? ")
            print("Enter A or press any key to quit")
            choice = input("Enter choice: ").upper()
            if choice == "A":
                f = open('Saves.txt','w')
                f.write(objectName.getattributes())
                f.close()
                print("Character was saved")
        elif choice == "B":
            filename = input("Enter name of the character you want to load: ")
            filename = filename.lower()
            filename = filename.capitalize()
            load(filename)
        elif choice == "C":
            """character1 = input("Choose character 1: ")
            character2 = input("Choose character 2: ")
            if character1 == character2:
                print("You mst choose two characters")
            else:
                character1 = loadCharacter1(character1)
                character2 = loadCharacter2(character2)"""
            filename = input("Enter name of the character you want to load: ")
            filename = filename.lower()
            filename = filename.capitalize()
        elif choice == "D":
            print("Bye Bye")
            break
        else:
            print("Please chose A, B, C, D or E")

main()
