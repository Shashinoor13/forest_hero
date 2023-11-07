class MobData:
    def __init__(self):
        self.mobs = {
            1: {
                "name": "Spider",
                "health": 100,
                "damage": 20,
                "rarity": 1,
                "drops": ["eye of spider", "webs"],
            },
            2: {
                "name": "Skeleton",
                "health": 150,
                "damage": 30,
                "rarity": 2,
                "drops": ["bones", "skull"],
            },
            3: {
                "name": "Zombie",
                "health": 200,
                "damage": 40,
                "rarity": 3,
                "drops": ["rotten flesh", "brain"],
            },
            4: {
                "name": "Ghost",
                "health": 250,
                "damage": 50,
                "rarity": 4,
                "drops": ["ectoplasm", "soul"],
            },
            5: {
                "name": "Vampire",
                "health": 300,
                "damage": 60,
                "rarity": 5,
                "drops": ["blood", "heart"],
            },
            6: {
                "name": "Werewolf",
                "health": 350,
                "damage": 70,
                "rarity": 6,
                "drops": ["fang", "claw"],
            },
            7: {
                "name": "Demon",
                "health": 400,
                "damage": 80,
                "rarity": 7,
                "drops": ["fire", "brimstone"],
            },
            8: {
                "name": "Dragon",
                "health": 450,
                "damage": 90,
                "rarity": 8,
                "drops": ["scale", "tooth"],
            },
            9: {
                "name": "Giant",
                "health": 500,
                "damage": 100,
                "rarity": 9,
                "drops": ["big toe", "thumb"],
            },
            10: {
                "name": "God",
                "health": 1000,
                "damage": 200,
                "rarity": 10,
                "drops": ["blessing", "holy grail"],
            },
        }

    def return_mob(self, item_id):
        if isinstance(item_id, int) and 0 <= item_id < len(self.items):
            return self.items[item_id]
        else:
            return None
