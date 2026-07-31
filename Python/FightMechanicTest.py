import math # For math.floor()
import random # For def randominteger()
import time # For time()

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

# Class containing all of the different enemies with their stats
class EnemyRoster():
    enemy_goblin = {
            "name": "Goblin",
            "currenthealth": 10, 
            "maximumhealth": 10, 
            "damagemin": 1,
            "damagemax": 2,
            "attackspeed": 2,
            "isalive": True,
            "spawnweight": 5,
            "level": 1,
            "experiencegranted": 2
        }

    enemy_ogre = {
            "name": "Ogre",
            "currenthealth": 20,
            "maximumhealth": 20, 
            "damagemin": 2,
            "damagemax": 4,
            "attackspeed": 1,
            "isalive": True,
            "spawnweight": 2,
            "level": 2,
            "experiencegranted": 10
        }

    enemy_dragon = {
            "name": "Dragon", 
            "currenthealth": 100,
            "maximumhealth": 100, 
            "damagemin": 10,
            "damagemax": 50,
            "attackspeed": 3,
            "isalive": True,
            "spawnweight": 1,
            "level": 3,
            "experiencegranted": 50
        }

# Class containing enemy weighted spawn list initialization
class EnemyWeightedListInit():
    # List of all monsters available to spawn
    enemyroster = [EnemyRoster.enemy_goblin, EnemyRoster.enemy_ogre, EnemyRoster.enemy_dragon]
        
    # List that is populated with the same dicts as enemyroster, but each dict has as many entries as specified in spawnweight variable
    enemyrosterweighted = []

    # Add as many elements of enemy type to the enemyrosterweighted as high is the spawnweight value
    for element in enemyroster:
        for i in range(element["spawnweight"]):
            enemyrosterweighted.append(element)

class Player:
    def __init__(self, currenthealth = 100, maximumhealth = 100, level = 0, currentexperience = 0, experiencerequired = 5, damagemin = 1, damagemax = 3, attackspeed = 2, isalive = True):#, target = Enemy()): 
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.level = level
        self.currentexperience = currentexperience
        self.experiencerequired = experiencerequired
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

    # Print full player stats info
    def info(self):
        print(f"""Player info:

Current Health: {self.currenthealth}
Maximum Health: {self.maximumhealth}
Level: {self.level}
Current Experience: {self.currentexperience}
Required Experience: {self.experiencerequired}
Damage minimum: {self.damagemin}
Damage maximum: {self.damagemax}
Damage current roll: {self.damage}
Attack speed: {self.attackspeed}
Alive: {self.isalive}
=====\n""")

    # Level up the player once he reaches required experience
    def levelup(self):
        # "while" instead of if "in" case that enough experience is earned for more than one level up in one instance
        while self.currentexperience >= self.experiencerequired:
           self.currentexperience -= self.experiencerequired

           # Raise required experience for the next level based on a formula (TBD)
           self.experiencerequired = math.floor(self.experiencerequired + (self.experiencerequired / 4))
           self.level += 1
           
           # PLACEHOLDER Rewards for levelling up
           self.maximumhealth += 10
           self.currenthealth = self.maximumhealth
           #self.info()

           print(f"""Player Level: {self.level}
Experience: {self.currentexperience} / {self.experiencerequired}\n""")

    # Attack a target
    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"Player damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    # Receive damage from a source
    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")

    # Receive rewards from a source
    def receiverewards(self, currentexperience):
        self.currentexperience += currentexperience
        self.levelup()

    # Death once currenthealth reaches 0 or less
    def death(self):
        self.isalive = False
        # If player has any currentexperience, remove a percentage of it 
        if self.currentexperience > 0:
            removedexperience = math.floor(self.currentexperience * 0.10) # The multiplier is the percentage of currentexperience removed - for example * 0.10 will remove 10% of current experience rounded down (due to math.floor())
            self.currentexperience -= removedexperience
            print(f"""Player dead
Lost {removedexperience} Experience\n""")
        
        else: 
            print("Player dead\n")

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
        chosenenemy = random.choice(EnemyWeightedListInit.enemyrosterweighted)

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
    playerinstance = Player()
    enemyinstance = Enemy()

    # Start the full game loop
    game_loop()

    #Create new class for gameloop related defs (for example turns, turnlength change etc.)
    #Move existing gameloop related defs into a new class
    #Separate defs and classes into another file?

    #Add legitimate way to revive player
    #Add gear/attributes/something to adjust player stats