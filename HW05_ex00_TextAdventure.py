#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

def backdoor(username5):
    print ("This is the backdoor filled with awesome programmers and ", username5, " is one of them.")
    print (username5," clears throat and then all great programmers welcome ", username5)
    print (username5, "starts programming in Python and never leaves")
    exit (0)


def infinite_stairway_room(count,username4):
    print(username4, " walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light. The user now has two options i.e. to take stairs')
    print("The second option is to follow the myth of the Nerds and look around to find the backdroor which is the stuff of legends")
    flag = 0
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        if count >0 and flag == 0 :
            print(username4," takes the stairs but is not happy about it.")
            print(username4," continues walking on the stairs")
            flag = 1

        while count > 0 and flag == 1:
            print("But ",username4, " is not happy about it. The player keeps walking")
            count = count -1
            flag = 1
            continue
        if count == 0 and flag == 1:
            print("The player reaches a backroom and cannot return back now since ", username4, " is too tired!!")
            print("The user now only has a option to go through the backdoor or stay here and starve. Please choose your option wisely !!! ")
            next10 = input("> ")
            if next == "take the backdoor":
                print(username4," slowly opens the backdoor revealing the tresures behind it ")
                print("\n")
                backdoor(username4)
            else:
                dead("Starvation and exhaustion kill !!!")

        #infinite_stairway_room(count+1,username4)
    # option 2 == The user in my version of the game searches for a backdoor based on a myth and then starves searching for the backdoor.
    if next == "look around and search for a backdoor":
        print(username4,' keeps searching and starts starving')
        dead ("Starves to death")

        
def gold_room(username3):
    print("This room is full of gold.  How much does ",username3," take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice,",username3," is not greedy, you win!")
        exit(0)
    else:
        dead(username3, " is a greedy goose!")


def bear_room(username2):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is ", username2 , "going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at", username2, " then slaps ", username2 ,"'s face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.", username2," can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews ",username2,"'s leg off.")
        elif next == "open door" and bear_moved:
            gold_room(username2)
        else:
            print("I got no idea what that means.")


def cthulhu_room(username1):
    print(username1, " here sees the great evil Cthulhu.")
    print("He, it, whatever stares at ", username1, " and ", username1, " goes insane.")
    print("Does", username1, "flee for his life or eat ", username1,"'s head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(username1)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print ("Please enter your name aka username")
    print("\n")
    username = input("")
    #This is the name entered by the user.
    print(username , "is in a dark room.") 
    print("There is a door to ",username,"'s right and left and center.")
    print("Which one does ", username, " take?")

    next = input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    elif next == "center":
        infinite_stairway_room(5,username)
    else:
        dead(username, " stumbles around the room until ", username, " starves.")

if __name__ == '__main__':
    main()
