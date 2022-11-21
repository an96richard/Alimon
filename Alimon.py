import math
class Alimon:
    shiny_rate = 0.00001
    def __init__(self, name, capture_rate, encounter_rate, base_xp_rate, xp_growth_rate, stats={"health":0,"attack":0,"defense":0,"sp.atk":0,"sp.def":0,"speed":0,"accuracy":0}, attack_list=["","","",""], stat_growth_rate = [0.0,0.0,0.0,0.0,0.0,0.0,0.0], level=1, exp =0, is_shiny = False, currenthp = 0):
        self.name = name
        self.level = level
        self.exp = exp
        self.is_shiny = is_shiny
        self.capture_rate = round(capture_rate,3)
        self.encounter_rate = round(encounter_rate, 3)
        self.stat_growth_rate = stat_growth_rate
        self.attack_list = attack_list
        self.stats = stats
        self.currenthp = currenthp
        self.base_xp_rate = base_xp_rate
        self.xp_growth_rate = xp_growth_rate

        if (self.xp_growth_rate == "FAST"):
            self.xp_needed_for_next_level = round(0.8 * (self.level + 1) ** 3)
        elif (self.xp_growth_rate == "MEDIUM_FAST"):
            self.xp_needed_for_next_level = round((self.level + 1) ** 3)
        elif (self.xp_growth_rate == "MEDIUM_SLOW"):
            self.xp_needed_for_next_level = round((1.2 * ((self.level + 1) ** 3)) - (15 * ((self.level + 1) ** 3)) + (100 * (self.level + 1)) - 140)
        elif (self.xp_growth_rate == "SLOW"):
            self.xp_needed_for_next_level =  round(1.25 * (self.level + 1) ** 3)


    def __repr__(self):
        description = "This is {name}, it is level {level} and is {exp} EXP from leveling up.".format(name=self.name,  level=self.level, exp=round(self.xp_needed_for_next_level - self.exp), capture_rate = self.capture_rate)
        if (self.is_shiny):
            description += "\nAnd it is SHINY!"
        return description

    def update_xp_needed(self):
        if (self.xp_growth_rate == "FAST"):
            self.xp_needed_for_next_level = round(0.8 * (self.level + 1) ** 3)
        elif (self.xp_growth_rate == "MEDIUM_FAST"):
            self.xp_needed_for_next_level = round((self.level + 1) ** 3)
        elif (self.xp_growth_rate == "MEDIUM_SLOW"):
            self.xp_needed_for_next_level = round(
                (1.2 * ((self.level + 1) ** 3)) - (15 * ((self.level + 1) ** 3)) + (100 * (self.level + 1)) - 140)
        elif (self.xp_growth_rate == "SLOW"):
            self.xp_needed_for_next_level = round(1.25 * (self.level + 1) ** 3)
