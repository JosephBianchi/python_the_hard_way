from sys import exit

def kitchen():
    print("this room is full of food. What kind of food should you eat?")
    print("meat")
    print("vegan")
    print("nothing")

    choice = input("> ")

    if "vegan" in choice and "meat" in choice:
        print("you're getting fat")
        dead("you exploded")
    elif "vegan" in choice:
        print("you win - you'll gain health")
        exit(0)
    elif "meat" in choice:
        print("you win - nice yo'll gain strength")
        exit(0)
    else:
        print("what not hungry")
        dead("you starved")

def chef_office():
    print("welcome to the chef's office. Lucky he's sleeping now's your chance to steal is key to get to tke kithchen.")
    print("options:")
    print("tip-toe")
    print("run")

    choice = input("> ")

    if "tip-toe" in choice:
        print("nice you got the keys")
        kitchen()
    elif "run" in choice:
        print("you woke the chef out, and he caught you for stew")
        dead("you're fryed")
    else:
        print("know your options")
        dead("make a better choice next time")

def dead(why):
    print(why, "uh oh")
    exit(0)

def start():
    print("you are about to go on a mission let's begin")
    print("you're goal is to gain health, or strength - don't make any wrong moves")
    chef_office()

start()
