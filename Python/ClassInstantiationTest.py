import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

class EnemyRoster():
    enemy_goblin = {
            "name": "Goblin", 
            "maximumhealth": 10, 
            "currenthealth": 10,
            "damagemin": 1,
            "damagemax": 2,
            "attackspeed": 2,
            "isalive": True,
            "spawnweight": 5
        }

    enemy_ogre = {
            "name": "Ogre", 
            "maximumhealth": 20, 
            "currenthealth": 20,
            "damagemin": 2,
            "damagemax": 4,
            "attackspeed": 1,
            "isalive": True,
            "spawnweight": 2
        }

    enemy_dragon = {
            "name": "Dragon", 
            "maximumhealth": 100, 
            "currenthealth": 100,
            "damagemin": 10,
            "damagemax": 50,
            "attackspeed": 1.5,
            "isalive": True,
            "spawnweight": 1
        }

class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True): 
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

    def info(self):
        print(f"""Player info:
        Maximum health: {self.maximumhealth}
        Current health: {self.currenthealth}
        Damage minimum: {self.damagemin}
        Damage maximum: {self.damagemax}
        Damage current roll: {self.damage}
        Attack speed: {self.attackspeed}
        Alive: {self.isalive}
        """)
        print("=====")

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
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True, spawnweight = 0):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive
        self.spawnweight = spawnweight

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
        """)
        print("=====")

    def attack(self, target):
        target.receivedamage(self.damage)
        print(f"{self.name} damage dealt: {self.damage}")
        self.damage = randominteger(self.damagemin, self.damagemax)

    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"{self.name} health: {self.currenthealth} / {self.maximumhealth}")
        
        if (self.currenthealth <= 0):
            self.death()

    def spawnrandomenemy(self):
        enemy_goblin = {
            "name": "Goblin", 
            "maximumhealth": 10, 
            "currenthealth": 10,
            "damagemin": 1,
            "damagemax": 2,
            "attackspeed": 2,
            "isalive": True,
            "spawnweight": 5
        }

        enemy_ogre = {
            "name": "Ogre", 
            "maximumhealth": 20, 
            "currenthealth": 20,
            "damagemin": 2,
            "damagemax": 4,
            "attackspeed": 1,
            "isalive": True,
            "spawnweight": 2
        }

        enemy_dragon = {
            "name": "Dragon", 
            "maximumhealth": 100, 
            "currenthealth": 100,
            "damagemin": 10,
            "damagemax": 50,
            "attackspeed": 1.5,
            "isalive": True,
            "spawnweight": 1
        }

        # Move this outside the def?
        enemyroster = [EnemyRoster.enemy_goblin, EnemyRoster.enemy_ogre, EnemyRoster.enemy_dragon]
        
        # List that is populated with the same dicts as enemyroster, but each dict has as many entries as specified in spawnweight variable
        enemyrosterweighted = []

        for element in enemyroster:
            for i in range(element["spawnweight"]):
                enemyrosterweighted.append(element)

        # Move outside this def?
        # Check random distribution with a loop
        for i in range(100):
            print(random.choice(enemyrosterweighted))

        chosenenemy = random.choice(enemyrosterweighted)

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"], chosenenemy["spawnweight"])

    def death(self):
        print("Enemy dead")
        self.isalive = False
        self.spawnrandomenemy()
        
playerinstance = Player()
enemyinstance = Enemy()

playerinstance.info()
enemyinstance.info()

enemyinstance.death()
enemyinstance.info()