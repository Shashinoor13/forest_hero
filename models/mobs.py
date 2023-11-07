import random


class Mobs:
    def __init__(self, name: str, hp: int, xp: int, danger: int, rewards: list[str]):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.danger = danger
        self.rewards = rewards

    def drop_items(self):
        return self.rewards[random.randint(0, len(self.rewards) - 1)]

    def take_damage(self, hit):
        self.hp -= hit
        if self.hp <= 0:
            print("Mob is dead")
            return True
        else:
            print("Mob is alive with hp ", self.hp)
            return False

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True


"""
danger ranges from 0,2
drops contains list of items that it can drop on being killed

Implement :
rewards according to the difficulty
"""
