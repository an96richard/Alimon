from Trainer import Trainer
from Alimon import Alimon

#This is the Game class used to interact with the player
#This class should be used to take input and call proper functions from other classes as well as store data properly.
#------------------------------------------------------
#TODO:
#1.Create Encounter Logic
#   -Battling
#       -Attacks
#       -HP
#       -EXP Gain
#   -Run Option
#   -Item Usage
#       -Capturing
#           -Ball Usage
#       -Healing
#2.Items
#   -Balls
#   -Potions
#   -Misc
#   -Key Items
#
#3.Save and Load
#4.Other
#   -NPC
#   -Maps


class Game:
    def __init__(self):
        ali_list = {"Mew": Alimon("MEW", 0.9, 1)}
        main_menu_choices = ["CREATE ALIMON", "PRINT ALIDEX", "ENCOUNTER", "EXIT"]
        print("Welcome to the world of Pokemon! Are You A Boy or a Girl?")
        correct_choice = 0
        while (correct_choice == 0):
            try:
                gender = input().upper()
            except:
                print("Please choose boy or girl")
            if (gender == "BOY" or gender == "GIRL"):
                correct_choice = 1
            else:
                print("Please choose boy or girl")
        print("Well that's wonderful, what is your name?")
        name = input().upper()
        new_trainer = Trainer(name, gender)
        print("It is very nice to meet you {name}, I am Prof. Broke. I am a researcher here in the Pokemon world. I'm sure you know how to be a trainer so here are some pokeballs.".format(name=new_trainer.name))
        end_game = 0
        while (end_game == 0):
            print("What will you do now? \n1.Create Alimon \n2.Print Alidex \n3.Encounter \n4.Print Trainer Info \n5.Print <Alimon> Info \n6.Exit")
            # Try to turn input uppercase
            try:
                answer = input().upper()
            except:
                print("That is not a valid choice")

            # Check what choice they made
            if answer not in main_menu_choices:
                print("That is not a valid choice, please try again")
            elif answer == "CREATE ALIMON":
                correct_choice = 0
                name = ""
                capture_rate = 1
                level = 1
                while (correct_choice == 0):
                    print("Please enter the name of the Alimon:")
                    name = input().upper()
                    if (name in ali_list):
                        print("That Alimon Already Exists")
                    else:
                        correct_choice = 1
                correct_choice = 0
                while (correct_choice == 0):
                    print("Does it have an initial level?(1-100)")
                    level = input()
                    try:
                        level = int(level)
                        if (level >= 1 and level <= 100):
                            correct_choice = 1
                        else:
                            print("Please pick an integer from 1-100")
                    except:
                        print("Please pick an integer from 1-100")
                correct_choice = 0
                while (correct_choice == 0):
                    print("What would you like the capture rate to be out of 1000?(1-999)")
                    capture_rate = input()
                    try:
                        capture_rate = int(capture_rate)
                        if (capture_rate >= 1 and capture_rate <= 999):
                            capture_rate = capture_rate / 1000
                            correct_choice = 1
                        else:
                            print("Please pick an integer from 1-999")
                    except:
                        print("Please pick an integer from 1-999")
                ali_list[name] = Alimon(name, capture_rate, level)
            elif answer == "ENCOUNTER":
                # Put a check to make sure poke_list has pokemon
                # ---------------------------------------------
                # Assuming it has pokemon,
                continue
            elif (answer == "PRINT ALIDEX"):
                if (len(ali_list) == 0):
                    print("Oh no! Your Alidex is Empty, Go Create Some!")
                else:
                    for key, value in ali_list.items():
                        print(key)
            elif (answer == "BAG"):
                continue;
            else:
                end_game = 1