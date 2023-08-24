import random
import time

loop = True
while loop == True:
    print("there are 13 Endings, try to get them all!")
    time.sleep(2)
    print("you wake up in a mysterious room.")
    time.sleep(1.4)
    direction = input("there are four doors, one in each direction. which one do you go through?(type n/e/s/w for the direction) ")
    if direction == "n":
        print("you find a plastic skeleton. you have a heart attack and die from how spooky that was.")
        time.sleep(3)
        print("Ending Obtained: Spooky")
        time.sleep(1.5)
    elif direction == "e":
        cheese = input("you find another room, this time, it has a slice of cheese in it. do you eat it? (type y/n) ")
        if cheese == "y":
            print("you eat the cheese.")
            cheesechance = random.randint(1, 2)
            time.sleep(1)
            if cheesechance == 1:
                print("you dropped dead on the floor.")
                time.sleep(0.8)
                print("Ending Obtained: Cheese")
            elif cheesechance == 2:
                print("Tastes good. you move onto the next room.")
                time.sleep(1.5)
                print("you come to a set of two doors.")
                time.sleep(0.8)
                direction4 = input("what door? (1/2) ")
                if direction4 == "1":
                    print("you find a peice of cake. you eat it.")
                    time.sleep(1)
                    print("the cake was poisoned.")
                    time.sleep(1.5)
                    print("Ending Obtained: Overused reference")
                    time.sleep(2)
                elif direction4 == "2":
                    print("behind the door is a bunch of fog. you die.")
                    time.sleep(2.3)
                    print("Ending Obtained: The fog is coming.")
                    time.sleep(1)
        elif cheese == "n":
            print("while you're walking away from the cheese, the cheese sneaks up behind you and stabs you.")
            time.sleep(3)
            print("Ending Obtained: Cheesy")
    elif direction == "s":
        print("another set of doors. this time only 2.")
        time.sleep(2)
        direction2 = input("which door? (type 1/2) ")
        if direction2 == "1":
            print("the door was actually a bomb. you exploded.")
            time.sleep(1)
            print("Ending Obtained: Door Bomb")
            time.sleep(1.4)
        elif direction2 == "2":
            print("you move onto the next room.")
            time.sleep(1)
            print("When you step into the room, you randomly have a brain aneurysm and die.")
            time.sleep(2)
            print("Ending Obtained: Aneurysm")
            time.sleep(2)
    elif direction == "w":
        print("more doors. only 3 this time.")
        time.sleep(1.5)
        direction3 = input("what door? (type 1/2/3) ")
        if direction3 == "1":
            print("As soon as you touch the doorknob, a spear breaks through the door and impales you.")
            time.sleep(2.5)
            print("Ending Obtained: Spear")
            time.sleep(1)
        elif direction3 == "2":
            print("you try to open the door, but it's locked.")
            time.sleep(1.3)
            lockpick = input("try to pick the lock? (type y/n) ")
            if lockpick == "y":
                lockchance = random.randint(1, 6)
                if lockchance == 6:
                    print("you pick the lock and escape!")
                    time.sleep(1.5)
                    print("Ending Obtained: Escaped")
                    time.sleep(2)
                else:
                    print("you failed to pick the lock. you died of skill issues.")
                    time.sleep(2.5)
                    print("Ending Obtained: Skill Issue")
                    time.sleep(2)
            elif lockpick == "n":
                print("you decide not to pick the lock.")
                time.sleep(1.5)
                print("you die of sadness shortly after.")
                time.sleep(1)
                print("Ending Obtained: Sad")
        elif direction3 == "3":
            print("you enter a room with a big red button in it, do you press it?")
            time.sleep(1)
            pressbutton = input("Press it? (y/n) ")
            if pressbutton == "y":
                print("you press the button.")
                time.sleep(2)
                print("you get teleported outside! you are free!")
                time.sleep(2.3)
                print("Ending Obtained: Teleportation")
                time.sleep(1.3)
            elif pressbutton == "n":
                print("You gain some common sense and you don't press the button.")
                time.sleep(2.5)
                print("However, you tripped and fell on the button.")
                time.sleep(1)
                print("you are then promptly hit by a missle and die.")
                time.sleep(2)
                print("Ending Obtained: Kaboom")
                time.sleep(2.5)