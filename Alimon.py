import math
class Alimon:
    shiny_rate = 0.00001
    def __init__(self, name, capture_rate, encounter_rate, stats={"health":0,"attack":0,"defense":0,"sp.atk":0,"speed":0,"accuracy":0}, attack_list=["","","",""], growth_rate = [0.0,0.0,0.0,0.0,0.0,0.0,0.0], level=1, exp =0, is_shiny = False, currenthp = 0):
        self.name = name
        self.level = level
        self.exp = exp
        self.is_shiny = is_shiny
        self.capture_rate = round(capture_rate,3)
        self.encounter_rate = round(encounter_rate, 3)
        self.growth_rate = growth_rate
        self.attack_list = attack_list
        self.stats = stats
        self.currenthp = currenthp

    def __repr__(self):
        description = "This is {name}, it is level {level} and is {exp} EXP from leveling up.".format(name=self.name,  level=self.level, exp=self.exp, capture_rate = self.capture_rate)
        if (self.is_shiny):
            description += "\nAnd it is SHINY!"
        return description

    def gain_exp(self, exp):
        self.exp += exp
        if (self.exp >= 100):
            self.level += 1
            self.exp = self.exp - 100

