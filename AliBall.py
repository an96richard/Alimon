from Item import Item
class AliBall(Item):
    def __init__(self):
        super().__init__("ALIBALL", "BALL", "This is an ordinary AliBall used to catch Alimons.", 10, 0)
        self.capture_rate_multiplier = 1