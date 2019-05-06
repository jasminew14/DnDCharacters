from Character import Character
import pickle
print("Welcome to your character creator")

"""def save(self, fileName = None):
    if fileName!= None:
        self.fileName = fileName
    elif self.fileName == None:
        return
    fileObj = open(self. fileName, "wb")
    for account in self.accounts.values():
        pickle.dump(account, fileObj)
    fileObj.close()

def load(self, fileName = None):
    self.accounts = {}
    self.fileName = fileName
    if fileName != None:
        fileObj = open(fileName, "rb")
        while True:
            try:
                account = pickle.load(fileObj)
                self.add(account)
            except EOFError:
                fileObj.close()
                break"""

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
def main():
    while True:
        characterList = []
        print("Enter A to create character")
        print("Enter B to view file or print characters")
        print("Enter C to have characters fight")
        print("Enter E to quit")
        choice = input("Enter choice: ").upper()
        if choice == "A":
            name = input("Enter a character name: ").lower
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
            print("Do you want to save charcter? ")
            print("Enter A or press any key to quit")
            choice = input("Enter choice: ").upper()
            if choice == "A":
                save(objectName, name)
        elif choice == "B":
            filename = input("Enter name of the character you want to load: ").lower
            load(filename)
        elif choice == "C":
            print("worked")
        elif choice == "E":
            print("Bye Bye")
            break
        else:
            print("Please chose A, B, C, D or E")

main()
