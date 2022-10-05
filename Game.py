from Trainer import Trainer
from Alimon import Alimon
from Item import Item
from AliBall import AliBall
import random
#This is the Game class used to interact with the player
#This class should be used to take input and call proper functions from other classes as well as store data properly.
#version 0.03
#CHANGE LOG 10/5/2022:
#   Added Bag Logic, Item Class, AliBall Class
#   Added functions for adding to bag
#   Revamped Main Menu to accomodate users. Simplified now.
#
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
#   -Use Items
#   -Balls
#      -Different Balls
#   -Potions
#   -Misc
#   -Key Items
#
#3.Save and Load
#4.Other
#   -NPC
#   -Maps
#   -Alidex viewing


# ---------------------------------------------------------------------------------------------------------------
#                                          GAME CLASS
#   -Game Class that will run the main menu and text of the game
#   -Should create a trainer and an empty Alidex on run right now
#   -Constructor will start the game
#   ............................................................................................................
#                                          Possible Changes
#   -Instantiate Alidex in main class, and have constructor take in an Alidex for multiple games (load/saves)
#   -Instantiate main trainer in main class to have different trainers
#   ............................................................................................................
#
# ---------------------------------------------------------------------------------------------------------------
class Game:
    ali_list = {"MEW": Alimon("MEW", 345, 1), "POOP": Alimon("POOP", 345, 999)}
    menu_choices = ["Create Alimon" ,"Print Alidex" , "Encounter" ,"Print Trainer Info","Print <Alimon> Info" ,"Bag" ,"Exit"]
    item_list = {"POKEBALL" : ["BALL", 0, ]}
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
        self.main_trainer.add_to_bag(AliBall(), 5)



        num_of_menu_choices = len(self.menu_choices)
        choice_num = 1
        select_num = 1
        end_game = False
        while (not end_game):
            for choice in self.menu_choices:
                if (select_num == choice_num):
                    print(">{choice_num}.".format(choice_num=choice_num) + choice)
                    choice_num += 1
                    current_choice = choice
                else:
                    print("{choice_num}.".format(choice_num=choice_num) + choice)
                    choice_num += 1
            choice_num = 1
            print("What will you do now? (DOWN, UP, ENTER, EXIT)")
            # Try to turn input uppercase
            try:
                answer=input().upper().strip()
            except:
                print("That is not a valid choice")
            if (answer == "DOWN"):
                if (select_num == num_of_menu_choices):
                    select_num = 1
                else:
                    select_num += 1
            elif (answer == "UP"):
                if (select_num == 1):
                    select_num = num_of_menu_choices
                else:
                    select_num -= 1
            elif (answer == "ENTER"):
                print(current_choice)
                if current_choice == "Create Alimon":
                    self.alimon_creation()
                # IF answer is ENCOUNTER call encounter function
                elif current_choice == "Encounter":
                    self.encounter(self.main_trainer)
                # IF answer is PRINT ALIDEX call print_alidex function
                elif (current_choice == "Print Alidex"):
                    self.print_alidex()
                # IF answer is PRINT TRAINER INFO call print_trainer_info function
                elif (current_choice == "Print Trainer Info"):
                    self.print_trainer_info()
                #IF answer is PRINT <Alimon> INFO separate the alimon name and then call print_alimon_info on it
                #TODO: Add AliDex viewer to eliminate this choice
                #elif (current_choice == "PRINT <Alimon> INFO"):
                #    print("What Alimon Would You Like To See?")
                #    self.print_alimon_info(alimon_name)
                # IF answer is BAG call create BAG function which will turn on the BAG menu
                elif (current_choice == "Bag"):
                    self.view_bag(self.main_trainer, False)
                # IF answer is EXIT set end_game to 1 and end the game loop
                elif (current_choice == "Exit"):
                    end_game = True
                else:
                    print("Sorry that is not a valid choice.")
            elif(answer == "EXIT"):
                end_game = True
            #IF answer is invalid, print a message and have them choose again
            else:
                print("Sorry that is not a valid choice")



    #---------------------------------------------------------------------------------------------------------------
    #                                          ALIMON CREATION FUNCTION
    #   -Takes in Self as a parameter
    #   -Prompts user for Name, Base Level, Capture Rate, and Encounter Rate
    #   -Creates a new Alimon object and appends it to the "Ali_Dex"
    #---------------------------------------------------------------------------------------------------------------
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

    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT ALIDEX FUNCTION
    #   -Takes in Self as a parameter
    #   -Checks if Length of Pokedex is > 0
    #       -If Yes, Prints All Keys in the "ali_list" dictionary
    #       -If No, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def print_alidex(self):
        if (len(self.ali_list) == 0):
            print("Oh no! Your Alidex is Empty, Go Create Some!")
        else:
            for key, value in self.ali_list.items():
                print(key)

    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT TRAINER INFO FUNCTION
    #   -Takes in Self as a parameter
    #   -Prints Main Trainer info
    # ---------------------------------------------------------------------------------------------------------------
    def print_trainer_info(self):
        print(self.main_trainer)

    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT ALIMON INFO FUNCTION
    #   -Takes in Self and Alimon "name" as a parameter
    #   -Checks if Alimon exists in the Alidex
    #       -If Yes, Prints __repr__ function of the Alimon
    #       -If No, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def print_alimon_info(self, alimon):
        if (self.ali_list.get(alimon) != None):
            print(self.ali_list[alimon])
        else:
            print("Sorry that Alimon does not exist")

    # ---------------------------------------------------------------------------------------------------------------
    #                                          ENCOUNTER FUNCTION
    #   -Takes in Self and trainer as a parameter
    #   -Creates a new Weighted list consisting of all Alimons in the Alidex and their respective encounter rates
    #   -Chooses an Alimon from the Alidex randomly with weighted values and then prints out Encounter text
    #   -Opens a Menu prompting the User to choose what action they would like to do
    #       -If Battle (WIP)
    #       -If BAG (WIP)
    #       -If RUN, make correct choice = 1 and then return them to the last menu
    #       -If invalid choice, prints error message and promps them again about the encounter.
    # ---------------------------------------------------------------------------------------------------------------
    def encounter(self, trainer):
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
                self.view_bag(trainer, True)
            elif (answer == "RUN"):
                correct_choice == 1
            else:
                print("Sorry that is not a valid option, please choose something else")

    # ---------------------------------------------------------------------------------------------------------------
    #                                          VIEW BAG FUNCTION
    #   -Takes in Self, current Trainer, and in_encoutner boolean
    #   -Checks bag is empty
    #       -If Yes, Prints All Items In Bag with a pointer to currently selected item
    #           -Prompts user to navigate the menu or go back
    #           -Selector symbol will move accordingly to user input
    #       -If No, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def view_bag(self, trainer, in_encounter):
        if (len(trainer.bag) == 0):
            print("Oh no! Your Bag is Empty, Go Create Some!")
        else:
            num_of_items_in_bag = len(trainer.bag)
            choice_num = 0
            select_num = 0
            finish_view = False
            while(not finish_view):
                for key, value in trainer.bag.items():
                    if(select_num == choice_num):
                        print(">{choice_num}.".format(choice_num = choice_num) + key + "            x" + str(trainer.bag[key].count))
                        choice_num+=1
                        current_item = trainer.bag[key]
                    else:
                        print("{choice_num}.".format(choice_num = choice_num)+ key + "            x" + str(trainer.bag[key].count))
                        choice_num+=1
                choice_num = 0
                print("Back\n")
                print("---------------------------------------------------------------------------------------")
                print(current_item.desc + "\n")
                print("---------------------------------------------------------------------------------------")
                print("What would you like to do? \nDOWN \nUP \nENTER \nBACK")
                try:
                    answer = input().strip().upper()
                except:
                    print("That is not a valid choice.")
                if(answer == "DOWN"):
                    if(select_num == num_of_items_in_bag -1):
                        select_num = 0
                    else:
                        select_num +=1
                elif(answer == "UP"):
                    if (select_num == 0):
                        select_num = num_of_items_in_bag -1
                    else:
                        select_num -= 1
                elif(answer == "ENTER"):
                    continue
                elif(answer == "BACK"):
                    finish_view = True
                else:
                    print("Sorry that is not a valid choice.")
