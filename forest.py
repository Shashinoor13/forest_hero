import random


class Forest:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.layers = random.randint(3, 5)
        self.mobs = []
        self.trees = []
        self.items = []
        self.generate_forest()

    def generate_forest(self):
        for i in range(self.layers):
            self.generate_layer()

    def generate_layer(self):
        for i in range(random.randint(5, 10)):
            self.generate_tree()
        for i in range(random.randint(5, 10)):
            self.generate_mob()
        for i in range(random.randint(5, 10)):
            self.generate_item()

    def generate_tree(self):
        pass

    def generate_mob(self):
        pass

    def generate_item(self):
        pass


"""
spawns trees,mobs,inside the forest according to the difficulty
"""
