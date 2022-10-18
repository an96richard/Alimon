import math
class Alimon:
    shiny_rate = 0.00001
    def __init__(self, name, capture_rate, encounter_rate, level=1, exp =0, is_shiny = False):
        self.name = name
        self.level = level
        self.exp = exp
        self.is_shiny = is_shiny
        self.capture_rate = round(capture_rate,3)
        self.encounter_rate = round(encounter_rate, 3)


    def __repr__(self):
        description = "This is {name}, it is level {level} and is {exp} EXP from leveling up. It has a {capture_rate} capture rate.".format(name=self.name,  level=self.level, exp=self.exp, capture_rate = self.capture_rate)
        if (self.is_shiny):
            description += " And it is SHINY!"
        return description

    def gain_exp(self, exp):
        self.exp += exp
        if (self.exp >= 100):
            self.level += 1
            self.exp = self.exp - 100

