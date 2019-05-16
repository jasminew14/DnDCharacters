class Management(object):

    def save(self,name):
        with open('Saves.txt', 'r') as datafile:
            for line in datafile:
                if name not in line:
                    return True
                else:
                    print("Please try a new name")
                    return False

    def showcharacters(self):
        headers = ["Name","Race","Health","Luck","Strength","Intelligence","Dexterity"]
        print("   ".join(headers))
        for line in open("Saves.txt", "r"):
            line = line.strip().split(",")
            line.append(str(int(line[3]) - int(line[5])))
            for i, word in enumerate(line):
                if i == 7:
                    continue
                print(word.ljust(len(headers[i - (i > 4)])), end="    " * ((i - (i > 4)) != len(headers) - 1))
            print()

    def loadcharacterstats(self,name):

        breakpoint()
