#import asyncio # For async defs/threading
import math # For math.floor()
import random # For def randominteger
import time # For time()

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

    # Move this outside the def?
    enemyroster = [enemy_goblin, enemy_ogre, enemy_dragon]
        
    # List that is populated with the same dicts as enemyroster, but each dict has as many entries as specified in spawnweight variable
    enemyrosterweighted = []

    for element in enemyroster:
        for i in range(element["spawnweight"]):
            enemyrosterweighted.append(element)

    # Check random distribution with a loop
        #for i in range(100):
        #    print(random.choice(enemyrosterweighted))

class Player:
    def __init__(self, maximumhealth = 10, currenthealth = 10, level = 0, experience = 0, experiencerequired = 40, damagemin = 1, damagemax = 3, attackspeed = 2, isalive = True):#, target = Enemy()): 
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
        
        if (self.currenthealth <= 0):
            self.death()

    def receiverewards(self, experience):
        self.experience += experience
        self.levelup()

    def death(self):
        print("Player dead")
        self.isalive = False

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
        
        if (self.currenthealth <= 0):
            self.death()

    def spawnrandomenemy(self):
        chosenenemy = random.choice(EnemyRoster.enemyrosterweighted)

        # Initialize Enemy class with values of a randomly chosen enemy - "spawn" it
        self.__init__(chosenenemy["name"], chosenenemy["maximumhealth"], chosenenemy["currenthealth"], chosenenemy["damagemin"], chosenenemy["damagemax"], chosenenemy["attackspeed"], chosenenemy["isalive"], chosenenemy["spawnweight"], chosenenemy["experiencegranted"])

    def grantrewards(self, target):
        target.receiverewards(self.experiencegranted)

    def death(self, target):
        self.grantrewards(target)
        print("Enemy dead")
        self.isalive = False
        self.spawnrandomenemy()
        
#async def player_thread(player, enemy):
#    #while player.isalive == True: #player.isalive == True and enemy.isalive == True:
#        print("Player attacking")
#        player.attack(enemy)
#        time.sleep(player.attackspeed) # Better way of doing attacks per time interval?

#async def enemy_thread(enemy, player):
#    #while enemy.isalive == True: #enemy.isalive == True and player.isalive == True:
#        print("Enemy attacking")
#        enemy.attack(player)
#        time.sleep(enemy.attackspeed) # Better way of doing attacks per time interval?

#def both_attack(player, enemy):
#    print("Both attacking")
#    player.attack(enemy)
#    enemy.attack(player)
#    time.sleep(player.attackspeed)

#async def run_threads():
#    while True:
#       # If player is faster than enemy, the threads execute player -> enemy
#       if playerinstance.attackspeed > enemyinstance.attackspeed:
#           await asyncio.gather(player_thread(playerinstance, enemyinstance), enemy_thread(enemyinstance, playerinstance))
#           print(f"Bigger: {playerinstance.attackspeed}")
#       # If player is slower than enemy, the threads execute enemy -> player
#       if playerinstance.attackspeed < enemyinstance.attackspeed:
#           await asyncio.gather(enemy_thread(enemyinstance, playerinstance), player_thread(playerinstance, enemyinstance))
#           print(f"Lesser: {playerinstance.attackspeed}")
#       # If player and enemy have the same attackspeed, both get to attack
#       if playerinstance.attackspeed == enemyinstance.attackspeed:
#           both_attack(playerinstance, enemyinstance)
#           print(f"Equal: {playerinstance.attackspeed}")

def player_turn(player, enemy):
    time.sleep(1/player.attackspeed)
    print("Player attacking")
    player.attack(enemy)
    
def enemy_turn(enemy, player):
    time.sleep(1/enemy.attackspeed)
    print("Enemy attacking")
    enemy.attack(player)

def both_turn(player, enemy):
    time.sleep(1/player.attackspeed)
    print("Both attacking")
    player.attack(enemy)
    enemy.attack(player)
    
def run_turns():
    while True:
        if playerinstance.attackspeed > enemyinstance.attackspeed:
            player_turn(playerinstance, enemyinstance)
            enemy_turn(enemyinstance, playerinstance)
            print(f"Bigger: {playerinstance.attackspeed}")
        if playerinstance.attackspeed < enemyinstance.attackspeed:
            enemy_turn(enemyinstance, playerinstance)
            player_turn(playerinstance, enemyinstance)
            print(f"Lesser: {playerinstance.attackspeed}")
        if playerinstance.attackspeed == enemyinstance.attackspeed:
            both_turn(playerinstance, enemyinstance)
            print(f"Equal: {playerinstance.attackspeed}")

playerinstance = Player()#(10, 10, 0, 0, 40, 1, 3, 2, True, enemyinstance)
enemyinstance = Enemy()#("Enemy", 10, 10, 1, 3, 1, True, 0, 1, playerinstance)

if __name__ == "__main__":
   playerinstance.info()
   enemyinstance.info()
   
   # Run "gameplay loop" - player and enemy attacking based on their attack speed
   #asyncio.run(run_threads())

   run_turns()

   #player_thread = threading.Thread(target=player_thread(playerinstance, enemyinstance))
   #enemy_thread = threading.Thread(target=enemy_thread(enemyinstance, playerinstance))
   #player_thread.start()
   #enemy_thread.start()
   #player_thread.join()
   #enemy_thread.join()

   #Subtract time it took for one entity to attack from another's attack (so if attack times are e.g. 1s and 1.5s then it takes 1.5s per both turns total not 2.5s from waiting 1s and 1.5s for another)
   #Adjust death() defs
   #Are threads even necessary in the current setup?
   #Add comments to the async/turn code here and in the test file
   #Add console close without ctrl+c