class Weapons:
    def __init__(
        self,
        name: str,
        category: str,
        damage: int,
        rarity: int,
        enchantments: list[str],
    ):
        self.name = name
        self.category = category
        self.damage = damage
        self.rarity = rarity
        self.enchantments = enchantments


"""
To implement Enchainment and add to the damage and rarity of the weapon
"""
