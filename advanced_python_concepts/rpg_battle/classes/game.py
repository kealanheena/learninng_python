import random
from .magic import Spell

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Person:
	def __init__(self, name, hp, mp, atk, df, magic, items):
		self.name = name
		self.max_hp = hp
		self.hp = hp
		self.max_mp = mp
		self.mp = mp
		self.atkl = atk - 10
		self.atkh = atk + 10
		self.df = df
		self.magic = magic
		self.items = items
		self.actions = ["Attack", "Magic", "Items"]

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def heal(self, dmg):
		self.hp += dmg
		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def get_hp(self):
		return self.hp

	def get_max_hp(self):
		return self.max_hp

	def get_mp(self):
		return self.mp

	def get_max_mp(self):
		return self.max_mp

	def reduce_mp(self, cost):
		self.mp -= cost

	def choose_action(self):
		i = 1
		print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
		print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
		for item in self.actions:
			print("      " + str(i) + ".", item)
			i += 1

	def choose_magic(self):
		i = 1

		print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
		for spell in self.magic:
			print("      " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + "mp)")
			i += 1

	def choose_items(self):
		i = 1

		print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
		for item in self.items:
			print("      " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
			i += 1

	def choose_target(self, enemies):
		i = 1
		print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
		for enemy in enemies:
			if enemy.get_hp() is not 0:
				print("        " + str(i) + ".", enemy.name)
				i += 1
		choice = int(input("    Choose target:")) - 1
		return choice


	def get_enemy_stats(self):
		hp_bar = ""
		hp_bar_ticks = (self.hp / self.max_hp) * 100 / 2

		while hp_bar_ticks > 0:
			hp_bar += "█"
			hp_bar_ticks -= 1
		while len(hp_bar) < 50:
			hp_bar += " "
				
		display_hp = str(self.hp) + "/" + str(self.max_hp)
		while len(display_hp) < 11:
			display_hp = " " + display_hp

		print("                   __________________________________________________")
		print(bcolors.BOLD + self.name + " " + 
			display_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD + "|   " + bcolors.ENDC)

	def get_stats(self):
		hp_bar = ""
		hp_bar_ticks = (self.hp / self.max_hp) * 100 / 4

		mp_bar = ""
		mp_bar_ticks = (self.mp / self.max_mp) * 100 / 10

		while hp_bar_ticks > 0:
			hp_bar += "█"
			hp_bar_ticks -= 1
		while len(hp_bar) < 25:
			hp_bar += " "

		while mp_bar_ticks > 0:
			mp_bar += "█"
			mp_bar_ticks -= 1
		while len(mp_bar) < 10:
			mp_bar += " "

		display_hp = str(self.hp) + "/" + str(self.max_hp)
		while len(display_hp) < 9:
			display_hp = " " + display_hp 

		display_mp = str(self.mp) + "/" + str(self.max_mp)
		while len(display_mp) < 8:
			display_mp = " " + display_mp


		print("                    _________________________              __________")
		print(bcolors.BOLD + self.name + "   " + 
			display_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|   " + 
			display_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC +"|" + bcolors.ENDC)

	def choose_enemy_spell(self):
		magic_choice = random.randrange(0, len(self.magic))
		spell = self.magic[magic_choice]
		magic_dmg = spell.generate_damage()

		pct = (self.hp / self.mhp) * 100

		if self.mp < spell.cost or spell.type is "white" and pct > 50:
			self.choose_enemy_spell()
		else:
			return spell, magic_dmg
