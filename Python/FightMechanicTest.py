import random # For def randominteger

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class Player:
    health = 20
    damage = randominteger(2, 5)

class Enemy:
    health = 10
    damage = randominteger(1, 3)

# Spawn random objects (enemies)

print(Player.health)
print(Player.damage)
print(Enemy.health)
print(Enemy.damage)