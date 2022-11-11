from Trainer import Trainer
from Alimon import Alimon
from AliBall import AliBall
from Attack import Attack
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
#
#version 0.099
#CHANGE LOG 11/11/2022
#   Finished most of the Battle Logic
#       -Implemented Turned Based Battle
#       -Implemented Damage Calculations
#       -Implemented Fainted check
#   Fixed Bug in Generate Alimon function to give it correct stats
#   TODO: Finish battle logic for stat changes, finish EXP calculations for after battle procedures
#
#version 0.095
#CHANGE LOG 11/3/2022
#   Added growth rate, currentHP, attack_list to Alimon Object
#   Added implmentation for saving and loading new features added to the Alimon object
#   Added Generate Random Alimon Function in order to do so on command
#   Added logic for printing alimon encounters
#
#   TODO: Battle Logic
#version 0.09
#CHANGE LOG 11/1/2022
#   Added stats to Alimon
#   Added implmentation for saving and loading stats
#   Added function to load list of attacks to use as reference for later
#   Added pseudo code for other functions at the bottom
#   Added new file named AttackList to be used to store attack data
#   Add new Attack class to represent attack objects

#   TODO:Add attacks to Alimons and start working on battle logic
#   Notes:
#   Unsure if version is stable or not. Due to lack of Sleep I will be testing it tomorrow.
#
#BUGFIX:
#Fixed a bug in view party that listed the wrong options after switching alimons
#
#version 0.085
#CHANGE LOG 10/26/2022
#   Further developed view party with some changes and bug fixes
#   Added switch Alimon function in both Encounter and View Party functions to allow user to switch order of their Ali-Team
#
#version 0.08
#CHANGE LOG 10/25/2022
#   Added a view party function to allow users to look at all Alimon in currently in their "party"
#   Function works to display and allow users to select a specific Alimon and inspect it
#   Needs supporting functions to be implemented to switch order of Alimon, use items on them, and display important information (stats, desc, traits etc)
#
#
#version 0.07
#CHANGE LOG 10/18/2022
#   Added Save and Load functions and 3 text files containing meta data and trainer profile
#   Added 3 more Balls that will be usable in the future.
#   Implmented logic on reading saves and having a universal alidex and item list
#   Fixed all other functions to work correctly with newly added loading function
#   Cleaned up printing logic to make it look like an actual text game.
#
#version 0.05
#CHANGE LOG 10/17/2022
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
#TODO: PARTY MECHANIC, FULL ALIDEX, BATTLE SYSTEM, OTHER ITEMS, EXP SYSTEM
#
#
#CURRENTLY IN PROGRESS: BATTLE MECHANIC
#
#1.Create Encounter Logic
#   -Party Mechanic
#       -Pretty now? Pretty Later?? IDK MAN
#       -View Party
#           -In Battle
#           -Out Of Battle
#       -Alimon Options
#           -Switch (CHECK)
#           -Item
#           -View Info (CHECK)
#           -Release
#       -HP
#       -EXP Gain
#
#2. Alimon Center
#       -Heal All Alimon in Party
#3.Items
#   -Use Items
#   -Balls
#      -Different Balls
#   -Potions
#   -Misc
#   -Key Items
#
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
    menu_choices = ["Party","Print Alidex" , "Encounter" ,"Print Trainer Info","Print <Alimon> Info" ,"Bag","Save","Exit"]
    item_list = {}
    attack_list = {}
    main_trainer = None
    in_encounter = False
    def __init__(self, trainerProfile, itemDex, alimonDex, attackList):
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
        self.load_attack_list(attackList)
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
                if current_choice == "Party":
                    self.view_party()
                # IF answer is ENCOUNTER call encounter function
                elif current_choice == "Encounter":
                    self.encounter(self.main_trainer)
                    self.in_encounter = False
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
                currenthp = ali_info[2]
                exp = ali_info[3]
                is_shiny = (ali_info[4] == "True")
                stats = ali_info[5].strip("[]").split("?")
                print(stats)
                newStatDict = {}
                newStatDict["health"] = int(stats[0])
                newStatDict["attack"] = int(stats[1])
                newStatDict["defense"] = int(stats[2])
                newStatDict["sp.atk"] = int(stats[3])
                newStatDict["sp.def"] = int(stats[4])
                newStatDict["speed"] = int(stats[5])
                newStatDict["accuracy"] = int(stats[6])
                atks = ali_info[6].strip("[]").split("?")
                growth_rate = self.ali_list[name].growth_rate
                new_alimon = Alimon(name, float(self.ali_list[name].capture_rate), float(self.ali_list[name].encounter_rate), newStatDict,atks, growth_rate, (lvl),
                                    int(exp), is_shiny, currenthp=int(currenthp))
                trainer_team.append(new_alimon)

            for alimon in trainer_info[5].split("+"):
                ali_info = alimon.strip("[]").split(",")
                name = ali_info[0]
                lvl = ali_info[1]
                currenthp = ali_info[2]
                exp = ali_info[3]
                is_shiny = bool(ali_info[4])
                stats = ali_info[5].strip("[]").split("?")
                newStatDict = {}
                newStatDict["health"] = int(stats[0])
                newStatDict["attack"] = int(stats[1])
                newStatDict["defense"] = int(stats[2])
                newStatDict["sp.atk"] = int(stats[3])
                newStatDict["sp.def"] = int(stats[4])
                newStatDict["speed"] = int(stats[5])
                newStatDict["accuracy"] = int(stats[6])
                atks = ali_info[6].strip("[]").split("?")
                growth_rate = self.ali_list[name].growth_rate
                new_alimon = Alimon(name, float(self.ali_list[name].capture_rate), float(self.ali_list[name].encounter_rate), newStatDict, atks,growth_rate, int(lvl),
                                    int(exp), is_shiny,currenthp=int(currenthp))
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
                base_stats = alimon[3].strip("[]").split(",")
                base_stat_dict = {}
                base_stat_dict["health"] = int(base_stats[0])
                base_stat_dict["attack"] = int(base_stats[1])
                base_stat_dict["defense"] = int(base_stats[2])
                base_stat_dict["sp.atk"] = int(base_stats[3])
                base_stat_dict["sp.def"] = int(base_stats[4])
                base_stat_dict["speed"] = int(base_stats[5])
                base_stat_dict["accuracy"] = int(base_stats[6])
                growth_rate = alimon[4].strip("[]").split(",")
                new_alimon = Alimon(name, cap_rate, enc_rate,stats=base_stat_dict,growth_rate=growth_rate)
                self.ali_list[name] = new_alimon

    # ---------------------------------------------------------------------------------------------------------------
    #                                          LOAD ATTACK LIST FUNCTION
    #   @param Self, attackdex file containing info about possible attacks to use
    #   @return nothing runs until it ends
    #   -Read through the file and parces the data appropriately
    #   -Creates new attack object and stores it in attack_list dict to be used later
    # ---------------------------------------------------------------------------------------------------------------
    def load_attack_list(self, attackdex_file):
        with open(attackdex_file, 'r') as reader:
            for line in reader:
                attack = line.strip("\n").split("+")
                name = attack[0]
                type = attack[1]
                damage = int(attack[2])
                accuracy = float(attack[3])
                stat_change = attack[4]
                description = attack[5]
                self.attack_list[name] = Attack(name=name,type=type,damage=damage,accuracy=accuracy,stat_change=stat_change,description=description)
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
                                    statStr = "[{stat1}?{stat2}?{stat3}?{stat4}?{stat5}?{stat6}?{stat7}]".format(stat1 = item.stats["health"],stat2 = item.stats["attack"],stat3 = item.stats["defense"],stat4 = item.stats["sp.atk"],stat5 = item.stats["sp.def"],stat6 = item.stats["speed"],stat7 = item.stats["accuracy"])
                                    atkList = "[{atk1}?{atk2}?{atk3}?{atk4}]".format(atk1 = item.attack_list[0],atk2 = item.attack_list[1],atk3 = item.attack_list[2],atk4 = item.attack_list[3])
                                    newStr += "[{name},{lvl},{hp},{exp},{isShiny},{stats},{atkList}]".format(name=item.name,lvl=item.level,exp=item.exp,isShiny=item.is_shiny,stats = statStr, atkList = atkList, hp= item.currenthp) + "+"
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
                print("Save Successful!")
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
    #                                          VIEW PARTY FUNCTION
    #   @param Self and optional swap position if user wants to swap alimon
    #   @return nothing runs until it ends or party is empty
    #   -Print out main trainer's Ali team with name and level
    #   -If user selects an Alimon options will appear allowing user to manipulate selected Alimon
    #   -If in-encounter is TRUE different options will be available for each Alimon
    # ---------------------------------------------------------------------------------------------------------------
    def view_party(self, swap_position=None, force_swap = False):
        os.system('cls')
        num_of_alimon = len(self.main_trainer.ali_team)
        if(num_of_alimon == 0):
            print("Sorry You Do Not Have Any Alimons! Go Encounter Alimons in the Wild!")
            time.sleep(2)
            os.system('cls')
            return


        #This portion of the code is used to print out the current Alimon in the party and let user choose which Alimon they want to navigate and manipulate. INFO/SUMMARY/SWITCH
        #=============================================================================================================================================================================================
        choice_num = 1
        select_num = 1
        end_party_view = False
        while (not end_party_view):
            # PARTY PRINTING LOGIC
            for box in range(0,6):
                if(box < num_of_alimon):
                    if (select_num == choice_num):
                        print(">{choice_num}. {alimon}    lvl{lvl}".format(choice_num=choice_num, alimon = self.main_trainer.ali_team[box].name, lvl = self.main_trainer.ali_team[box].level))
                        choice_num += 1
                        current_alimon = self.main_trainer.ali_team[box]
                    else:
                        print("{choice_num}. {alimon}    lvl{lvl}".format(choice_num=choice_num, alimon = self.main_trainer.ali_team[box].name, lvl = self.main_trainer.ali_team[box].level))
                        choice_num += 1
                else:
                    print(str(choice_num) + ".")
                    choice_num+=1
            choice_num = 1
            if(swap_position == None):
                print("What will you do now? (DOWN, UP, ENTER, BACK)")
            else:
                print("Which Alimon Do You Want TO Swap With?")
            # Try to turn input uppercase
            try:
                answer = input().upper().strip()
            except:
                os.system('cls')
                print("That is not a valid choice")
                time.sleep(2)
                os.system('cls')
            if (answer == "DOWN"):
                if (select_num == num_of_alimon):
                    select_num = 1
                    os.system('cls')
                else:
                    select_num += 1
                    os.system('cls')
            elif (answer == "UP"):
                if (select_num == 1):
                    select_num = num_of_alimon
                    os.system('cls')
                else:
                    select_num -= 1
                    os.system('cls')
            elif (answer == "ENTER"):
                os.system('cls')
                menu_choices = []
                #If trainer is currently in an encounter
                if(self.in_encounter):
                    # If user is selecting the first alimon in the party and is not trying to swap
                    if(select_num == 1 and swap_position == None):
                        menu_choices = ["Item", "Summary", "Back"]
                    # If your alimon fainted and needs to be swapped out immediately
                    elif(self.main_trainer.ali_team[select_num-1].currenthp == 0):
                        os.system('cls')
                        print("You Cannot Send Out An Alimon with 0HP!")
                        time.sleep(2)
                        os.system('cls')
                    # If the selected alimon is being swapped with itself
                    elif(select_num == swap_position):
                        os.system('cls')
                        print("You Cannot Swap This Alimon with Itself")
                        time.sleep(2)
                        os.system('cls')
                        continue
                    # If the selected alimon is not the first alimon in the party
                    elif(swap_position == None):
                        menu_choices = ["Item", "Summary", "Switch", "Back"]
                    # If the user is swapping two Alimons
                    else:
                        self.swap_alimon_position(select_num-1, swap_position-1)
                        return
                else:
                    # If the selected alimon is being swapped with itself
                    if (select_num == swap_position):
                        os.system('cls')
                        print("You Cannot Swap This Alimon with Itself")
                        time.sleep(2)
                        os.system('cls')
                        continue
                    # If the selected alimon is not the first alimon in the party
                    elif (swap_position == None):
                        menu_choices = ["Item", "Summary", "Move", "Back"]
                    # If the user is swapping two Alimons
                    else:
                        self.swap_alimon_position(select_num - 1, swap_position - 1)
                        return


                #This inner portion is within the elif where ANSWER is equal to "ENTER". It prints out the options that the user can choose for the currently selected Alimon
                #--------------------------------------------------------------------------------------------------------------------------------------------------------------
                num_of_menu_choices = len(menu_choices)
                choice = 1
                select = 1
                end_alimon_party_view = False
                while (not end_alimon_party_view):
                    # VIEWING OPTIONS FOR ALIMON DURING PARTY VIEW PRINTING LOGIC
                    if (current_alimon.is_shiny == True):
                        print("===========================================")
                        print("|       *{choice}          lvl {lvl}      |".format(choice=current_alimon.name,lvl=current_alimon.level))
                        print("===========================================")
                    else:
                        print("===========================================")
                        print("|       {choice}          lvl {lvl}       |".format(choice=current_alimon.name,lvl=current_alimon.level))
                        print("===========================================")
                    for option in menu_choices:
                        if (select == choice):
                            print(">".format(choice_num=choice) + option)
                            choice += 1
                            curr_choice = option
                        else:
                            print(option)
                            choice += 1
                    choice = 1
                    print("What will you do now? (DOWN, UP, ENTER, BACK)")
                    # Try to turn input uppercase
                    try:
                        answer = input().upper().strip()
                    except:
                        os.system('cls')
                        print("That is not a valid choice")
                        time.sleep(2)
                        os.system('cls')
                    if (answer == "DOWN"):
                        if (select == num_of_menu_choices):
                            select = 1
                            os.system('cls')
                        else:
                            select += 1
                            os.system('cls')
                    elif (answer == "UP"):
                        if (select == 1):
                            select = num_of_menu_choices
                            os.system('cls')
                        else:
                            select -= 1
                            os.system('cls')
                    #TODO: Make  view_bag_with_alimon/switch_alimon method. Redo print Alimon info to print more things.
                    elif (answer == "ENTER"):
                        os.system('cls')
                        if(curr_choice == "Item"):
                            self.view_bag_with_alimon(current_alimon)
                        elif(curr_choice == "Summary"):
                            self.print_alimon_info(current_alimon, select_num-1, self.main_trainer)
                        elif(curr_choice == "Switch"):
                            if(force_swap == True):
                                self.swap_alimon_position(select_num-1, 0)
                                os.system('cls')
                                print("You sent out {alimon}!".format(alimon=current_alimon.name))
                                time.sleep(2)
                                os.system('cls')
                                return
                            else:
                                self.view_party(select_num)
                                os.system('cls')
                                print("You sent out {alimon}!".format(alimon = current_alimon.name))
                                time.sleep(2)
                                os.system('cls')
                                return
                        elif(curr_choice == "Move"):
                            self.view_party(select_num)
                            return
                        elif(curr_choice == "Back"):
                            end_alimon_party_view = True
                    elif (answer == "BACK"):
                        end_alimon_party_view = True
                        os.system('cls')
                    else:
                        os.system('cls')
                        print("Sorry that is not a valid choice")
                        time.sleep(2)
                        os.system('cls')
                    #-------------------------------------------------------------------------------------------------------------------------
            elif (answer == "BACK"):
                end_party_view = True
                os.system('cls')
            # IF answer is invalid, print a message and have them choose again
            else:
                os.system('cls')
                print("Sorry that is not a valid choice")
                time.sleep(2)
                os.system('cls')
            #==================================================================================================================================================



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
    def print_alimon_info(self, alimon, ali_postion=0, trainer=None):
        if (self.ali_list.get(alimon.name) != None):
            print("================================")
            print("|          {alimon}            |".format(alimon =alimon.name))
            print("================================")
            print("--------------------------------------------------------------------------------------------\n")
            if(trainer == None):
                print(self.ali_list[alimon.name])
            else:
                selected_alimon = trainer.ali_team[ali_postion]
                print(trainer.ali_team[ali_postion])
                print("********Stats********")
                print("*HP:           {HP}".format(HP=selected_alimon.stats["health"]))
                print("*Attack:           {atk}".format(atk = selected_alimon.stats["attack"]))
                print("*Defense:          {defense}".format(defense= selected_alimon.stats["defense"]))
                print("*Sp.Atk:           {spatk}".format(spatk = selected_alimon.stats["sp.atk"]))
                print("*Sp.Def:           {spdef}".format(spdef = selected_alimon.stats["sp.def"]))
                print("*Speed:            {speed}".format(speed =selected_alimon.stats["speed"]))
                print("*Accuracy:         {accuracy}".format(accuracy= selected_alimon.stats["accuracy"]))
                print("*********************")
                print("<     Attacks     >")
                print("     {attack1}     ".format(attack1 = selected_alimon.attack_list[0]))
                print("     {attack2}     ".format(attack2=selected_alimon.attack_list[1]))
                print("     {attack3}     ".format(attack3=selected_alimon.attack_list[2]))
                print("     {attack4}     ".format(attack4=selected_alimon.attack_list[3]))


            print("--------------------------------------------------------------------------------------------")
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
        self.in_encounter = True
        new_alimon = self.generate_random_alimon()


        shiny_prompt = ""
        if (new_alimon.is_shiny):
            shiny_prompt = " AND ITS SHINY!!!"
        print("You Have Encountered {name} lvl {level}! What Would You Like To Do?".format(name=new_alimon.name, level=new_alimon.level) + shiny_prompt)
        time.sleep(2)
        os.system('cls')


        #Prompt Trainer
        correct_choice = 0
        while (correct_choice == 0):
            #Sets primary Alimon to the first index
            alimons_that_battled = []
            curr_alimon_index = 0
            curTrainerAlimon = trainer.ali_team[curr_alimon_index]
            # If all Alimons have fainted, black out trainer and return them to main menu
            if(curr_alimon_index > len(trainer.ali_team)):
                print("You Blacked Out!")
                return
            # If the first index Alimon has 0 HP set next Alimon as primary

            while(curTrainerAlimon.currenthp == 0):
                curr_alimon_index+=1
                continue

            if(curTrainerAlimon not in alimons_that_battled):
                alimons_that_battled.append(curTrainerAlimon)
            print("                                    ********{opp_alimon} lvl{lvl}*********".format(opp_alimon=new_alimon.name,lvl=new_alimon.level))
            hp_text = ""
            for each in range(0,int(round(new_alimon.currenthp/new_alimon.stats["health"],1)*10)):
                hp_text += "="
            print("                                    *HP:{hp_text}".format(hp_text=hp_text))
            print("                                    *{currenthp}/{max_hp}              ".format(currenthp=round(new_alimon.currenthp), max_hp=new_alimon.stats["health"]))
            print("                                    ******************************")
            print("\n\n")
            hp_text = ""
            for each in range(0,int(round(curTrainerAlimon.currenthp/curTrainerAlimon.stats["health"],1)*10)):
                hp_text += "="
            print("********{your_alimon} lvl{lvl}*********".format(your_alimon=curTrainerAlimon.name, lvl=curTrainerAlimon.level))
            print("*HP:{hp_text}".format(hp_text=hp_text))
            print("*{currenthp}/{max_hp}".format(currenthp=round(curTrainerAlimon.currenthp), max_hp=curTrainerAlimon.stats["health"]))
            print("*********************************")
            print("Battle\nParty\nBag\nRun")
            try:
                answer = input().upper().strip()
            except:
                os.system('cls')
                print("That is not a valid option try again")
                time.sleep(2)
                os.system('cls')
            if (answer == "BATTLE"):
                os.system('cls')
                turns = self.battle(curTrainerAlimon, new_alimon)
                if(new_alimon.currenthp <= 0):
                    os.system('cls')
                    print("{alimon} fainted!".format(alimon=new_alimon.name))
                    time.sleep(2)
                    os.system('cls')
                    self.exp_calculations(alimons_that_battled, new_alimon, turns)
                elif(curTrainerAlimon.currenthp <= 0):
                    for alimon in self.main_trainer.ali_team:
                        if (alimon.currenthp != 0):
                            os.system('cls')
                            print("Your {alimon} fainted!".format(alimon=curTrainerAlimon.name))
                            time.sleep(2)
                            os.system('cls')
                            self.view_party(force_swap=True)
                            continue
                        else:
                            continue
                time.sleep(2)
                os.system('cls')
            elif (answer == "PARTY"):
                os.system('cls')
                self.view_party()
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
                    if (current_item.type == "BALL"):
                        if (self.in_encounter == False):
                            os.system('cls')
                            print("Sorry You Cannot Use That Item Right Now.")
                            time.sleep(2)
                            os.system('cls')
                        else:
                            self.main_trainer.remove_item(item, 1)
                            caught = self.catching_alimon(current_item, current_opp_alimon, trainer)
                            return caught
                    elif(current_item.type == "HEAL"):
                        pass


                elif (answer == "BACK"):
                    os.system('cls')
                    return False
                else:
                    os.system('cls')
                    print("Sorry that is not a valid choice.")
                    time.sleep(2)
                    os.system('cls')

    # -----------------------------------------------------------------------------------------------------------------------------
    #                                          SWITCH ALIMON FUNCTION
    #   @param Self, position one, position two
    #   @return nothing, runs until it ends
    #   -Swaps Alimon at position 1 with alimon at position 2
    # -----------------------------------------------------------------------------------------------------------------------------
    def swap_alimon_position(self, position_one, position_two):
        os.system('cls')
        temp_var = self.main_trainer.ali_team[position_one]
        self.main_trainer.ali_team[position_one] = self.main_trainer.ali_team[position_two]
        self.main_trainer.ali_team[position_two] = temp_var
        print("Switch Successful")
        time.sleep(1)
        os.system('cls')
        return

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




    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                          BATTLE FUNCTION
    #   @param Self, trainer's Alimon, and opposing Alimon
    #   @return number of turns that passed during the battle
    #   -Prints out all available attacks Trainer ALimon can use and promps user to select one
    #   -If trainer selects an attack, increment Turns by 1, randomly choose an attack for opposing Alimon to use.
    #   -Then calculate how much damage both attacks will do
    #   -Then Compare Speed stats to see which Alimon will Attack first
    #   -Then commence turn based combat while checking if either Alimon has fainted during the battle.
    #       -In Turn Based combat, damage calculation is done (depeneding on type of attack) using stats from both Alimons (Attack, Defense, Sp.Atk, Sp.Def)
    #   TODO: Fix damage calculations, Apply stat change effects
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def battle(self, trainer_alimon, opp_alimon):
        turns = 0
        num_of_menu_choices = 4
        choice_num = 1
        select_num = 1
        end_battle = False
        while (not end_battle):
            # MENU CHOICES PRINTING LOGIC
            for choice in trainer_alimon.attack_list:
                if (select_num == choice_num):
                    print(">{choice_num}.".format(choice_num=choice_num) + choice)
                    choice_num += 1
                    current_choice = choice
                else:
                    print("{choice_num}.".format(choice_num=choice_num) + choice)
                    choice_num += 1
            choice_num = 1
            print("What will you do now? (DOWN, UP, ENTER, BACK)")
            # Try to turn input uppercase
            try:
                answer = input().upper().strip()
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

                #Increment Turns
                turns +=1

                #Calculate how much damage the attack from the opposing alimon is gonna do
                opp_alimon_attack = random.choice(opp_alimon.attack_list)
                while(opp_alimon_attack == "--"):
                    opp_alimon_attack = random.choice(opp_alimon.attack_list)
                opp_attack_type = self.attack_list[opp_alimon_attack].type
                if(opp_attack_type == "physical"):
                    damage_from_opp_attack = self.attack_list[opp_alimon_attack].damage + (opp_alimon.stats["attack"]/10)
                else:
                    damage_from_opp_attack = self.attack_list[opp_alimon_attack].damage + (opp_alimon.stats["sp.atk"]/10)



                #Calculate how much damage the attack from the trainer is going to do
                trainer_alimon_attack = current_choice
                trainer_attack_type = self.attack_list[trainer_alimon_attack].type
                if(trainer_attack_type == "physical"):
                    damage_from_trainer_attack = self.attack_list[trainer_alimon_attack].damage + (trainer_alimon.stats["attack"]/10)
                else:
                    damage_from_trainer_attack = self.attack_list[trainer_alimon_attack].damage + (trainer_alimon.stats["sp.atk"]/10)


                #Decide who is going to attack first
                first_attacker = (trainer_alimon.stats["speed"] > opp_alimon.stats["speed"])


                #If Trainer's Alimon is faster, it attacks first
                if(first_attacker == True):
                    os.system("cls")
                    print("{trainermon} used {atk_name}!".format(trainermon= trainer_alimon.name, atk_name=current_choice))
                    time.sleep(2)
                    os.system('cls')
                    #Alimon's accuracy/10 + attack's base accuracy * 100 to get whole number rounded.
                    attack_accuracy = round((self.attack_list[trainer_alimon_attack].accuracy+(trainer_alimon.stats["accuracy"]/10))*100)

                    if(attack_accuracy < 100):
                        weighted_list = [attack_accuracy, 100-attack_accuracy]
                        boolean_list = [True, False]
                        hit_or_miss = random.choices(boolean_list, weights= weighted_list, k=1)
                    else:
                        hit_or_miss = True

                    #If random choice chose True (attack lands) calculate damage
                    if(hit_or_miss):
                        if(trainer_attack_type == "physical"):
                            opp_alimon_damage = damage_from_trainer_attack - (opp_alimon.stats["defense"]/5)
                        else:
                            opp_alimon_damage = damage_from_trainer_attack - (opp_alimon.stats["sp.def"] / 5)

                        if(opp_alimon_damage < 0):
                            opp_alimon_damage = 0
                        print("{opp_alimon} took {damage} from the attack!".format(opp_alimon=opp_alimon.name, damage=round(opp_alimon_damage)))
                        opp_alimon.currenthp -= opp_alimon_damage
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print("But it Missed!")
                        time.sleep(2)
                #If False, opposing Alimon attacks first
                else:
                    os.system("cls")
                    print("{opp_mon} used {atk_name}!".format(opp_mon=opp_alimon.name, atk_name=current_choice))
                    time.sleep(2)
                    os.system('cls')
                    # Alimon's accuracy/10 + attack's base accuracy * 100 to get whole number rounded.
                    attack_accuracy = round((self.attack_list[opp_alimon_attack].accuracy + (
                                opp_alimon.stats["accuracy"] / 10)) * 100)
                    if (attack_accuracy < 100):
                        weighted_list = [attack_accuracy, 100 - attack_accuracy]
                        boolean_list = [True, False]
                        hit_or_miss = random.choices(boolean_list, weights=weighted_list, k=1)
                    else:
                        hit_or_miss = True

                    # If random choice chose True (attack lands) calculate damage
                    if (hit_or_miss):
                        if (opp_attack_type == "physical"):
                            trainer_alimon_damage = damage_from_opp_attack - (trainer_alimon.stats["defense"] / 5)
                        else:
                            trainer_alimon_damage = damage_from_opp_attack - (trainer_alimon.stats["sp.def"] / 5)

                        if (trainer_alimon_damage < 0):
                            trainer_alimon_damage = 0
                        print("{trainer_alimon} took {damage} from the attack!".format(trainer_alimon=trainer_alimon.name,damage=round(trainer_alimon_damage)))
                        trainer_alimon.currenthp -= trainer_alimon_damage
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print("But it Missed!")
                        time.sleep(2)

                print(trainer_alimon.currenthp)
                print(opp_alimon.currenthp)
                time.sleep(3)
                if (trainer_alimon.currenthp <= 0 or opp_alimon.currenthp <= 0):
                    return turns

                #Same logic as above but reversed depending who attacked first
                if (first_attacker == True):
                    os.system("cls")
                    print("{opp_mon} used {atk_name}!".format(opp_mon=opp_alimon.name, atk_name=current_choice))
                    time.sleep(2)
                    os.system('cls')
                    # Alimon's accuracy/10 + attack's base accuracy * 100 to get whole number rounded.
                    attack_accuracy = round((self.attack_list[opp_alimon_attack].accuracy + (
                            opp_alimon.stats["accuracy"] / 10)) * 100)
                    if (attack_accuracy < 100):
                        weighted_list = [attack_accuracy, 100 - attack_accuracy]
                        boolean_list = [True, False]
                        hit_or_miss = random.choices(boolean_list, weights=weighted_list, k=1)
                    else:
                        hit_or_miss = True

                    # If random choice chose True (attack lands) calculate damage
                    if (hit_or_miss):
                        if (opp_attack_type == "physical"):
                            trainer_alimon_damage = damage_from_opp_attack - (trainer_alimon.stats["defense"] / 5)
                        else:
                            trainer_alimon_damage = damage_from_opp_attack - (trainer_alimon.stats["sp.def"] / 5)

                        if (trainer_alimon_damage < 0):
                            trainer_alimon_damage = 0
                        print("{trainer_alimon} took {damage} from the attack!".format(trainer_alimon=trainer_alimon.name, damage=round(trainer_alimon_damage)))
                        trainer_alimon.currenthp -= trainer_alimon_damage
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print("But it Missed!")
                        time.sleep(2)
                else:
                    os.system("cls")
                    print(
                        "{trainermon} used {atk_name}!".format(trainermon=trainer_alimon.name, atk_name=current_choice))
                    time.sleep(2)
                    os.system('cls')
                    # Alimon's accuracy/10 + attack's base accuracy * 100 to get whole number rounded.
                    attack_accuracy = round((self.attack_list[trainer_alimon_attack].accuracy + (
                            trainer_alimon.stats["accuracy"] / 10)) * 100)
                    if (attack_accuracy < 100):
                        weighted_list = [attack_accuracy, 100 - attack_accuracy]
                        boolean_list = [True, False]
                        hit_or_miss = random.choices(boolean_list, weights=weighted_list, k=1)
                    else:
                        hit_or_miss = True

                    # If random choice chose True (attack lands) calculate damage
                    if (hit_or_miss):
                        if (trainer_attack_type == "physical"):
                            opp_alimon_damage = damage_from_trainer_attack - (opp_alimon.stats["defense"] / 5)
                        else:
                            opp_alimon_damage = damage_from_trainer_attack - (opp_alimon.stats["sp.def"] / 5)

                        if (opp_alimon_damage < 0):
                            opp_alimon_damage = 0
                        print("{opp_alimon} took {damage} from the attack!".format(opp_alimon=opp_alimon.name, damage=round(opp_alimon_damage)))
                        opp_alimon.currenthp -= opp_alimon_damage
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print("But it Missed!")
                        time.sleep(2)

                print(trainer_alimon.currenthp)
                print(opp_alimon.currenthp)
                time.sleep(3)
                if (trainer_alimon.currenthp <= 0 or opp_alimon.currenthp <= 0):
                    return turns

                end_battle = True
            elif (answer == "BACK"):
                end_battle = True
                # IF answer is invalid, print a message and have them choose again
            else:
                os.system('cls')
                print("Sorry that is not a valid choice")
                time.sleep(2)
                os.system('cls')

        return turns


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



    #TODO: Finish EXP calculation function
    def exp_calculations(self, list_of_alimons_battled, opp_alimon, turns):
        pass


    # -------------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                          GENERATE RANDOM ALIMON FUNCTION
    #   @param self
    #   @return Random Alimon object
    #   -Using a weighted list and the Random.choices function, we pick an Alimon from the Alidex.
    #       -The weights are correspondant to the encounter rates of each Alimon.
    #       -This function is going to be primarily used for the Encounter Function
    #   -Once Alimon has been picked, we randomize all of it's stats by randomizing it's level, then using it's base stats and growth stats to formulate it's stats
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------
    def generate_random_alimon(self):
        weighted_list = []
        for alimon in self.ali_list:
            weighted_list.append(self.ali_list[alimon].encounter_rate)
        encountered_alimon = self.ali_list[self.random_choice(self.ali_list, weighted_list, 1)[0]]
        is_shiny = self.random_choice([True, False], [encountered_alimon.shiny_rate, 1 - encountered_alimon.shiny_rate], 1)
        level = self.random_choice(range(1, 51), None, 1)
        stats = {"health":0,"attack":0,"defense":0,"sp.atk":0,"speed":0,"accuracy":0}
        stats["health"] = (int(encountered_alimon.stats["health"]) + round(int(encountered_alimon.stats["health"]) * float(encountered_alimon.growth_rate[0]) * (int(level[0])/10)))
        stats["attack"] = (int(encountered_alimon.stats["attack"]) + round(int(encountered_alimon.stats["attack"]) * float(encountered_alimon.growth_rate[1]) * int(level[0])/10))
        stats["defense"] = (int(encountered_alimon.stats["defense"]) + round(int(encountered_alimon.stats["defense"]) * float(encountered_alimon.growth_rate[2]) * int(level[0])/10))
        stats["sp.atk"] = (int(encountered_alimon.stats["sp.atk"]) + round(int(encountered_alimon.stats["sp.atk"]) * float(encountered_alimon.growth_rate[3]) * int(level[0])/10))
        stats["sp.def"] = (int(encountered_alimon.stats["sp.def"]) + round(int(encountered_alimon.stats["sp.def"]) * float(encountered_alimon.growth_rate[4]) * int(level[0])/10))
        stats["speed"] = (int(encountered_alimon.stats["sp.def"]) + round(int(encountered_alimon.stats["sp.def"]) * float(encountered_alimon.growth_rate[5]) * int(level[0])/10))
        stats["accuracy"] = (int(encountered_alimon.stats["sp.def"]) + round(int(encountered_alimon.stats["sp.def"]) * float(encountered_alimon.growth_rate[6]) * int(level[0])/10))
        attack_list = ["headbutt","hate raid","--","--"]
        currenthp = stats["health"]
        new_alimon = Alimon(encountered_alimon.name, self.ali_list[encountered_alimon.name].capture_rate,self.ali_list[encountered_alimon.name].encounter_rate,stats=stats,level= level[0], growth_rate=encountered_alimon.growth_rate, attack_list=attack_list, is_shiny=is_shiny[0], currenthp=currenthp)
        return new_alimon
