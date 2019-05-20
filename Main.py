from Character import Character
from Management import Management
from Fighting import Fighting

management_object = Management
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
            name = input("Enter a character name: ")  # #Inputting your character name
            name = name.lower()
            name = name.capitalize()  # #Making sure the naming convention is consistent
            object_name = Character(name)
            print(object_name)
            print("Do you want to save character? ")
            print("Enter A or press any key to quit")
            choice = input("Enter choice: ").upper()
            if choice == "A":
                if management_object.save(name):
                    f = open('Saves.txt', 'a')  # # Opening the text file
                    f.write(object_name.getattributes())  # # Saving the attributes of the object
                    f.close()
                else:
                    continue
        elif choice == "B":
            management_object.show_characters()  # # Showing the a list of characters in the table format
        elif choice == "C":
            filename = input("Enter the name of your first character: ")
            filename = filename.lower()
            filename = filename.capitalize()  # #Making sure the naming convention is consistent
            filename2 = input("Enter the name of your second character: ")
            filename2 = filename2.lower()
            filename2 = filename2.capitalize()  # #Making sure the naming convention is consistent
            fighting.fighting_tournament(Fighting, filename, filename2)  # # Starting the fighting simulation
        elif choice == "D":
            print("Bye Bye")
            break
        else:
            print("Please chose A, B, C, D or E")


main()
