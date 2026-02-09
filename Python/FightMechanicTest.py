import random # For def randominteger
import threading # For threading.Thread()
import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

def player_thread_function():
    while Player.isalive == True and Enemy.isalive == True:
        print("Player attacking")
        Player.attack(Player.damage)
        time.sleep(Player.attackspeed)

def enemy_thread_function():
    while Enemy.isalive == True and Player.isalive == True:
        print("Enemy attacking")
        Enemy.attack(Enemy.damage)
        time.sleep(Enemy.attackspeed)

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
        
if __name__ == "__main__":
    player_thread = threading.Thread(target=player_thread_function)
    enemy_thread = threading.Thread(target=enemy_thread_function)
    player_thread.start()
    enemy_thread.start()
    #Add console close without ctrl+c