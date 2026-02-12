import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, damage = randominteger(1, 3), attackspeed = 1, isalive = True):
        self.maximumhealth, self.currenthealth, self. damage, self.attackspeed, self.isalive = maximumhealth, currenthealth, damage, attackspeed, isalive
#split
    #def attack(damage):
    #    Enemy.receivedamage(damage)
    #    print(f"Player damage dealt: {Player.damage}")

    #def receivedamage(damage):
    #    Player.currenthealth -= damage
    #    print(f"Player health: {Player.currenthealth} / {Player.maximumhealth}")
        
    #    if (Player.currenthealth <= 0):
    #        Player.death()

    #def death():
    #    print("Player dead")
    #    Player.isalive = False

class Enemy:
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damage = randominteger(1, 3), attackspeed = 1, isalive = True):
        self.name, self.maximumhealth, self.currenthealth, self. damage, self.attackspeed, self.isalive = name, maximumhealth, currenthealth, damage, attackspeed, isalive
#split
    #def attack(damage):
    #    Player.receivedamage(damage)
    #    print(f"Enemy damage dealt: {Enemy.damage}")

    #def receivedamage(damage):
    #    Enemy.currenthealth -= damage
    #    print(f"Enemy health: {Enemy.currenthealth} / {Enemy.maximumhealth}")
        
    #   if (Enemy.currenthealth <= 0):
    #        Enemy.death()

    #def death():
    #    print("Enemy dead")
    #    Enemy.isalive = False

playerinstance = Player()
enemyinstance = Enemy()

print("Player: ")
print(playerinstance.maximumhealth)
print(playerinstance.currenthealth)
print(playerinstance.damage)
print(playerinstance.attackspeed)
print(playerinstance.isalive)

print("Enemy: ")
print(enemyinstance.name)
print(enemyinstance.maximumhealth)
print(enemyinstance.currenthealth)
print(enemyinstance.damage)
print(enemyinstance.attackspeed)
print(enemyinstance.isalive)