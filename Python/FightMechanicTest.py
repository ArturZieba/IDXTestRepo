import math # For math.floor()
import random # For def randominteger
import time # For time()

turnlength = 1 # Constant variable used to adjust time between attack turns

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

# Class containing all of the different enemies with their stats
class EnemyRoster():
    enemy_goblin = {
            "name": "Goblin", 
            "maximumhealth": 10, 
            "currenthealth": 10,
            "damagemin": 1,
            "damagemax": 2,
            "attackspeed": 2,
            "isalive": True,
            "spawnweight": 5,
            "currentexperiencegranted": 2
        }

    enemy_ogre = {
            "name": "Ogre", 
            "maximumhealth": 20, 
            "currenthealth": 20,
            "damagemin": 2,
            "damagemax": 4,
            "attackspeed": 1,
            "isalive": True,
            "spawnweight": 2,
            "currentexperiencegranted": 10
        }

    enemy_dragon = {
            "name": "Dragon", 
            "maximumhealth": 100, 
            "currenthealth": 100,
            "damagemin": 10,
            "damagemax": 50,
            "attackspeed": 3,
            "isalive": True,
            "spawnweight": 1,
            "currentexperiencegranted": 50
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
    def __init__(self, currenthealth = 100, maximumhealth = 100, level = 0, currentexperience = 0, currentexperiencerequired = 5, damagemin = 1, damagemax = 3, attackspeed = 2, isalive = True):#, target = Enemy()): 
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.level = level
        self.currentexperience = currentexperience
        self.currentexperiencerequired = currentexperiencerequired
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

    def info(self):
        print(f"""Player info:

Current Health: {self.currenthealth}
Maximum Health: {self.maximumhealth}
Level: {self.level}
Current Experience: {self.currentexperience}
Required Experience: {self.currentexperiencerequired}
Damage minimum: {self.damagemin}
Damage maximum: {self.damagemax}
Damage current roll: {self.damage}
Attack speed: {self.attackspeed}
Alive: {self.isalive}
=====""")

    def levelup(self):
        if self.currentexperience >= self.currentexperiencerequired:
           self.currentexperience -= self.currentexperiencerequired
           self.currentexperiencerequired = math.floor(self.currentexperiencerequired + (self.currentexperiencerequired / 4))
           self.level += 1
           
           #PLACEHOLDER Rewards for levelling up
           self.maximumhealth += 10
           self.currenthealth = self.maximumhealth
           self.info()

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"Player damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")

    def receiverewards(self, currentexperience):
        self.currentexperience += currentexperience
        self.levelup()
        print(f"\nExperience: {self.currentexperience} - Level: {self.level}")

    def death(self):
        self.isalive = False
        print("\nPlayer dead")

class Enemy:
    def __init__(self, name = "Enemy", currenthealth = 10, maximumhealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True, spawnweight = 0, currentexperiencegranted = 1):#, target = Player()):
        self.name = name
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive
        self.spawnweight = spawnweight
        self.currentexperiencegranted = currentexperiencegranted

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
Experience granted: {self.currentexperiencegranted}
=====""")

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")

    def spawnrandomenemy(self):
        chosenenemy = random.choice(EnemyWeightedListInit.enemyrosterweighted)

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"], chosenenemy["spawnweight"], chosenenemy["currentexperiencegranted"])

    def grantrewards(self, target):
        target.receiverewards(self.currentexperiencegranted)

    def death(self, target):
        self.grantrewards(target)
        self.isalive = False
        print("\nEnemy dead")
        self.spawnrandomenemy()

def player_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    player.attack(enemy)
    enemy.attack(player)
    print(" ")

def enemy_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    enemy.attack(player)
    player.attack(enemy)
    print(" ")

def both_turn(turnlength, player, enemy):
    time.sleep(turnlength)
    player.attack(enemy)
    enemy.attack(player)
    print(" ")

# Run "fight loop" continuously - player and enemy attacking based on their attack speed difference - ends on player death
def run_turns(turnlength, player, enemy):
    while True:
        while player.isalive & enemy.isalive:
            if enemy.currenthealth <= 0:
                enemy.death(player)
            if player.currenthealth <= 0:
                player.death()
                return

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
            if enemy.currenthealth <= 0:
                enemy.death(player)
                return
            if player.currenthealth <= 0:
                player.death()
                return

            if player.attackspeed > enemy.attackspeed:
                player_turn(turnlength, player, enemy)
            if player.attackspeed < enemy.attackspeed:
                enemy_turn(turnlength, player, enemy)
            if player.attackspeed == enemy.attackspeed:
                both_turn(turnlength, player, enemy)

# Main game loop
def game_loop():
    while True:
        print("""
1 - Automatic fight loop
2 - Fight once
3 - Player stats
4 - Enemy stats
5 - Exit
=====""")

        userinput = input("\nInput option number: ")
        print(" ")

        if userinput == "1":
            run_turns(turnlength, playerinstance, enemyinstance)

        elif userinput == "2":
            run_turns_once(turnlength, playerinstance, enemyinstance)
        
        elif userinput == "3":
            playerinstance.info()
        
        elif userinput == "4":
            enemyinstance.info()
        
        elif userinput == "5":
            print("\nExit")
            break

        else:
            print(f"No {userinput} option, type in one of listed numbers") 

if __name__ == "__main__":
    # Create initial Player and Enemy instances
    playerinstance = Player()
    enemyinstance = Enemy()

    # Start the full game loop
    game_loop()

    #Add tabs to input and other prints
    #Add gear/attributes/something to adjust player stats
    #Add comments to the async/turn code here and in the test file
    #What to do when player dies (-exp?)
    #Add some rewards for levelup (increase hp?)

    #Don't start with gameloop, add a switch to choose game/exit/whatever
    #Add console close without ctrl+c (workaround keyboard not being accessible without root)