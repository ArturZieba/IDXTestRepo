import FMTEnemyRoster
import FMTTools

class Enemy:
    def __init__(self, name = "Enemy", currenthealth = 10, maximumhealth = 10, damagemin = 1, damagemax = 3, attackspeed = 1, isalive = True, spawnweight = 0, level = 0, experiencegranted = 1):#, target = Player()):
        self.name = name
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = FMTTools.randominteger(damagemin, damagemax)
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
        self.damage = FMTTools.randominteger(self.damagemin, self.damagemax)

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