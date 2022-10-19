from Trainer import Trainer
from Alimon import Alimon
from AliBall import AliBall
import keyboard
import os
import time
import random
################################################################################################################################
#                                                                                                                              #
#                                                                                                                              #
#    .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.   #
#   | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |   #
#   | |      __      | || |   _____      | || |     _____    | || | ____    ____ | || |     ____     | || | ____  _____  | |   #
#   | |     /  \     | || |  |_   _|     | || |    |_   _|   | || ||_   \  /   _|| || |   .'    `.   | || ||_   \|_   _| | |   #
#   | |    / /\ \    | || |    | |       | || |      | |     | || |  |   \/   |  | || |  /  .--.  \  | || |  |   \ | |   | |   #
#   | |   / ____ \   | || |    | |   _   | || |      | |     | || |  | |\  /| |  | || |  | |    | |  | || |  | |\ \| |   | |   #
#   | | _/ /    \ \_ | || |   _| |__/ |  | || |     _| |_    | || | _| |_\/_| |_ | || |  \  `--'  /  | || | _| |_\   |_  | |   #
#   | ||____|  |____|| || |  |________|  | || |    |_____|   | || ||_____||_____|| || |   `.____.'   | || ||_____|\____| | |   #
#   | |              | || |              | || |              | || |              | || |              | || |              | |   #
#   | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |   #
#   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'     #
#                                                                                                                              #
#                              Welcome To Alimon, a new adventure created by Richie An                                         #
################################################################################################################################
#
#version 0.07
#CHANGE LGG 10/18/2022
#   Added Save and Load functions and 3 text files containing meta data and trainer profile
#   Added 3 more Balls that will be usable in the future.
#   Implmented logic on reading saves and having a universal alidex and item list
#   Fixed all other functions to work correctly with newly added loading function
#
#version 0.05
#CHANGE LGG 10/17/2022
#   Added new View Bag Functions and logic
#   Implmented Use AliBall Function to properly catch Alimons and store them in trainer team and PC
#   Fixed Encounter to generate new Alimon object on each encounter, and logic for view bag and use items
#
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
#TODO:  IMPLEMENT SAVE, FULL ALIDEX, BATTLE SYSTEM, OTHER ITEMS, EXP SYSTEM
#1.Create Encounter Logic
#   -Battling
#       -Attacks
#       -HP
#       -EXP Gain
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
#   -Story
#   -Events


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
    ali_list = {}
    menu_choices = ["Create Alimon" ,"Print Alidex" , "Encounter" ,"Print Trainer Info","Print <Alimon> Info" ,"Bag","Save","Exit"]
    item_list = {}
    main_trainer = None

    def __init__(self, trainerProfile, itemDex, alimonDex):
        #Empty File Check
        if(itemDex == None):
            print("Please Load an ItemDex file")
            return
        if(alimonDex == None):
            print("Please Load an AliDex file")
            return
        # Call load Alidex, load item list, load_trainer to initialize all 3 with a given save
        self.load_alidex(alimonDex)
        self.load_item_list(itemDex)
        self.load_trainer(trainerProfile)
        #If no trainer profile is provided, this means its a new game so lets create a new Trainer!


        num_of_menu_choices = len(self.menu_choices)
        choice_num = 1
        select_num = 1
        end_game = False
        while (not end_game):
            #MENU CHOICES PRINTING LOGIC
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
                os.system('cls')
                print("That is not a valid choice")
                time.sleep(2)
                os.system('cls')
            if (answer == "DOWN"):
                if (select_num == num_of_menu_choices):
                    select_num = 1
                    os.system('cls')
                else:
                    select_num += 1
                    os.system('cls')
            elif (answer == "UP"):
                if (select_num == 1):
                    select_num = num_of_menu_choices
                    os.system('cls')
                else:
                    select_num -= 1
                    os.system('cls')
            elif (answer == "ENTER"):
                #print(current_choice)
                os.system('cls')
                if current_choice == "Create Alimon":
                    self.alimon_creation()
                # IF answer is ENCOUNTER call encounter function
                elif current_choice == "Encounter":
                    self.encounter(self.main_trainer)
                # IF answer is PRINT ALIDEX call print_alidex function
                elif (current_choice == "Print Alidex"):
                    self.print_alidex()
                    time.sleep(5)
                # IF answer is PRINT TRAINER INFO call print_trainer_info function
                elif (current_choice == "Print Trainer Info"):
                    self.print_trainer_info()
                    time.sleep(5)
                # IF answer is PRINT <Alimon> INFO separate the alimon name and then call print_alimon_info on it
                # TODO: Add AliDex viewer to eliminate this choice
                elif (current_choice == "Print <Alimon> Info"):
                    print("What Alimon Would You Like To See?")
                    alimon_name = input().upper().strip()
                    self.print_alimon_info(alimon_name)
                # IF answer is BAG call create BAG function which will turn on the BAG menu
                elif (current_choice == "Bag"):
                    self.view_bag_out_battle(self.main_trainer)
                elif (current_choice == "Save"):
                    self.save_game(trainerProfile)
                # IF answer is EXIT set end_game to 1 and end the game loop
                elif (current_choice == "Exit"):
                    end_game = True
                else:
                    os.system('cls')
                    print("Sorry that is not a valid choice.")
                    time.sleep(2)

                os.system('cls')
            elif (answer == "EXIT"):
                end_game = True
                # IF answer is invalid, print a message and have them choose again
            else:
                os.system('cls')
                print("Sorry that is not a valid choice")
                time.sleep(2)
                os.system('cls')




    #---------------------------------------------------------------------------------------------------------------
    #                                          ALIMON CREATION FUNCTION
    #   @param Self
    #   @return nothing runs until it ends
    #   TODO: This function is only here for testing purposes and will be removed in the final version
    #   -Prompts user for Name, Base Level, Capture Rate, and Encounter Rate
    #   -Creates a new Alimon object and appends it to the "Ali_Dex"
    #---------------------------------------------------------------------------------------------------------------
    def alimon_creation(self, name, capture_rate, encounter_rate, level):

        self.ali_list[name] = Alimon(name, capture_rate, level)

    # ---------------------------------------------------------------------------------------------------------------
    #                                          LOAD TRAINER FUNCTION
    #   @param Self, trainer profile containing trainer info with data separated by \n
    #   @return nothing runs until it ends
    #   -Read through the file and parces the data appropriately
    #   -Creates new trainer object and points main trainer at it
    #   or
    #   -Creates new trainer from user input data
    #   -Makes main trainer point at new trainer object created from data
    # ---------------------------------------------------------------------------------------------------------------
    def load_trainer(self, trainerProfile):
        #If None gets sent, that means we started a new game!
        if (trainerProfile == None):
            print("Welcome to the world of Alimon! Are You A Boy or a Girl?")
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
            print(
                "It is very nice to meet you {name}, I am Prof. Broke. I am a researcher here in the Pokemon world. I'm sure you know how to be a trainer so here are some pokeballs and money.".format(
                    name=self.main_trainer.name))
            self.main_trainer.add_to_bag(AliBall(), 1)

            # If Trainer Profile is given, iterate through and set Trainer parameters
        else:
            trainer_info = []
            trainer_bag = {}
            trainer_bag_count = []
            trainer_team = []
            trainer_pc = []
            money = 0
            with open("trainerProfile.txt", 'r') as reader:
                for line in reader:
                    trainer_info.append(line.strip("\n"))

            # Make two new bag objects and occupy them with the contents of the 3rd and 4th line of the file
            for item in trainer_info[2].split("+"):
                if (item not in self.item_list):
                    print("You have an invalid Item")
                    return
                else:
                    trainer_bag[item] = self.item_list[item]
            for count in trainer_info[3].split("+"):
                trainer_bag_count.append(int(count))

            # Iterate through each Alimon and fill Trainer team and pc
            for alimon in trainer_info[4].split("+"):
                ali_info = alimon.strip("[]").split(",")
                name = ali_info[0]
                lvl = ali_info[1]
                exp = ali_info[2]
                is_shiny = ali_info[3]
                new_alimon = Alimon(name, self.ali_list[name].capture_rate, self.ali_list[name].encounter_rate, lvl,
                                    exp, is_shiny)
                trainer_team.append(new_alimon)

            for alimon in trainer_info[5].split("+"):
                ali_info = alimon.strip("[]").split(",")
                name = ali_info[0]
                lvl = ali_info[1]
                exp = ali_info[2]
                is_shiny = ali_info[3]
                new_alimon = Alimon(name, self.ali_list[name].capture_rate, self.ali_list[name].encounter_rate, lvl,
                                    exp, is_shiny)
                trainer_pc.append(new_alimon)
            money = int(trainer_info[6])
            self.main_trainer = Trainer(trainer_info[0], trainer_info[1], trainer_bag, trainer_bag_count, trainer_team,
                                        trainer_pc)

    # ---------------------------------------------------------------------------------------------------------------
    #                                          LOAD ALIDEX FUNCTION
    #   @param Self, alidex text file containing alimons with its base data separated by +
    #   @return nothing runs until it ends
    #   -Read through the file and parces the data appropriately
    #   -Creates new alimon object and adds to it the AliDex List
    # ---------------------------------------------------------------------------------------------------------------
    def load_alidex(self, alidex_file):
        with open(alidex_file, 'r') as reader:
            for line in reader:
                alimon = line.strip("\n").split("+")
                name = alimon[0]
                cap_rate = float(alimon[1])
                enc_rate = float(alimon[2])
                new_alimon = Alimon(name, cap_rate, enc_rate)
                self.ali_list[name] = new_alimon

    # ---------------------------------------------------------------------------------------------------------------
    #                                          SAVE GAME FUNCTION
    #   @param Self, name of file to save to
    #   @return nothing runs until it ends
    #   -Check if fileToSaveTo is empty
    #       -If yes, sets it to the default "trainerProfile.txt"
    #   -Prompts user if they want to save over the file
    #       -If yes, writes all info of current main trainer into specified file in correct format
    #       -If no, returns to main menu
    #       -Repeat prompt for every other answer
    # ---------------------------------------------------------------------------------------------------------------
    def save_game(self, fileToSaveTo):
        exit = 0
        while(exit == 0):
            if(fileToSaveTo== None):
                fileToSaveTo = "trainerProfile.txt"
            print("Are You Sure You Wnat to Save To: " + fileToSaveTo + "?(yes/no)")
            try:
                answer = input().upper().strip()
            except:
                print("That is not a valid choice")
            if(answer == "YES"):
                with open(fileToSaveTo, 'w') as filetowrite:
                    print(self.main_trainer.trainer_info)
                    for each in self.main_trainer.trainer_info:

                        if(type(each) ==type([])):
                            newStr = ""
                            for item in each:
                                if(isinstance(item, Alimon)):
                                    newStr += "[{name},{lvl},{exp},{isShiny}]".format(name=item.name,lvl=item.level,exp=item.exp,isShiny=item.is_shiny) + "+"
                                else:
                                    newStr += str(item) + "+"
                            newStr = newStr.rstrip("+")
                            filetowrite.write(newStr + "\n")
                        elif(type(each) == type({})):
                            newStr = ""
                            for item in each.keys():
                                newStr += str(item) + "+"
                            newStr = newStr.rstrip("+")
                            filetowrite.write(newStr + "\n")
                        else:
                            filetowrite.write(str(each) + "\n")
                print("Save Successful! ")
                exit = 1
            elif(answer == "NO"):
                exit = 1
            else:
                print("Sorry that is not a valid choice.")

    # ---------------------------------------------------------------------------------------------------------------
    #                                          LOAD ITEM LIST FUNCTION
    #   @param Self, item list file containing items with its base data separated by +
    #   @return nothing runs until it ends
    #   -Read through the file and parces the data appropriately
    #   -Creates new item object and adds to it the item list
    #   -AliBalls are special and require a change to its multipliers
    # ---------------------------------------------------------------------------------------------------------------
    def load_item_list(self, item_list):
        with open(item_list, 'r') as reader:
            for line in reader:
                item = line.split("+")
                name = item[0]
                type = item[1]
                desc = item[2]
                cost = int(item[3])
                if(type == "BALL"):
                    multi = float(item[4])
                    new_item = AliBall(name,type, desc, cost)
                    new_item.capture_rate_multiplier = multi
                else:
                    new_item = Item(name,type,desc,cost)

                self.item_list[name] = new_item
    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT ALIDEX FUNCTION
    #   @param Self
    #   @return nothing runs until it ends
    #   -Checks if Length of Pokedex is > 0
    #       -If Yes, Prints All Keys in the "ali_list" dictionary
    #       -If No, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def print_alidex(self):
        if (len(self.ali_list) == 0):
            print("Oh no! Your Alidex is Empty, Go Create Some!")
        else:
            for key, value in self.ali_list.items():
                print(key + " Capture Rate" + str(self.ali_list[key].capture_rate))

    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT TRAINER INFO FUNCTION
    #   @param Self
    #   @return nothing runs until it ends
    #   -Prints Main Trainer info
    # ---------------------------------------------------------------------------------------------------------------
    def print_trainer_info(self):
        print(self.main_trainer)

    # ---------------------------------------------------------------------------------------------------------------
    #                                          PRINT ALIMON INFO FUNCTION
    #   @param Self and Alimon "name"
    #   @return nothing runs until it ends
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
    #   @param Self and trainer as a parameter
    #   @return nothing runs until it ends
    #   -Creates a new Weighted list consisting of all Alimons in the Alidex and their respective encounter rates
    #   -Chooses an Alimon from the Alidex randomly with weighted values
    #   -Create new Alimon object for trainer to interact with
    #   -Opens a Menu prompting the User to choose what action they would like to do
    #       -If Battle (WIP)
    #       -If BAG call the view bag in battle function
    #           -View Bag Function can determine if encounter ends or not
    #       -If RUN, make correct choice = 1 and then return them to the last menu
    #       -If invalid choice, prints error message and promps them again about the encounter.
    # ---------------------------------------------------------------------------------------------------------------
    def encounter(self, trainer):

        #Create new Alimon For Trainer to battle or catch
        weighted_list = []
        for alimon in self.ali_list:
            weighted_list.append(self.ali_list[alimon].encounter_rate)
        encountered_alimon = self.ali_list[self.random_choice(self.ali_list, weighted_list, 1)[0]]
        is_shiny = self.random_choice([True, False], [encountered_alimon.shiny_rate,1-encountered_alimon.shiny_rate], 1)[0]
        level = self.random_choice(range(1,51), None, 1)[0]
        new_alimon = Alimon(encountered_alimon.name, self.ali_list[encountered_alimon.name].capture_rate,self.ali_list[encountered_alimon.name].encounter_rate, level)
        new_alimon.is_shiny = is_shiny
        print(new_alimon)

        #Prompt Trainer
        correct_choice = 0
        while (correct_choice == 0):
            shiny_prompt = ""
            if(is_shiny):
                shiny_prompt = " AND ITS SHINY!!!"
            print("You Have Encountered {name} lvl {level}! What Would You Like To Do?".format(name=new_alimon.name, level= level) + shiny_prompt)
            print("Battle (not Implemented)\nBag\nRun")
            try:
                answer = input().upper().strip()
            except:
                os.system('cls')
                print("That is not a valid option try again")
                time.sleep(2)
                os.system('cls')
            if (answer == "BATTLE"):
                os.system('cls')
                print("Sorry this has not been implemented yet, please RUN or BAG")
                time.sleep(2)
                os.system('cls')
            elif (answer == "BAG"):
                os.system('cls')
                end_battle = self.view_bag_in_battle(trainer, None, new_alimon)
                if(end_battle):
                    correct_choice=1
            elif (answer == "RUN"):
                correct_choice = 1
            else:
                os.system('cls')
                print("Sorry that is not a valid option, please choose something else")
                time.sleep(2)
                os.system('cls')

    # ---------------------------------------------------------------------------------------------------------------
    #                                          VIEW BAG OUT OF BATTLE FUNCTION
    #   @param Self, and current Trainer
    #   @return nothing, runs until it ends
    #   -Checks bag is empty
    #       -If No, Prints All Items In Bag with count > 0 and a pointer to currently selected item
    #           -Prompts user to navigate the menu or go back
    #           -Selector symbol will move accordingly to user input
    #       -If Yes, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def view_bag_out_battle(self, trainer):
        #Empty bag Check
        if (len(trainer.bag) == 0):
            os.system('cls')
            print("Oh no! Your Bag is Empty, Go Create Some!")
            time.sleep(2)
            os.system('cls')
        else:
            #Bag contents printing logic
            num_of_items_in_bag = len(trainer.bag)
            choice_num = 0
            select_num = 0
            current_item_count = 0
            finish_view = False
            while (not finish_view):
                # Basically for every item if choice_num (User hovering certain item) and select_num (current item being iterated on) match, then it will print a ">" otherwise it prints it normally
                for key, value in trainer.bag.items():
                    if (select_num == choice_num):
                        print(">{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.get_item_count(value)))
                        choice_num += 1
                        current_item = trainer.bag[key]
                        current_item_count = trainer.get_item_count(value)
                    else:
                        print("{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.get_item_count(value)))
                        choice_num += 1
                choice_num = 0
                print("Back\n")
                print("---------------------------------------------------------------------------------------")
                print(current_item.desc)
                print("---------------------------------------------------------------------------------------")
                print("What would you like to do? \nDOWN \nUP \nUSE \nBACK")

                #USER INPUT LOGIC
                try:
                    answer = input().strip().upper()
                except:
                    os.system('cls')
                    print("That is not a valid choice.")
                    time.sleep(2)
                    os.system('cls')
                if (answer == "DOWN"):
                    if (select_num == num_of_items_in_bag - 1):
                        select_num = 0
                        os.system('cls')
                    else:
                        select_num += 1
                        os.system('cls')
                elif (answer == "UP"):
                    if (select_num == 0):
                        select_num = num_of_items_in_bag - 1
                        os.system('cls')
                    else:
                        select_num -= 1
                        os.system('cls')
                elif (answer == "USE"):
                    print(current_item.name)
                    #Calls the use item function on the current item selected
                    self.use_item(current_item, False)
                elif (answer == "BACK"):
                    return False
                else:
                    os.system('cls')
                    print("Sorry that is not a valid choice.")
                    time.sleep(2)
                    os.system('cls')


    # -----------------------------------------------------------------------------------------------------------------------------
    #                                          VIEW BAG IN BATTLE FUNCTION
    #   -This function is essentially an overloaded View Bag Out Of Battle function that is used specifically for catching Alimons
    #   @param Self, current Trainer, current active Alimon, and current opposing Alimon
    #   @return nothing, runs until it ends
    #   -Checks bag is empty
    #       -If No, Prints All Items In Bag with a pointer to currently selected item
    #           -Prompts user to navigate the menu or go back
    #           -Selector symbol will move accordingly to user input
    #       -If Yes, Prints error message and sends them back to the last menu
    # -----------------------------------------------------------------------------------------------------------------------------
    def view_bag_in_battle(self, trainer, current_active_alimon, current_opp_alimon):
        #Empty Bag Check
        if (len(trainer.bag) == 0):
            print("Oh no! Your Bag is Empty, Go Create Some!")
        else:
            #Bag contents printing logic
            num_of_items_in_bag = len(trainer.bag)
            choice_num = 0
            select_num = 0
            current_item_count = 0
            finish_view = False
            while (not finish_view):
                #Basically for every item if choice_num (User hovering certain item) and select_num (current item being iterated on) match, then it will print a ">" otherwise it prints it normally
                for key, value in trainer.bag.items():
                    if (select_num == choice_num):
                        print(">{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.get_item_count(value)))
                        choice_num += 1
                        current_item = trainer.bag[key]
                        current_item_count = trainer.get_item_count(value)
                    else:
                        print("{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.get_item_count(value)))
                        choice_num += 1
                choice_num = 0
                print("Back\n")
                print("---------------------------------------------------------------------------------------")
                print(current_item.desc)
                print("---------------------------------------------------------------------------------------")
                print("What would you like to do? \nDOWN \nUP \nUSE \nBACK")

                #USER INPUT LOGIC
                try:
                    answer = input().strip().upper()
                except:
                    os.system('cls')
                    print("That is not a valid choice.")
                    time.sleep(2)
                    os.system('cls')
                if (answer == "DOWN"):
                    if (select_num == num_of_items_in_bag - 1):
                        select_num = 0
                        os.system('cls')
                    else:
                        select_num += 1
                        os.system('cls')
                elif (answer == "UP"):
                    if (select_num == 0):
                        select_num = num_of_items_in_bag - 1
                        os.system('cls')
                    else:
                        select_num -= 1
                        os.system('cls')
                elif (answer == "USE"):
                    print(current_item.name)
                    #catch_bool is used to check if trainer is attempting to catch an Alimon
                    catch_bool = self.use_item(current_item, True)

                    #Caught is here to see if the battle needs to end
                    caught = False

                    #If Trainer is attempting to catch an Alimon, call the catching function
                    if (catch_bool):
                        caught = self.catching_alimon(current_item, current_opp_alimon, trainer)

                    return caught
                elif (answer == "BACK"):
                    return False
                else:
                    os.system('cls')
                    print("Sorry that is not a valid choice.")
                    time.sleep(2)
                    os.system('cls')


    # ---------------------------------------------------------------------------------------------------------------
    #                                          USE ITEM FUNCTION
    #   @param self, item trying to be used, and if we are currently in an encounter
    #   @return currently returns True if Ball was used, False if not
    #   TODO: make item logic for other items (healing, key items, etc)
    #   -Checks what type of item is being used and correctly uses that item
    #       -If item is a ball and can be used, the function returns true so we can call the catch function
    #   -After successful use, subtract 1x from item count and return
    # ---------------------------------------------------------------------------------------------------------------
    def use_item(self, item, in_encounter):
        if(item.type == "BALL"):
            if(in_encounter == False):
                os.system('cls')
                print("Sorry You Cannot Use That Item Right Now.")
                time.sleep(2)
                os.system('cls')
                return False
            else:
                self.main_trainer.remove_item(item, 1)
                return True

    # ---------------------------------------------------------------------------------------------------------------
    #                                          CATCH ALIMON FUNCTION
    #   @param self, item trying to be used, trainer, alimon that needs to be caught
    #   @return True or False depending on if Alimon is caught
    #   -First decides if alimon will be caught using random generator based on the alimon's capture rate
    #       -If Yes, will print shake 4 times and print respective message and returns true
    #       -If No
    #           -Randomly chooses a number of shakes
    #           -Prints respective message
    #
    # ---------------------------------------------------------------------------------------------------------------
    def catching_alimon(self, item, alimon, trainer):

        #Decide wether or not the Alimon is caught using it's capture rate multiplied by Ball multiplier
        caught_bool = self.random_choice([True, False], [alimon.capture_rate * item.capture_rate_multiplier, 1 - (alimon.capture_rate * item.capture_rate_multiplier)],1)[0]
        os.system('cls')
        print("{name} used {item}!".format(name = trainer.name, item = item.name))
        time.sleep(1)
        #Instantiate a message list
        catch_message = ["Not Even Close Bro", "Oops Try Again", "Close But No Sauce", "Lmao You Thought", "WE CAUGHT {alimon_name}!".format(alimon_name= alimon.name)]

        #If caught_bool ends up false, simulate ball shakes and print respective message
        if(caught_bool == False):
            num_shakes = random.randint(0,3)
            shake = 0
            while(shake < num_shakes):
                time.sleep(2)
                print("*shake*")
                shake+=1
            time.sleep(2)
            print(catch_message[num_shakes])
            time.sleep(2)
            os.system('cls')
            return False

        #If caught_bool ends up True, shake 3 times and click to simulate capture, then append new Alimon object to Trainers team or PC
        else:
            shake = 0
            while (shake < 3):
                time.sleep(2)
                print("*shake*")
                shake+=1
            time.sleep(2)
            print("*CLICK")
            time.sleep(2)
            print(catch_message[4])
            time.sleep(2)
            if(len(trainer.ali_team) < 7):
                print("{alimon} has been added to your team!".format(alimon = alimon.name))
                trainer.ali_team.append(alimon)
            else:
                print("You Dont Have Enough Space On Your Team, {alimon} has been sent to your PC".format(alimon = alimon.name))
                trainer.pc.append(alimon)

            time.sleep(4)
            os.system('cls')
            return True

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                          RANDOM CHOICE FUNCTION
    #   @param self, target list you want to choose from, optional weighted list if you want the values weight, and then the number of choices you want picked
    #   @return list containing the random choice(s) chosen
    #   -If target list is empty or num of choices = 0, print an error
    #   -Else uses random.choices() to pick k values from target_list using weights from weight_list and returns them.
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    def random_choice(self, target_list, weighted_list, num_of_choices):
        if(len(target_list) == 0):
            os.system('cls')
            print("Your list is empty")
            time.sleep(2)
            os.system('cls')
        elif(num_of_choices == 0):
            os.system('cls')
            print("Please specify how many choices you want")
            time.sleep(2)
            os.system('cls')
        else:
            return random.choices(list(target_list), weights=weighted_list, k=num_of_choices)