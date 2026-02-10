import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class Player:
    maximumhealth = 20
    currenthealth = maximumhealth
    damage = randominteger(2, 5)
    attackspeed = 0.5
    isalive = True

    def attack(damage):
        Enemy.receivedamage(damage)
        print(f"Player damage dealt: {Player.damage}")

    def receivedamage(damage):
        Player.currenthealth -= damage
        print(f"Player health: {Player.currenthealth} / {Player.maximumhealth}")
        
        if (Player.currenthealth <= 0):
            Player.death()

    def death():
        print("Player dead")
        Player.isalive = False

class Enemy:
    maximumhealth = 10
    currenthealth = maximumhealth
    damage = randominteger(1, 3)
    attackspeed = 1
    isalive = True

    def attack(damage):
        Player.receivedamage(damage)
        print(f"Enemy damage dealt: {Enemy.damage}")

    def receivedamage(damage):
        Enemy.currenthealth -= damage
        print(f"Enemy health: {Enemy.currenthealth} / {Enemy.maximumhealth}")
        
        if (Enemy.currenthealth <= 0):
            Enemy.death()

    def death():
        print("Enemy dead")
        Enemy.isalive = False

print(Player.maximumhealth)
print(Enemy.maximumhealth)