import random
from data.items import ItemData
from functions.data_adapter import DataAdapter
from models.items import Items

from models.mobs import Mobs


class Forest:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.layers = random.randint(3, 5)
        self.mobs = []
        self.trees = []
        self.items = []
        self.item_data = ItemData()
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
        self.mobs.append(
            DataAdapter().MobDataAdapt(self.item_data.mobs[random.randint(1, 5)])
        )

    def generate_item(self):
        self.items.append(
            DataAdapter().ItemDataAdapt(self.item_data.items[random.randint(1, 5)])
        )


"""
spawns trees,mobs,inside the forest according to the difficulty
"""
