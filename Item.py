class Item:
    def __init__(self, name, type, desc,cost=0, count=0):
        self.name  = name
        self.type = type
        self.cost = cost
        self.count = count
        self.desc = desc