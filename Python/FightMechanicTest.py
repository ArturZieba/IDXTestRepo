import random # For def randominteger
import threading
import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

def player_thread_function():
    while True:
        print("Player attacking")
        Player.attack(Player.damage)
        time.sleep(Player.attackspeed)
        #Check for enemy death

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

if __name__ == "__main__":
    x = threading.Thread(target=player_thread_function)
    x.start()
 
# Spawn random objects (enemies)

#timestart = time.time()
#starttime = time.monotonic()

# Game loop
#while (True):
    #print("Ping")

    #time.sleep(Player.attackspeed - ((time.monotonic() - starttime) % Player.attackspeed))
    #if(time.time() - timestart == Player.attackspeed):
    #    Player.attack(Player.damage)
    #elif(time.time() - timestart == Enemy.attackspeed):
    #    Enemy.attack(Enemy.damage)

#print(time.time() - timestart)