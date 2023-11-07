class ItemData:
    def __init__(self):
        self.items = {
            1: {
                "name": "Sword",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": True,
                "is_armor": False,
                "is_key": False,
                "health": 0,
                "armor": 0,
                "key_id": 0,
            },
            2: {
                "name": "Shield",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": True,
                "is_key": False,
                "health": 0,
                "armor": 10,
                "key_id": 0,
            },
            3: {
                "name": "Potion",
                "space": 1,
                "value": 50,
                "is_consumable": True,
                "is_weapon": False,
                "is_armor": False,
                "is_key": False,
                "health": 50,
                "armor": 0,
                "key_id": 0,
            },
            4: {
                "name": "Key",
                "space": 1,
                "value": 50,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": False,
                "is_key": True,
                "health": 0,
                "armor": 0,
                "key_id": 1,
            },
            5: {
                "name": "Axe",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": True,
                "is_armor": False,
                "is_key": False,
                "health": 0,
                "armor": 0,
                "key_id": 0,
            },
            6: {
                "name": "Helmet",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": True,
                "is_key": False,
                "health": 0,
                "armor": 10,
                "key_id": 0,
            },
            7: {
                "name": "Dagger",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": True,
                "is_armor": False,
                "is_key": False,
                "health": 0,
                "armor": 0,
                "key_id": 0,
            },
            8: {
                "name": "Bow",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": True,
                "is_armor": False,
                "is_key": False,
                "health": 0,
                "armor": 0,
                "key_id": 0,
            },
            9: {
                "name": "Arrow",
                "space": 1,
                "value": 50,
                "is_consumable": False,
                "is_weapon": True,
                "is_armor": False,
                "is_key": False,
                "health": 0,
                "armor": 0,
                "key_id": 0,
            },
            10: {
                "name": "Boots",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": True,
                "is_key": False,
                "health": 0,
                "armor": 10,
                "key_id": 0,
            },
            11: {
                "name": "Gloves",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": True,
                "is_key": False,
                "health": 0,
                "armor": 10,
                "key_id": 0,
            },
            12: {
                "name": "Ring",
                "space": 2,
                "value": 100,
                "is_consumable": False,
                "is_weapon": False,
                "is_armor": True,
                "is_key": False,
                "health": 0,
                "armor": 10,
                "key_id": 0,
            },
        }

    def return_item(self, item_id):
        if isinstance(item_id, int) and 0 <= item_id < len(self.items):
            return self.items[item_id]
        else:
            return None


"""
1: sword
2: shield
3: potion
4: key
5: axe
6: helmet
7: dagger
8: bow
9: arrow
10: boots
11: gloves
12: ring
"""
