import random # For def randominteger
import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class Player:
    health = 20
    damage = randominteger(2, 5)
    attackspeed = 1.5

    def attack(damage):
        Enemy.receivedamage(damage)

class Enemy:
    health = 10
    damage = randominteger(1, 3)
    attackspeed = 1

    def death():
        print("Enemy dead")

    def receivedamage(damage):
        Enemy.health -= damage
        
        if (Enemy.health <= 0):
            Enemy.death()

# Spawn random objects (enemies)

timestart = time.time()
#print(Player.health)
#print(Player.damage)
#print(Player.attackspeed)

#print(Enemy.health)
#print(Enemy.damage)
#print(Enemy.attackspeed)

while (Enemy.health > 0):
    Player.attack(Player.damage)
    print(Enemy.health)

print(time.time() - timestart)