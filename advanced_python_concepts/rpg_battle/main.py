from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores the party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5},
                {"item": grenade, "quantity": 5}]

# Instatiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Gimar:", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Mercer", 11200, 701, 525, 15, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("======================")

    print("\n\n")
    print("NAME                HP                                    MP        ")
    for player in players:
        player.get_stats()
        print("\n")

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index is 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
        elif index is 1:
            player.choose_magic()
            magic_choice = int(input("Choose spell: ")) -1

            if magic_choice is -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = player.magic[magic_choice].generate_damage()


            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of magic damage." + bcolors.ENDC)

        elif index is 2:
            player.choose_items()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice is -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] is 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type is "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop), "HP" + bcolors.ENDC)
            elif item.type is "elixer":
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type is "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " Deals " + str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg)

    print("-----------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() is 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() is 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
