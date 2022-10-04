class Trainer:
    # Trainer Contructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.bag = {}
        self.poke_team = []

    # Description of Trainer
    def __repr__(self):
        pronoun = ""
        num_of_pokemon = len(self.poke_team)
        if (self.gender == "BOY"):
            pronoun = "he"
        else:
            pronoun = "she"
        description = "This is {name}, {pronoun} has {num_pokemon}!".format(name=self.name, pronoun=pronoun,
                                                                            num_pokemon=num_of_pokemon)
        return description

    def add_to_bag(self):
        def encounter_pokemon(self):
            pass