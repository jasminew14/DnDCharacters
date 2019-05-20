
class Management(object):

    @staticmethod
    def save(name):   # # Making a method that saves a character and checks if the name exists
        if name in open('Saves.txt').read():
            print("Please try a new name")
            return True
        else:
            print("Your character was saved ")
            return False

    @staticmethod
    def checkifexists(name, name2):   # #  Checking if both character exists
        if name and name2 in open('Saves.txt').read():
            return True
        else:
            return False

    @staticmethod
    def show_characters():
        # # Showing list of characters
        headers = ["Name  ", "Race", "Health", "Luck", "Strength", "Intelligence", "Dexterity "]
        print("%-8s " % "       ".join(headers))
        for line in open("Saves.txt", "r"):
            line = line.strip().split(",")    # # Splitting the lust via commas
            line.append(str(int(line[3]) - int(line[5])))
            for i, word in enumerate(line):
                if i == 7:
                    continue
                print("%-8s" % word.ljust(len(headers[i - (i > 7)])), end="     " * ((i - (i > 7)) != len(headers) - 1))
            print()

    @staticmethod
    def load_character_health(name):     # # Loading a specific attribute from a specific character
        for line in open("Saves.txt", "r"):
            if line.startswith(name):
                line = line.strip().split(",")
                health = int(line[2])
                return health

    @staticmethod
    def load_character_luck(name):     # # Loading a specific attribute from a specific character
        for line in open("Saves.txt", "r"):
            if line.startswith(name):
                line = line.strip().split(",")
                luck = int(line[3])
                return luck

    @staticmethod
    def load_character_strength(name):     # # Loading a specific attribute from a specific character
        for line in open("Saves.txt", "r"):
            if line.startswith(name):
                line = line.strip().split(",")
                strength = int(line[4])
                return strength

    @staticmethod
    def load_character_intelligence(name):     # # Loading a specific attribute from a specific character
        for line in open("Saves.txt", "r"):
            if line.startswith(name):
                line = line.strip().split(",")
                intelligence = int(line[5])
                return intelligence

    @staticmethod
    def load_character_dexterity(name):     # # Loading a specific attribute from a specific character
        for line in open("Saves.txt", "r"):
            if line.startswith(name):
                line = line.strip().split(",")
                dexterity = int(line[6])
                return dexterity
