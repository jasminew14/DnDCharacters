from Character import Character
from Management import Management
from Fighting import Fighting

o = Management
fighting = Fighting
print("Welcome to your character creator")


def main():
    while True:
        print("Enter [A] to create character")
        print("Enter [B] to print characters")
        print("Enter [C] to have characters fight")
        print("Enter [D] to quit")
        choice = input("Enter choice: ").upper()
        if choice == "A":
            name = input("Enter a character name: ")
            name = name.lower()
            name = name.capitalize()
            objectname = Character(name)
            print(objectname)
            print("Do you want to save character? ")
            print("Enter A or press any key to quit")
            choice = input("Enter choice: ").upper()
            if choice == "A":
                if o.save(None,name):
                    f = open('Saves.txt', 'a')
                    f.write(objectname.getattributes())
                    f.close()
                else:
                    continue
        elif choice == "B":
            o.showcharacters(None)
        elif choice == "C":
            filename = input("Enter the name of your first character: ")
            filename = filename.lower()
            filename = filename.capitalize()
            filename2 = input("Enter the name of your second character: ")
            filename2 = filename2.lower()
            filename2 = filename2.capitalize()
            fighting.fightingtournement(Fighting, filename, filename2)
        elif choice == "D":
            print("Bye Bye")
            break
        else:
            print("Please chose A, B, C, D or E")

main()
