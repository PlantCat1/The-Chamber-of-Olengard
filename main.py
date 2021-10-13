from text import *
#def room4()

def chest():
    print("")
    print(text10)
    print("")
    print("\033[1m" + "Do you (1) open the chest or (2) leave it" + "\033[0m")
    chest_or_not = input("> ")
    if chest_or_not == "1":
        print("chest open")
        if player_weapon_type == True:
            print(text12)
        else:
            print(text11)
    elif chest_or_not == "2":
        print("leave it")
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            chest_or_not = input("> ")
            if chest_or_not == "1":
                 print("chest open")
                 break
            elif chest_or_not == "2":
                 print("leave it")
                 break
            else:
                print("Come again?")

def stairs():
    print("")
    print(text8)
    print("")
    print("\033[1m" + "Do you (1) investigate the chest (2) investigate the guard (3) go past both and move to the next room" + "\033[0m")
    area3 = input(">")
    if area3 == "1":
        print("chest")
        chest()
    elif area3 == "2":
        print("guard")
        #guard()
    elif area3 == "3":
        print("next room")
        #room4()
    else:
        print("Sorry, you can only answer 1, 2 or 3")
        while True:
            area3 = input("> ")
            if area3 == "1":
                print("chest")
                #chest()
                break
            elif area3 == "2":
                print("guard")
                #guard()
                break
            elif area3 == "3":
                print("next room")
                #room4()
                break
            else:
                print("Come again?")
    
def run():
    print("")
    print(text6)
    print("")
    print("\033[1m" + "Do you (1) Try to find a way to get the door open or (2) Venture further into the abyss adhead" + "\033[0m")
    dooropen_or_furter = input("> ")
    if dooropen_or_furter == "1":
        print("")
        print(text9)
        stairs()
    elif dooropen_or_furter == "2":
        print("")
        print("You decide there is nothing for you to do about the door and the only option is to move forward")
        stairs()
    else:
        print("Sorry, you can only answer 1 or 2")
        while True:
            dooropen_or_furter = input("> ")
            if dooropen_or_furter == "1":
                 print("")
                 print(text9)
                 stairs()
                 break
            elif dooropen_or_furter == "2":
                 print("")
                 print("You decide there is nothing for you to do about the door and the only option is to move forward")
                 stairs()
            else:
                print("Come again?")

def door():
    print("")
    print(text5)
    print("")
    print("\033[1m" + "Do you (1) get the hell out of there or (2) go further into the room" + "\033[0m")
    run_or_stay = input("> ")
    if run_or_stay == "1":
        run()
    elif run_or_stay == "2":
        print("")
        print(text7)
        stairs()
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
    print("\033[1m" + "One more question before the adventure begins... Are you more of a (1) sword or (2) bow and arrow type?" + "\033[0m")
    player_weapon_type = input("> ")
    if player_weapon_type == "1":
        player_weapon_type = True
    elif player_weapon_type == "2":
        player_weapon_type = False
    else:
        print("Sorry, I do not understand this. Please try again.")
        while True:
            player_weapon_type = input("> ")
            if player_weapon_type == "2":
                 player_weapon_type = True
                 break
            if player_weapon_type == "1":
                 player_weapon_type = False
                 break
            else:
                print("Come again?")
    if player_weapon_type:
        print("Ah I see... I thought you would pick the sword")
    else:
        print("Ah I see... I thought you would pick the bow")
    start_adventure()

intro()
