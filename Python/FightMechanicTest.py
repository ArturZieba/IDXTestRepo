import random # For def randominteger
import threading # For threading.Thread()
import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger



class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, damage = randominteger(1, 3), attackspeed = 1, isalive = True): 
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = damage
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
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, damage = randominteger(1, 3), attackspeed = 1, isalive = True):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = damage
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

playerinstance = Player()
enemyinstance = Enemy()
        
def player_thread_function(player, enemy):
    while player.isalive == True and enemy.isalive == True:
        print("Player attacking")
        player.attack(player.damage)
        time.sleep(player.attackspeed)

    if player.isalive == False:
        player = Enemy(15, 15, 2, 4, randominteger(2, 4), 2)

def enemy_thread_function(enemy, player):
    while enemy.isalive == True and player.isalive == True:
        print("Enemy attacking")
        enemy.attack(enemy.damage)
        time.sleep(enemy.attackspeed)
    
    if enemyinstance.isalive == False:
        enemyinstance = Enemy("Resurrected", 15, 15, 2, 4, randominteger(2, 4), 2)

#if __name__ == "__main__":
#   player_thread = threading.Thread(target=player_thread_function(playerinstance, enemyinstance))
#   enemy_thread = threading.Thread(target=enemy_thread_function(enemyinstance, playerinstance))
#   player_thread.start()
#   enemy_thread.start()
    #Add console close without ctrl+c
    #Go back to separate file to test respawning?