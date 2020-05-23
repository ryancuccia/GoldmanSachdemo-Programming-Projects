#This is a text based adventure game that I created
#where the user can move around using north, south, east, and west
#until they find their way home

title2 = "Welcome to the middle of the ocean. Can you survive??"
title = "Ocean: The Video Game"
foward = "Press enter to continue..."
h_name = "Please enter the name of your best friend: "
food = "Please enter your favorie kind of seafood: "
home = "Please enter the name of the state that you live in: "
score = "Score:"
current = "Current Location:"
vert = 0
horz = 0
home_a = "PLACE HOLDING STRING"
directiona = "PLACE HOLDIG STRING"

current_locale = ["The middle of the ocean", "Familiar waters", "Western ocean", "Southern ocean", "South eastern ocean", "Fishing cove",\
                  "Northern ocean", "Eastern ocean", "Northeastern ocean", "Home"]
descript = ["You are at the starting position. Move north, south, east, or west to move.", "Familar waters means that you are close to home.",\
            "You do not want to be in the western ocean, move east or risk gettng lost.", "You do not want to be in the southern ocean, move north or risk getting lost",\
            "You do not want to be in the south eastern ocean, find familiar waters or risk getting lost", "The fishing cove is a quaint little spot where luxurious sea life can be found",\
            "The northen ocean can get chilly, move south to find warmer waters and get closer to home", "You do not want to be too far east, move west or risk getting lost",
            "Alright I don't know how you got here but go southwest to get home", "You made it home just in time for dinner and your mom made hot pockets as a welcome home gift!"]
locale_code = current_locale[0]
scoren = 0
descript_code = descript[0]

#has been list
hasbeen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#move counter
moves = 0

def intro():
    print(title)
    print(title2)
    input(foward)
    print()
def intro2():
    intro()
    name = input(h_name)
    food_a = input(food)
    home_a = input(home)
    return(name, food_a, home_a)
    


def locale1(name_po):
    print("Oh no! It looks like you and " + name_po + " are stranded in the middle of the ocean! Type north south east and west to move around. type help for help. type quit to quit")
    print()
def locale2(home_a_po):
    print("You're getting closer to " + home_a_po + ", keep moving.")
def locale3():
    print("You're way too far south. Move north")
def locale4():
    print("Oh no you went too far north! Move south")
def locale5():
    print("You're way too far west. Move east.")
def locale6():
    print("Oh no you went too far east! Move west.")
def locale7(home_a_po):
    print("You made it home to " + home_a_po + "!!!" "Congrats!")
def locale8(food_a_po):
    print("Nice, you stumbled onto some fresh " + food_a_po +"! Enjoy!")
def locale9():
    print("You're back where you started! Keep moving")

def satelite():
    global vert
    global horz
    if vert == 2 and horz == 2:
        locale8(food_a)
    elif vert == 3 and horz == 4:
        locale7(home_a)
    elif vert >= 0 and vert < 4 and horz >= 0 and horz < 5:
        locale2(home_a)
    elif vert >= 0 and horz < 0:
        locale5()
    elif vert < 0 and horz < 0:
        locale9()
    elif vert < 0 and horz >= 0:
        locale3()
    elif vert > 3:
        locale4()
    elif horz > 4:
        locale6()
    elif vert == 0 and horz == 0:
        locale9()

        
def userinput():
    global directiona
    directiona = input("What direction would you like to go in: ")
    directiona = directiona.lower()
    
    

