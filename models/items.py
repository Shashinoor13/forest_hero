class Items:
    def __init__(
        self,
        name,
        space,
        value,
        is_consumable=False,
        is_weapon=False,
        is_armor=False,
        is_key=False,
        health=0,
        armor=0,
        key_id=0,
    ):
        self.space = space
        self.name = name
        self.value = value
        self.is_consumable = is_consumable
        self.is_weapon = is_weapon
        self.is_armor = is_armor
        self.is_key = is_key
        self.health = health
        self.armor = armor
        self.key_id = key_id
