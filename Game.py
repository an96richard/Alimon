from Trainer import Trainer
from Alimon import Alimon
from Item import Item
from AliBall import AliBall
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
#TODO:  IMPLEMENT SAVE AND LOAD, FULL ALIDEX, BATTLE SYSTEM, OTHER ITEMS, EXP SYSTEM
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
    ali_list = {"MEW": Alimon("MEW", 0.345, 1), "POOP": Alimon("POOP", 0.03, 999)}
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
        self.main_trainer.add_to_bag(AliBall(), 1)



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
                elif (current_choice == "Print <Alimon> Info"):
                     print("What Alimon Would You Like To See?")
                     alimon_name = input().upper().strip()
                     self.print_alimon_info(alimon_name)
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
    #   @param Self
    #   @return nothing runs until it ends
    #   TODO: This function is only here for testing purposes and will be removed in the final version
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
                print(key)

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
                print("That is not a valid option try again")
            if (answer == "BATTLE"):
                print("Sorry this has not been implemented yet, please RUN or BAG")
            elif (answer == "BAG"):
                end_battle = self.view_bag_in_battle(trainer, True, None, new_alimon)
                if(end_battle):
                    correct_choice=1
            elif (answer == "RUN"):
                correct_choice = 1
            else:
                print("Sorry that is not a valid option, please choose something else")

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
            print("Oh no! Your Bag is Empty, Go Create Some!")
        else:
            #Bag contents printing logic
            num_of_items_in_bag = len(trainer.bag)
            choice_num = 0
            select_num = 0
            finish_view = False
            while (not finish_view):
                # Basically for every item if choice_num (User hovering certain item) and select_num (current item being iterated on) match, then it will print a ">" otherwise it prints it normally
                for key, value in trainer.bag.items():
                    if (select_num == choice_num):
                        print(">{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.bag[key].count))
                        choice_num += 1
                        current_item = trainer.bag[key]
                    else:
                        print("{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.bag[key].count))
                        choice_num += 1
                choice_num = 0
                print("Back\n")
                print("---------------------------------------------------------------------------------------")
                print(current_item.desc + "\n")
                print("---------------------------------------------------------------------------------------")
                print("What would you like to do? \nDOWN \nUP \nUSE \nBACK")

                #USER INPUT LOGIC
                try:
                    answer = input().strip().upper()
                except:
                    print("That is not a valid choice.")
                if (answer == "DOWN"):
                    if (select_num == num_of_items_in_bag - 1):
                        select_num = 0
                    else:
                        select_num += 1
                elif (answer == "UP"):
                    if (select_num == 0):
                        select_num = num_of_items_in_bag - 1
                    else:
                        select_num -= 1
                elif (answer == "USE"):
                    print(current_item.name)
                    #Calls the use item function on the current item selected
                    self.use_item(current_item, False)
                    #If the current item's count == 0, pop it from the list so it doesnt get printed
                    if (current_item.count == 0):
                        trainer.bag.pop(current_item.name)
                elif (answer == "BACK"):
                    return False
                else:
                    print("Sorry that is not a valid choice.")



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
            finish_view = False
            while (not finish_view):
                #Basically for every item if choice_num (User hovering certain item) and select_num (current item being iterated on) match, then it will print a ">" otherwise it prints it normally
                for key, value in trainer.bag.items():
                    if (select_num == choice_num):
                        print(">{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.bag[key].count))
                        choice_num += 1
                        current_item = trainer.bag[key]
                    else:
                        print("{choice_num}.".format(choice_num=choice_num) + key + "            x" + str(
                            trainer.bag[key].count))
                        choice_num += 1
                choice_num = 0
                print("Back\n")
                print("---------------------------------------------------------------------------------------")
                print(current_item.desc + "\n")
                print("---------------------------------------------------------------------------------------")
                print("What would you like to do? \nDOWN \nUP \nUSE \nBACK")

                #USER INPUT LOGIC
                try:
                    answer = input().strip().upper()
                except:
                    print("That is not a valid choice.")
                if (answer == "DOWN"):
                    if (select_num == num_of_items_in_bag - 1):
                        select_num = 0
                    else:
                        select_num += 1
                elif (answer == "UP"):
                    if (select_num == 0):
                        select_num = num_of_items_in_bag - 1
                    else:
                        select_num -= 1
                elif (answer == "USE"):
                    print(current_item.name)
                    #catch_bool is used to check if trainer is attempting to catch an Alimon
                    catch_bool = self.use_item(current_item, True)

                    #Caught is here to see if the battle needs to end
                    caught = False

                    #If Trainer is attempting to catch an Alimon, call the catching function
                    if (catch_bool):
                        caught = self.catching_alimon(current_item, current_opp_alimon, trainer)

                    #If the item count is now equal to 0, pop it from the list so it doesnt print
                    if (current_item.count == 0):
                        trainer.bag.pop(current_item.name)

                    return caught
                elif (answer == "BACK"):
                    return False
                else:
                    print("Sorry that is not a valid choice.")


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
                print("Sorry You Cannot Use That Item Right Now.")
                return False
            else:
                self.main_trainer.bag[item.name].count -= 1
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
        print("{name} used {item}!".format(name = trainer.name, item = item.name))
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
            if(len(trainer.poke_team) < 7):
                print("{alimon} has been added to your team!".format(alimon = alimon.name))
                trainer.poke_team.append(alimon)
            else:
                print("You Dont Have Enough Space On Your Team, {alimon} has been sent to your PC".format(alimon = alimon.name))
                trainer.pc.append(alimon)

            time.sleep(2)
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
            print("Your list is empty")
        elif(num_of_choices == 0):
            print("Please specify how many choices you want")
        else:
            return random.choices(list(target_list), weights=weighted_list, k=num_of_choices)