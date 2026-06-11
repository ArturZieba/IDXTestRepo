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
            "experiencegranted": 2
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
            "experiencegranted": 10
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
    def __init__(self, maximumhealth = 100, currenthealth = 100, level = 0, experience = 0, experiencerequired = 40, damagemin = 1, damagemax = 3, attackspeed = 2, isalive = True):#, target = Enemy()): 
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.level = level
        self.experience = experience
        self.experiencerequired = experiencerequired
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive
        #self.target = target

    def info(self):
        print(f"""Player info:
        Maximum health: {self.maximumhealth}
        Current health: {self.currenthealth}
        Level: {self.level}
        Experience: {self.experience}
        Required Experience: {self.experiencerequired}
        Damage minimum: {self.damagemin}
        Damage maximum: {self.damagemax}
        Damage current roll: {self.damage}
        Attack speed: {self.attackspeed}
        Alive: {self.isalive}
        """)
        print("=====")

    def levelup(self):
        if self.experience >= self.experiencerequired:
           self.experience -= self.experiencerequired
           self.experiencerequired = math.floor(self.experiencerequired + (self.experiencerequired / 4))
           self.level += 1

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"Player damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")
        
        #if (self.currenthealth <= 0):
        #    self.death()

    def receiverewards(self, experience):
        self.experience += experience
        self.levelup()

    def death(self):
        self.isalive = False
        print("Player dead")

class Enemy:
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True, spawnweight = 0, experiencegranted = 1):#, target = Player()):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive
        self.spawnweight = spawnweight
        self.experiencegranted = experiencegranted
        #self.target = target

    def info(self):
        print(f"""Enemy info:
        Name: {self.name}
        Maximum health: {self.maximumhealth}
        Current health: {self.currenthealth}
        Damage minimum: {self.damagemin}
        Damage maximum: {self.damagemax}
        Damage current roll: {self.damage}
        Attack speed: {self.attackspeed}
        Alive: {self.isalive}
        Spawn weight: {self.spawnweight}
        Experience granted: {self.experiencegranted}
        """)
        print("=====")

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")
        
        #if (self.currenthealth <= 0):
        #    self.death()

    def spawnrandomenemy(self):
        chosenenemy = random.choice(EnemyWeightedListInit.enemyrosterweighted)

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"], chosenenemy["spawnweight"], chosenenemy["experiencegranted"])

    def grantrewards(self, target):
        target.receiverewards(self.experiencegranted)

    def death(self):#, target):
        #self.grantrewards(target)
        self.isalive = False
        print("Enemy dead")
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

def run_turns(turnlength, player, enemy):
    while True:
        while player.isalive & enemy.isalive:
            if enemy.currenthealth <= 0:
                enemy.death()
                #return
            if player.currenthealth <= 0:
                player.death()
                return

            if player.attackspeed > enemy.attackspeed:
                player_turn(turnlength, player, enemy)
            if player.attackspeed < enemy.attackspeed:
                enemy_turn(turnlength, player, enemy)
            if player.attackspeed == enemy.attackspeed:
                both_turn(turnlength, player, enemy)
            
playerinstance = Player()#(10, 10, 0, 0, 40, 1, 3, 2, True, enemyinstance)
enemyinstance = Enemy()#("Enemy", 10, 10, 1, 3, 1, True, 0, 1, playerinstance)

if __name__ == "__main__":
    playerinstance.info()
    enemyinstance.info()
   
    # Run "gameplay loop" - player and enemy attacking based on their attack speed difference
    run_turns(turnlength, playerinstance, enemyinstance)

    #Adjust death() defs
    #Add comments to the async/turn code here and in the test file
    #Add console close without ctrl+c