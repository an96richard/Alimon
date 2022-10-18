from Item import Item
from AliBall import AliBall
class Trainer:
    # Trainer Contructor
    #TODO: change poke team to aliTeam
    def __init__(self, name, gender, bag = {}, bag_count = [], ali_team = [], pc = []):
        self.name = name
        self.gender = gender
        self.bag = bag
        self.bag_count = bag_count
        self.ali_team = ali_team
        self.pc = pc

    # Description of Trainer
    def __repr__(self):
        pronoun = ""
        num_of_alimon = len(self.ali_team)
        if (self.gender == "BOY"):
            pronoun = "he"
        else:
            pronoun = "she"
        description = "This is {name}, {pronoun} has {num_pokemon} Alimon(s)!".format(name=self.name, pronoun=pronoun,
                                                                            num_pokemon=num_of_alimon)
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
                index = list(self.bag.keys()).index(item.name)
                self.bag_count[index] += number_of_item
            else:
                self.bag[item.name] = item
                self.bag = dict(sorted(self.bag.items()))
                index = list(self.bag.keys()).index(item.name)
                self.bag_count.insert(index,number_of_item)
        else:
            print("Sorry That Is Not A Valid Item")

    def get_item_count(self, item):
        index = list(self.bag.keys()).index(item.name)
        if(index != -1):
            return self.bag_count[index]
        else:
            return "Sorry You Do Not Have That Item"

    def remove_item(self, item, num_of_item):
        index = list(self.bag.keys()).index(item.name)
        if (index != -1):
            self.bag_count[index] -= num_of_item
            if(self.bag_count[index] <=0):
                self.bag.pop(item.name)
                self.bag_count.pop(index)
        else:
            return "Sorry You Do Not Have That Item"