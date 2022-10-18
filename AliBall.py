from Item import Item
class AliBall(Item):
    def __init__(self,name,type,desc,cost):
        super().__init__(name, type, desc, cost)
        self.capture_rate_multiplier = 1