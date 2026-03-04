import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

def randomenemy():
    name = "Respawned" 
    maximumhealth = randominteger(10, 100) 
    currenthealth = maximumhealth
    damagemin = randominteger(2, 10)
    damagemax = randominteger(12, 20)
    attackspeed = 2
    isalive = True

    return name, maximumhealth, currenthealth, damagemin, damagemax, attackspeed, isalive

class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True): 
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"Player damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")
        
        if (self.currenthealth <= 0):
            self.death()

    def death(self):
        print("Player dead")
        self.isalive = False

class Enemy:
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")
        
        if (self.currenthealth <= 0):
            self.death()

    def death(self):
        print("Enemy dead")
        self.isalive = False
        self.__init__(randomenemy())
        # Change to premade sets of values that are randomly chosen
        # Def for returning base stats of Enemy/Player objects

playerinstance = Player()
enemyinstance = Enemy()

#print("Player: ")
#print(playerinstance.maximumhealth)
#print(playerinstance.currenthealth)
#print(playerinstance.damage)
#print(playerinstance.attackspeed)
#print(playerinstance.isalive)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
playerinstance.attack(enemyinstance)
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
#enemyinstance.attack(playerinstance)