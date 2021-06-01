def start_adventure():
    print("")
    print("You find yourself in a flat plain with swaying green grass and massive oak trees scattered near and far into the distance.")
    print("As you look around, you see no signs of civliation, only plains as far as the eye can seeBehind you is a small hill with tall,")
    print("light green grasses and shrubs swaying in the light, cool wind. On the edge of the hill is a small, deteriorated platform with a double door going into it")
    print("You do not remember where you are or how you got here. amd there is a weird sense of urgancy to the situation, specically regrading the doors going into the hill.")
    print("")
    print("Having no idea where you are or why you are here, there are few options for what to do. You can either (1) investiage the platform or (2) investigate the surrounding area")
    platform_or_area = float(input("> "))
    if platform_or_area == 1:
        #platform stuff
        print("platform")
    elif platform_or_area == 2:
        #surroding area stuff
        print("area")
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            platform_or_area = float(input("> "))
            if platform_or_area == 1:
                 #platform stuff
                 print("platform1")
                 break
            elif platform_or_area == 2:
                 #surroding area stuff
                 print("area1")
                 break
            else:
                print("Come again?")

def intro():
    print("Hello traveler. Before you may begin on your journy, I must first know your name.")
    player_name = input("> ")
    print("I see, " + player_name + ".")
    print("")
    print("One last question before the adventure begins... Are you more of a bow and arrow or sword type?")
    player_weapon = input("> ")
    if "sword" in player_weapon.lower():
        player_weapon = True
    elif player_weapon.lower() in ["bow", "arrow", "bow and arrow"]:
        player_weapon = False
    else:
        print("Sorry, I do not understand this. Please say again?")
        while True:
            player_weapon = input("> ")
            if "sword" in player_weapon.lower():
                 player_weapon = True
                 break
            elif player_weapon.lower() in ["bow", "arrow", "bow and arrow"]:
                 player_weapon = False
                 break
            else:
                print("Come again?")
    start_adventure()

intro()