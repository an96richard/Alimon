from Trainer import Trainer
from Alimon import Alimon
import random
#This is the Game class used to interact with the player
#This class should be used to take input and call proper functions from other classes as well as store data properly.
#version 0.02
#CHANGE LOG 10/4/2022:
#   Added Beggining stages code for Alidex, Encounters, Trainer info, and Alimon info.
#   Added functions for encounters, creating and storing alimons, and printing necessary information
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
    ali_list = {"MEW": Alimon("MEW", 345, 1), "POOP": Alimon("POOP", 345, 999)}
    main_trainer = None
    def __init__(self):
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
        self.main_trainer = Trainer(name, gender)
        print("It is very nice to meet you {name}, I am Prof. Broke. I am a researcher here in the Pokemon world. I'm sure you know how to be a trainer so here are some pokeballs.".format(name=self.main_trainer.name))
        end_game = 0
        while (end_game == 0):
            print("What will you do now? \n1.Create Alimon \n2.Print Alidex \n3.Encounter \n4.Print Trainer Info \n5.Print <Alimon> Info \n6.Exit")
            # Try to turn input uppercase
            try:
                answer=input().upper().strip()
            except:
                print("That is not a valid choice")
            # Check what choice they made
            if answer == "CREATE ALIMON":
                self.alimon_creation()
            elif answer == "ENCOUNTER":
                self.encounter()
            elif (answer == "PRINT ALIDEX"):
                self.print_alidex()
            elif(answer == "PRINT TRAINER INFO"):
                self.print_trainer_info()
            elif(answer[0:6] == "PRINT " and answer[-5:] == " INFO"):
                try:
                    alimon_name = answer[6:-5].upper().strip()
                except:
                    print("Please enter a valid Alimon")
                    continue
                self.print_alimon_info(alimon_name)
            elif (answer == "BAG"):
                continue;
            elif(answer == "EXIT"):
                end_game = 1
            else:
                print("Sorry that is not a valid choice")


    def alimon_creation(self):
        correct_choice = 0
        name = ""
        capture_rate = 1
        level = 1
        while (correct_choice == 0):
            print("Please enter the name of the Alimon:")
            name = input().upper()
            if (name in self.ali_list):
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
        self.ali_list[name] = Alimon(name, capture_rate, level)
    def print_alidex(self):
        if (len(self.ali_list) == 0):
            print("Oh no! Your Alidex is Empty, Go Create Some!")
        else:
            for key, value in self.ali_list.items():
                print(key)
    def print_trainer_info(self):
        print(self.main_trainer)
    def print_alimon_info(self, alimon):
        if (self.ali_list.get(alimon) != None):
            print(self.ali_list[alimon])
        else:
            print("Sorry that Alimon does not exist")

    def encounter(self):
        weighted_list = []
        for alimon in self.ali_list:
            weighted_list.append(self.ali_list[alimon].encounter_rate)
        encountered_alimon = random.choices(list(self.ali_list), weights=weighted_list, k=1)
        print(encountered_alimon[0])
        correct_choice = 0
        while (correct_choice == 0):
            print("You Have Encountered {name}! What Would You Like To Do?".format(name=encountered_alimon[0]))
            print("Battle (not Implemented)\nBag\nRun")
            try:
                answer = input().upper().strip()
            except:
                print("That is not a valid option try again")
            if (answer == "BATTLE"):
                print("Sorry this has not been implemented yet, please RUN or BAG")
            elif (answer == "BAG"):
                continue
            elif (answer == "RUN"):
                correct_choice == 1
            else:
                print("Sorry that is not a valid option, please choose something else")