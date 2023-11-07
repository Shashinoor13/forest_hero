from hero import Hero
from mobs import Mobs
from utils import Helpers

main_character = Hero("Shashinoor", ["sword", "axe"])
m = Mobs("Spider", 200, 500, 1, ["eye of spider", "webs"])


print("You are in a forest")
print("You see a mob")
print("The mob has ", m.hp, " health")
print("You have ", main_character.health, " health")
print("You have ", main_character.level, " level")
print("You have ", main_character.xp, " xp")
print("You have ", main_character.weapons, " weapons")


def attack_mob(mob):
    while mob.is_alive():
        Helpers.clearScreen()
        print("Mob is alive with ", mob.hp, " health")
        choice = input("Attack or run \nCHOICE : ")
        if choice.lower() == "attack":
            mob.take_damage(100)
        elif choice.lower() == "run":
            print("You ran away")
            print("The mob has ", mob.hp, " health left")
            break
        else:
            print("Wrong choice")
            continue
        if not m.is_alive():
            Helpers.clearScreen()
            print("You killed the mob")
            gained_items = m.drop_items()
            print("You got ", gained_items)
            print("You gained ", m.xp, " xp")
            main_character.gain_xp(m.xp)


choice = input("Do you want to fight the mob ?")
if choice.lower() == "yes":
    attack_mob(m)
elif choice.lower() == "no":
    print("You ran away")


print(main_character.show_all())
