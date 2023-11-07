from models.weapons import Weapons
from models.mobs import Mobs
from models.items import Items


class DataAdapter:
    def ItemDataAdapt(self, itemData):
        return Items(
            itemData["name"],
            itemData["space"],
            itemData["value"],
            itemData["is_consumable"],
            itemData["is_weapon"],
            itemData["is_armor"],
            itemData["is_key"],
            itemData["health"],
            itemData["armor"],
            itemData["key_id"],
        )

    def MobDataAdapt(self, mobData):
        return Mobs(
            mobData["name"],
            mobData["health"],
            mobData["xp"],
            mobData["level"],
            mobData["drops"],
        )

    def WeaponDataAdapt(self, weaponData):
        return Weapons(
            weaponData["name"],
            weaponData["category"],
            weaponData["damage"],
            weaponData["rarity"],
            weaponData["enchantments"],
        )
