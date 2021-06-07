from text import *

def run():
    print("run")

def stay():
    print("stay")

def door():
    print("")
    print(text5)
    print("")
    print("\033[1m" + "Do you (1) get the hell out of them or (2) go further into the room" + "\033[0m")
    run_or_stay = input("> ")
    if run_or_stay == "1":
        run()
    elif run_or_stay == "2":
        stay()
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            run_or_stay = input("> ")
            if run_or_stay == "1":
                 run()
                 break
            elif run_or_stay == "2":
                 stay()
                 break
            else:
                print("Come again?")
    

def surrounding_area():
    print("")
    print(text3)
    platform()

def surrounding_area_platform_first():
    print("")
    print(text4)
    door()


def platform():
    print("")
    print(text2)
    print("")
    print("\033[1m" + "This doesn't provide any answers to your quetions and decide you should either (1) investigate the door or (2) investigate the surronding area." + "\033[0m")
    door_or_area = input("> ")
    if door_or_area == "1":
        door()
    elif door_or_area == "2":
        surrounding_area_platform_first()
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            door_or_area = input("> ")
            if door_or_area == "1":
                 door()
                 break
            elif door_or_area == "2":
                 surrounding_area_platform_first()
                 break
            else:
                print("Come again?")

def start_adventure():
    print("")
    print(text1)
    print("")
    print("\033[1m" + "Having no idea where you are or why you are here, there are few options for what to do. You can either (1) investigate the platform or (2) investigate the surrounding area" + "\033[0m")
    platform_or_area = input("> ")
    if platform_or_area == "1":
        platform()
    elif platform_or_area == "2":
        surrounding_area()
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            platform_or_area = input("> ")
            if platform_or_area == "1":
                 platform()
                 break
            elif platform_or_area == "2":
                 surrounding_area
                 break
            else:
                print("Come again?")

def intro():
    print("")
    print("\033[1m" + "Hello traveler. Before you may begin on your journy, I must first know your name." + "\033[0m")
    player_name = input("> ")
    print("I see, " + player_name + ".")
    print("")
    print("\033[1m" + "One more question before the adventure begins... Are you more of a (1) bow and arrow or (2) a sword type?" + "\033[0m")
    player_weapon = input("> ")
    if player_weapon == "2":
        player_weapon = True
    elif player_weapon == "1":
        player_weapon = False
    else:
        print("Sorry, I do not understand this. Please try again.")
        while True:
            player_weapon = input("> ")
            if player_weapon == "2":
                 player_weapon = True
                 break
            if player_weapon == "1":
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