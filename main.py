from text import *

def start_adventure():
    print("")
    print(text1)
    print("")
    print("Having no idea where you are or why you are here, there are few options for what to do. You can either (1) investiage the platform or (2) investigate the surrounding area")
    platform_or_area = input("> ")
    if platform_or_area >= "1" and platform_or_area <= "1":
        print("")
        print(text2)
        print("")
    elif platform_or_area >= "2" and platform_or_area <= "2":
        #print("")
        #print("text3")
        print("")
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            platform_or_area = input("> ")
            if platform_or_area >= "1" and platform_or_area <= "1":
                 print("")
                 print(text2)
                 print("")
                 break
            elif platform_or_area >= "2" and platform_or_area <= "2":
                 #print("")
                 #print("text3")
                 print("")
                 break
            else:
                print("Come again?")

def intro():
    print("Hello traveler. Before you may begin on your journy, I must first know your name.")
    player_name = input("> ")
    print("I see, " + player_name + ".")
    print("")
    print("One last question before the adventure begins... Are you more of a (1) bow and arrow or (2) a sword type?")
    player_weapon = input("> ")
    if player_weapon >= "2" and player_weapon <= "2":
        player_weapon = True
    elif player_weapon >= "1" and player_weapon <= "1":
        player_weapon = False
    else:
        print("Sorry, I do not understand this. Please try again.")
        while True:
            player_weapon = input("> ")
            if player_weapon >= "2" and player_weapon <= "2":
                 player_weapon = True
                 break
            if player_weapon >= "2" and player_weapon <= "2":
                 player_weapon = False
                 break
            else:
                print("Come again?")
    if player_weapon:
        print("Ah I see... I thought you would pick the sword")
    else:
        print("Ah I see... I thought you would pick the bow")
    start_adventure()

intro()