def gps(locale_code_po, scoren_po, descript_po):
    global vert
    global horz
    global locale_code
    global home_a
    global hasbeen
    if vert == 0 and horz == 0:
        locale_code_po = current_locale[0]
        if hasbeen[0] == 0:
            scoren_po = 0
        descript_po = descript[0]
        return(locale_code_po, scoren_po, descript_po)
    elif vert < 0 and horz >= 0:
        locale_code_po = current_locale[3]
        if hasbeen[3] == 0:
            scoren_po = scoren-25
            hasbeen[3] = hasbeen[3] + 1
        descript_po = descript[3]
        return(locale_code_po, scoren_po, descript_po)
    elif vert < 0 and horz < 0:
        locale_code_po = current_locale[4]
        if hasbeen[4] == 0:
            scoren_po = scoren-25
            hasbeen[4] = hasbeen[4] + 1
        descript_po = descript[4]
        return(locale_code_po, scoren_po, descript_po)
    elif vert >= 0 and horz < 0:
        locale_code_po = current_locale[2]
        if hasbeen[2] == 0:
            scoren_po = scoren - 25
            hasbeen[2] = hasbeen[2] + 1
        descript_po = descript[2]
        return(locale_code_po, scoren_po, descript_po)
    elif vert == 2 and horz == 2:
        locale_code_po = current_locale[5]
        if hasbeen[3] == 0:
            scoren_po = scoren + 200
            hasbeen[3] = hasbeen[3] + 1
        descript_po = descript[5]
        return(locale_code_po, scoren_po, descript_po)
    elif vert > 3 and horz < 5:
        locale_code_po = current_locale[6]
        if hasbeen[6] == 0:
            scoren_po = scoren - 25
            hasbeen[6] = hasbeen[6] + 1
        descript_po = descript[6]
        return(locale_code_po, scoren_po, descript_po)
    elif vert < 4 and horz > 4:
        locale_code_po = current_locale[7]
        if hasbeen[3] == 0:
            scoren_po = scoren - 25
            hasbeen[3] = hasbeen[3] + 1
        descript_po = descript[7]
        return(locale_code_po, scoren_po, descript_po)
    elif vert == 3 and horz == 4:
        locale_code_po = current_locale[9]
        if hasbeen[9] == 0:
            scoren_po = scoren + 400
            hasbeen[9] = hasbeen[9] + 1
        descript_po = descript[9]
        return(locale_code_po, scoren_po, descript_po)
    else:
        locale_code_po = current_locale[1]
        if hasbeen[1] == 0:
            scoren_po = scoren + 25
            hasbeen[1] = hasbeen[1] + 1
        descript_po = descript[1]
        return(locale_code_po, scoren_po, descript_po)

def gameloop():
    global directiona
    global vert
    global horz
    global locale_code
    global scoren
    global descript_code
    global moves
    while vert != 3 or horz != 4:
        if moves < 16:
            userinput()
            if directiona == "north":
                vert = vert + 1
                moves = moves + 1
                satelite()
                locale_code, scoren, descript_code = gps(locale_code, scoren, descript_code)
                sand(scoren, locale_code, descript_code)
                print()
            elif directiona == "south":
                vert = vert - 1
                moves = moves + 1
                satelite()
                locale_code, scoren, descript_code = gps(locale_code, scoren, descript_code)
                sand(scoren, locale_code, descript_code)
                print()
            elif directiona == "east":
                horz = horz + 1
                moves = moves + 1
                satelite()
                locale_code, scoren, descript_code = gps(locale_code, scoren, descript_code)
                sand(scoren, locale_code, descript_code)
                print()
            elif directiona == "west":
                horz = horz - 1
                moves = moves + 1
                satelite()
                locale_code, scoren, descript_code = gps(locale_code, scoren, descript_code)
                sand(scoren, locale_code, descript_code)
                print()
            elif directiona == "help":
                print("Type north south east and west to move around. Type quit to quit. If you are lost, from the starting location go north three times and west four times to get home. go north twice and west twice for a bonus.")
                locale_code, scoren, descript_code = gps(locale_code, scoren, descript_code)
                sand(scoren, locale_code, descript_code)
                print()
                userinput()
            elif directiona == "quit":
                print("Game over.")
                break
            else:
                print("Invalid command.")
        else:
            print("You have run out of time and a shark has eaten you in your attempt to find your way back to", home_a  + "! Better luck next time!")
            print()
            break



def sand(scoren_posand, locale_code_posand, descript_posand):
    print(score, scoren_posand)
    print(current, locale_code_posand)
    print()
    print(descript_posand)
    print()

def copyrightm():
    print("I hope you enjoyed my game because it took me a LONG time to make.")
    print("This game was created by Ryan Cuccia spring semester, 2020.")

def main():
    global name
    global food_a
    global home_a
    name, food_a, home_a = intro2()

    locale1(name)

    gameloop()
    copyrightm()

main()
