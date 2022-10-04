class Alimon:
    def __init__(self, name, capture_rate, level=1):
        self.name = name
        self.level = level
        self.exp = 0
        self.is_shiny = False

    def __repr__(self):
        description = "This is {name}, it is level {level} and is {exp} from leveling up.".format(name=self.name,
                                                                                                  level=self.level,
                                                                                                  exp=self.exp)
        if (self.is_shiny):
            description += " And it is SHINY!"
        return description

    def gain_exp(self, exp):
        self.exp += exp
        if (self.exp >= 100):
            self.level += 1
            self.exp = self.exp - 100