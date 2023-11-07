class WeaponData:
    def __init__(self):
        # Create 10 weapons
        self.weapons = {
            1: {
                "name": "Sword",
                "category": "Sword",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            2: {
                "name": "Axe",
                "category": "Axe",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            3: {
                "name": "Mace",
                "category": "Mace",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            4: {
                "name": "Shield",
                "category": "Shield",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            5: {
                "name": "Bow",
                "category": "Bow",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            6: {
                "name": "Dagger",
                "category": "Dagger",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            7: {
                "name": "Staff",
                "category": "Staff",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            8: {
                "name": "Spear",
                "category": "Spear",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            9: {
                "name": "Hammer",
                "category": "Hammer",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
            10: {
                "name": "Mace",
                "category": "Mace",
                "damage": 100,
                "rarity": 1,
                "enchantments": [],
            },
        }

    def getWeapon(self, id):
        return self.weapons[id]
