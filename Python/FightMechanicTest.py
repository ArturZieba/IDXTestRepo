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

    def receivedamage(damage):
        Player.health -= damage
        
        if (Player.health <= 0):
            Player.death()

    def death():
        print("Player dead")

class Enemy:
    health = 10
    damage = randominteger(1, 3)
    attackspeed = 1

    def attack(damage):
        Player.receivedamage(damage)

    def receivedamage(damage):
        Enemy.health -= damage
        
        if (Enemy.health <= 0):
            Enemy.death()

    def death():
        print("Enemy dead")

# Spawn random objects (enemies)

timestart = time.time()
#print(Player.health)
#print(Player.damage)
#print(Player.attackspeed)

#print(Enemy.health)
#print(Enemy.damage)
#print(Enemy.attackspeed)

starttime = time.monotonic()

# Game loop
while (True):
    print("Ping")

    time.sleep(1.0 - ((time.monotonic() - starttime) % 1.0))
    #if(time.time() - timestart == Player.attackspeed):
    #    Player.attack(Player.damage)
    #elif(time.time() - timestart == Enemy.attackspeed):
    #    Enemy.attack(Enemy.damage)

#print(time.time() - timestart)