from classes.game import Person, bcolors

magic = [{"name": "Fire", "mp": 10, "dmg": 60},
        {"name": "Ice", "mp": 12, "dmg": 80},
        {"name": "Spark", "mp": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 15, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1
    
    if index is 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg, "points of damage. Player HP:", player.get_hp())
    # break