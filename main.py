from hero import Hero
from mobs import Mobs
import os

main_character = Hero("Shashinoor")
m = Mobs("Spider", 200, 500, 1, ["eye of spider", "webs"])

while m.is_alive():
    print("Mob is alive")
    choice = input("Attack or run \nCHOICE : ")
    if choice == "attack":
        m.take_damage(100)
    else:
        print("You ran away")
        print("The mob has ", m.hp, " health left")
        break

if not m.is_alive():
    os.system("clear")
    print("You killed the mob")
    gained_items = m.drop_items()
    print("You got ", gained_items)
    print("You gained ", m.xp, " xp")
    main_character.gain_xp(m.xp)

print(main_character.show_all())
