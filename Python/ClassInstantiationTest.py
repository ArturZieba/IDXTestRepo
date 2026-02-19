import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, damage = randominteger(1, 3), attackspeed = 1, isalive = True): 
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self. damage = damage
        self.attackspeed = attackspeed
        self.isalive = isalive

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"Player damage dealt: {self.damage}")
        self.damage = randominteger(1, 3)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")
        
        if (self.currenthealth <= 0):
            self.death()

    def death(self):
        print("Player dead")
        self.isalive = False

class Enemy:
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damage = randominteger(1, 3), attackspeed = 1, isalive = True):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self. damage = damage
        self.attackspeed = attackspeed
        self.isalive = isalive

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(1, 3)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")
        
        if (self.currenthealth <= 0):
            self.death()

    def death(self):
        print("Enemy dead")
        self.isalive = False

# Move random damage roll into it's own variable/def?

playerinstance = Player()
enemyinstance = Enemy()

print("Player: ")
print(playerinstance.maximumhealth)
print(playerinstance.currenthealth)
print(playerinstance.damage)
print(playerinstance.attackspeed)
print(playerinstance.isalive)
playerinstance.attack(enemyinstance)


print(" ")
print("=======")
print(" ")

print("Enemy: ")
print(enemyinstance.name)
print(enemyinstance.maximumhealth)
print(enemyinstance.currenthealth)
print(enemyinstance.damage)
print(enemyinstance.attackspeed)
print(enemyinstance.isalive)
enemyinstance.attack(playerinstance)
