class Attack:
    def __init__(self, name, type, damage, stat_change, description, accuracy= 0.0):
        self.name = name
        self.type = type
        self.damage = damage
        self.stat_change = stat_change
        self.accuracy = accuracy
        self.description = description