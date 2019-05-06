from Character import Character
print("Welcome to your character creator")



def main():
    while True:
        characterList = []
        print("Enter A to create character")
        print("Enter B to view file or print characters")
        print("Enter C to have characters fight")
        print("Enter E to quit")
        choice = input("Enter choice: ")
        choice.upper()
        if choice == "A":
            name = input("Enter a character name: ")
            objectName = name
            """if len(characterList)>0:
                while True:
                    for character in len(characterList):
                        if characterList[character] == name:
                            name = input("Enter a new character name: ")
                            if characterList[character] == name:
                                True
                            else:
                                False"""
            objectName = Character(name)
            print(objectName)
        elif choice == "B":
            print("worked")
        elif choice == "C":
            print("worked")
        elif choice == "E":
            print("Bye Bye")
            break

main()
