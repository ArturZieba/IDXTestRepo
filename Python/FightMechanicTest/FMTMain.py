import math # For math.floor()
import random # For def randominteger()
import time # For time()

import FMTEnemyRoster # What does this conatin?
import FMTGameLoop # What does this contain?
import FMTPlayer # What does this contain?

turnlength = 0.5 # Float variable used to adjust time between attack turns (lower means faster, higher means slower, see turn defs implementation for details)

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

def changeturnlength():
    print(f"Current turn length is: {turnlength}")
    userinput = input("\nInput desired turn length: ")
    print(" ")
    #turnlength = float(userinput) # Change string from input to 

class Enemy:
    def __init__(self, name = "Enemy", currenthealth = 10, maximumhealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True, spawnweight = 0, level = 0, experiencegranted = 1):#, target = Player()):
        self.name = name
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive
        self.spawnweight = spawnweight
        self.level = level
        self.experiencegranted = experiencegranted

    # Print full enemy stats info
    def info(self):
        print(f"""Enemy info:

Name: {self.name}
Current Health: {self.currenthealth}
Maximum Health: {self.maximumhealth}
Damage minimum: {self.damagemin}
Damage maximum: {self.damagemax}
Damage current roll: {self.damage}
Attack speed: {self.attackspeed}
Alive: {self.isalive}
Spawn weight: {self.spawnweight}
Level: {self.level}
Experience granted: {self.experiencegranted}
=====\n""")

    # Attack a target
    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    # Receive damage from a source
    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")

    # Reinitialize the instance with a random chosen enemy type - basically respawn without creating a new instance of the class
    def spawnrandomenemy(self):
        # Choose a random enemy from a weighted list at random
        chosenenemy = FMTEnemyRoster.EnemyRoster.chooserandomenemy()

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"], chosenenemy["spawnweight"], chosenenemy["level"], chosenenemy["experiencegranted"])

    # Grant rewards to the source that caused death
    def grantrewards(self, target):
        target.receiverewards(self.experiencegranted)

    # Death once currenthealth reaches 0 or less
    def death(self, target):
        self.grantrewards(target)
        self.isalive = False
        print("Enemy dead")
        print(f"Experience granted: {self.experiencegranted}\n")
        self.spawnrandomenemy()

# Turns when player's attackspeed is higher than the enemy's
def player_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    player.attack(enemy)
    enemy.attack(player)
    print(" ")

# Turns when enemy's attackspeed is higher than the player's
def enemy_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    enemy.attack(player)
    player.attack(enemy)
    print(" ")

# Turns when both the player and enemy attackspeed values are equal
def both_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    player.attack(enemy)
    enemy.attack(player)
    print(" ")

# Run "fight loop" continuously - player and enemy attacking based on their attack speed difference - ends on player death
def run_turns(turnlength, player, enemy):
    while True:
        while player.isalive & enemy.isalive:
            # First check if player or enemy have more than 0 currenthealth
            if enemy.currenthealth <= 0:
                enemy.death(player)
                # No return statement here, keeps going on until player's death in the return statement
            if player.currenthealth <= 0:
                player.death()
                return # Exit loop when player dies

            # If both the player and enemy remain alive then run turns based on their attackspeed
            if player.attackspeed > enemy.attackspeed:
                player_turn(turnlength, player, enemy)
            if player.attackspeed < enemy.attackspeed:
                enemy_turn(turnlength, player, enemy)
            if player.attackspeed == enemy.attackspeed:
                both_turn(turnlength, player, enemy)

# Run "fight loop" once - player and enemy attacking based on their attack speed difference - ends on player or enemy death
def run_turns_once(turnlength, player, enemy):
    while True:
        while player.isalive & enemy.isalive:
            # First check if player or enemy have more than 0 currenthealth
            if enemy.currenthealth <= 0:
                enemy.death(player)
                return # Exit loop when enemy dies
            if player.currenthealth <= 0:
                player.death()
                return # Exit loop when player dies

            # If both the player and enemy remain alive then run turns based on their attackspeed
            if player.attackspeed > enemy.attackspeed:
                player_turn(turnlength, player, enemy)
            if player.attackspeed < enemy.attackspeed:
                enemy_turn(turnlength, player, enemy)
            if player.attackspeed == enemy.attackspeed:
                both_turn(turnlength, player, enemy)

# Main game loop
def game_loop():
    while True:
        print("""1 - Automatic fight loop
2 - Fight once
3 - Player stats
4 - Enemy stats
5 - Exit

DEBUG
r - Revive player
g - Set current and maximum player health
n - Reroll current enemy
t - Set turn length
=====""")

        # Input for the main menu selection
        userinput = input("\nInput option chosen: ")
        print(" ")

        # 1 - Automatic fight loop
        if userinput == "1":
            run_turns(turnlength, playerinstance, enemyinstance)

        # 2 - Fight once
        elif userinput == "2":
            run_turns_once(turnlength, playerinstance, enemyinstance)
        
        # 3 - Player stats
        elif userinput == "3":
            playerinstance.info()
        
        # 4 - Enemy stats
        elif userinput == "4":
            enemyinstance.info()
        
        # 5 - Exit
        elif userinput == "5":
            print("Exitting script")
            break

        # r - Revive player
        elif userinput == "r":
            playerinstance.currenthealth = playerinstance.maximumhealth
            playerinstance.isalive = True
            print("Revived player with current health set to maximum health\n")

        # g - Set current and maximum player health
        elif userinput == "g":
            userinput = input("\nInput desired player maximum health: ")
            print(" ")
            playerinstance.maximumhealth = int(userinput) # Change string from input to integer to avoid issues with value comparison
            playerinstance.currenthealth = playerinstance.maximumhealth

        # n - Reroll current enemy
        elif userinput == "n":
            enemyinstance.spawnrandomenemy()

        # t - Set turn length
        elif userinput == "t":
            changeturnlength()

        else:
            print(f"No {userinput} option, type in one of listed numbers") 

if __name__ == "__main__":
    # Create initial Player and Enemy instances
    playerinstance = FMTPlayer.Player()
    enemyinstance = Enemy()

    # Start the full game loop
    game_loop()

    #Update import comments
    #Create new class for gameloop related defs (for example turns, turnlength change etc.)
    #Move existing gameloop related defs into a new class
    #Separate defs and classes into another file?

    #Add legitimate way to revive player
    #Add gear/attributes/something to adjust player stats