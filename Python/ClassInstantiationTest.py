import random # For def randominteger
#import threading # For threading.Thread()
#import time # For time()

# Roll a random integer in min/max range
def randominteger(min, max):
    generatedinteger = random.randint(min, max)
    return generatedinteger

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
    def __init__(self, name = "Enemy", maximumhealth = 10, currenthealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True):
        self.name = name
        self.maximumhealth = maximumhealth
        self.currenthealth = currenthealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = randominteger(damagemin, damagemax)
        self.attackspeed = attackspeed
        self.isalive = isalive

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
        goblindict = {
            "name": "Goblin", 
            "maximumhealth": 10, 
            "currenthealth": 10,
            "damagemin": 1,
            "damagemax": 2,
            "attackspeed": 2,
            "isalive": True
        }

        ogredict = {
            "name": "Ogre", 
            "maximumhealth": 20, 
            "currenthealth": 20,
            "damagemin": 2,
            "damagemax": 4,
            "attackspeed": 1,
            "isalive": True
        }

        enemyroster = [goblindict, ogredict]

        chosenenemy = random.choice(enemyroster)

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"])

    def death(self):
        print("Enemy dead")
        self.isalive = False
        self.spawnrandomenemy()
        # Change to premade sets of values that are randomly chosen
        # Def for returning base stats of Enemy/Player objects
        
playerinstance = Player()
enemyinstance = Enemy()

playerinstance.info()
enemyinstance.info()

enemyinstance.death()
enemyinstance.info()