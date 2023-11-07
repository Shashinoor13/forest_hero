from anyio import sleep
from models.forest import Forest
from models.hero import Hero
from models.mobs import Mobs
from utils.utils import Helpers

main_character = Hero("Shashinoor", ["sword", "axe"])
m = Mobs("Spider", 200, 500, 1, ["eye of spider", "webs"])

Helpers.clearScreen()

Helpers.printer("Welcome To The Jungle", False, "Green")
print("You see a mob")
print("The mob has ", m.hp, " health")
print("You have ", main_character.health, " health")
print("You have ", main_character.level, " level")
print("You have ", main_character.xp, " xp")
print("You have ", main_character.weapons, " weapons")


class GameGenerate:
    def __init__(self):
        self.is_complete = False

        def set_game_complete():
            self.is_complete = True

        main_character = Hero("Shashinoor", ["sword", "axe"])

        m = Mobs("Spider", 200, 500, 1, ["eye of spider", "webs"])

        Helpers.clearScreen()

        Helpers.printer("Press CTRL+C to exit \n", False, "Green")
        Helpers.printer("Welcome To The Jungle\n", False, "Green")

        forest = Forest(1)
        print("You see a mob")
        print("The mob has ", m.hp, " health")
        print("You have ", main_character.health, " health")
        print("You have ", main_character.level, " level")
        print("You have ", main_character.xp, " xp")
        print("You have ", main_character.weapons, " weapons")

        def attack_mob(mob):
            while mob.is_alive():
                print("Mob is alive with ", mob.hp, " health")
                choice = input("Attack or run \nCHOICE : ")
                if choice.lower() == "attack":
                    Helpers.clearScreen()
                    mob.take_damage(100)
                elif choice.lower() == "run":
                    Helpers.clearScreen()
                    print("You ran away")
                    print("The mob has ", mob.hp, " health left")
                    break
                else:
                    Helpers.printer("\nInvalid choice\n", True, "red")
                    continue
                if not m.is_alive():
                    Helpers.clearScreen()
                    print("You killed :", mob.name)
                    gained_items = m.drop_items()
                    print(f"You Gained :\033[32m {gained_items}\033[0m")
                    print("You gained ", m.xp, " xp")
                    main_character.gain_xp(m.xp)
                    set_game_complete()

        choice = input("Do you want to fight the mob ?")
        if choice.lower() == "yes":
            attack_mob(m)
        elif choice.lower() == "no":
            print("You ran away")


# print(main_character.show_all())
