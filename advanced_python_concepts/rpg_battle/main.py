from classes.game import Person, bcolors

magic = [{"name": "Fire", "mp": 10, "dmg": 60},
        {"name": "Ice", "mp": 10, "dmg": 80},
        {"name": "Spark", "mp": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))