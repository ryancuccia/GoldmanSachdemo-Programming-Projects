#here I used modular design to create a program
#that can read one of my professor's files
#and create a dictionary from that file so the user can input a word
#and the corresponding definition would be returned
def welcome():
    input("Welcome to my dictionary program. Press enter to open the file you wish to be read.")
    
dictionary = {}
def fileread():
    from tkinter.filedialog import askopenfilename
    ufile = askopenfilename()
    span = 2
    dictfile = open(ufile)
    data = dictfile.read().replace('\n', ':')
    words = data.split(':')
    yolo = [":".join(words[i:i+span]) for i in range(0, len(words), span)]
    for i in yolo:
        x = i.split(":")
        a = x[0]
        b = x[1]
        dictionary[a] = b
    dictfile.close()


def usersearch():
    print("Please enter the name of the word you would like to search, press enter to quit.")
    greg = 0
    while greg == 0:
        inpoot = input()
        inpoot = inpoot.strip()
        inpoot = inpoot.lower()
        if inpoot == "":
            greg = 1
        else:
            molly = dictionary.get(inpoot, "Word not found")
            print(molly)
            
def exitfunc():
    print("Thank you for using my program.")



def main():
    welcome()
    fileread()
    usersearch()
    exitfunc()

main()
