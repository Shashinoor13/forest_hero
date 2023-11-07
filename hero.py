from weapons import Weapons

MAX_WEAPON_LIMIT = 2
MAX_HEALTH_LIMIT = 500
MAX_CHARACTER_LIMIT = 10


class Hero:
    def __init__(self, name: str = "Joe", Weapons: list[Weapons] = []):
        self.name = name
        self.weapons = Weapons
        self.health = 100
        self.level = 1
        self.xp = 0

    def add_weapon(self, weapon: Weapons):
        if len(self.weapons) < MAX_WEAPON_LIMIT:
            self.weapons.append(weapon)
        else:
            print("Cannot add more weapons")

    def remove_weapon(self, weapon: Weapons):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
        else:
            print("Weapon not found")

    def add_health(self, health: int):
        if self.health + health <= MAX_HEALTH_LIMIT:
            self.health += health
        else:
            self.health = MAX_HEALTH_LIMIT

    def loose_health(self, health: int):
        if self.health - health >= 0:
            self.health -= health
        else:
            self.health = 0

    def gain_xp(self, xp: int):
        self.xp += xp
        self.increase_level(xp)

    def increase_level(self, xp: int):
        if self.xp + xp >= 100:
            print("\n ------------------------------------ \n")
            print("Level up")
            print("\n ------------------------------------ \n")
            self.level += 1
            self.xp = 0

    def show_all(self):
        print("\n ------------------------------------ \n")
        print("Name : ", self.name)
        print("Health : ", self.health)
        print("Level : ", self.level)
        print("XP : ", self.xp)
        print("Weapons : ")
        for weapon in self.weapons:
            print(weapon.name)
        print("\n ------------------------------------ \n")


"""
To increase the xp requirements according to the level
"""
