import random

class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("HP is", self.hp)

slime = Enemy(40, 49)
slime.getAtk()

dragon = Enemy(75, 90)
dragon.getAtk()

# playerhp = 260

# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg

#     if playerhp <= 30:
#         playerhp = 30
        
#     print("enemy deals", dmg, "points of damage. current hp is", playerhp)

#     if playerhp > 30:
#         continue

#     print("you have low health. You should see a doctors")
#     break

