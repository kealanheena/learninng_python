import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
        
    print("enemy deals", dmg, "points of damage. current hp is", playerhp)

    if playerhp > 30:
        continue

    print("you have low health. You should see a doctors")
    break

