from Item import Item
from AliBall import AliBall
class Trainer:
    # Trainer Contructor
    #TODO: change poke team to aliTeam
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.bag = {"ALIBALL" : AliBall(), "POOOPIE": Item("POOPIE", "POOP", "CHICKEN", 10, 2)}
        self.poke_team = []
        self.pc = []

    # Description of Trainer
    def __repr__(self):
        pronoun = ""
        num_of_pokemon = len(self.poke_team)
        if (self.gender == "BOY"):
            pronoun = "he"
        else:
            pronoun = "she"
        description = "This is {name}, {pronoun} has {num_pokemon} Alimon(s)!".format(name=self.name, pronoun=pronoun,
                                                                            num_pokemon=num_of_pokemon)
        return description

    # ---------------------------------------------------------------------------------------------------------------
    #                                          ADD TO BAG FUNCTION
    #   -Takes in Self, an Item, and NUMBER OF ITEM to be added
    #   -Checks if item is an Item object
    #       -If Yes, Checks if the item already exist in the bag
    #           -If Yes, adds number_of_item to the value of item that is already in the bag
    #           -If No, adds number_of_item to the item object and puts it in the Bag
    #       -If No, Prints error message and sends them back to the last menu
    # ---------------------------------------------------------------------------------------------------------------
    def add_to_bag(self, item, number_of_item):
        if(isinstance(item, Item)):
            if(item.name in self.bag):
                self.bag[item.name].count += number_of_item
            else:
                item.count += number_of_item
                self.bag[item.name] = item
        else:
            print("Sorry That Is Not A Valid Item")