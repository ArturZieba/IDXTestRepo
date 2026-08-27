import math # For floor() def

import FMTTools # For randominteger() def

class Player:
    # Player default values initialization
    def __init__(self, currenthealth = 100, maximumhealth = 100, level = 0, currentexperience = 0, experiencerequired = 5, damagemin = 1, damagemax = 3, attackspeed = 2, isalive = True):#, target = Enemy()): 
        self.currenthealth = currenthealth
        self.maximumhealth = maximumhealth
        self.level = level
        self.currentexperience = currentexperience
        self.experiencerequired = experiencerequired
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.damage = FMTTools.randominteger(damagemin, damagemax)
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

    # Level up the player once they reach required experience
    def levelup(self):
        # "while" instead of "if" in case that enough experience is earned for more than one level up in one instance
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
        self.damage = FMTTools.randominteger(self.damagemin, self.damagemax)

    # Receive damage from a source
    def receivedamage(self, damage):
        self.currenthealth -= damage
        print(f"Player health: {self.currenthealth} / {self.maximumhealth}")

    # Receive rewards from a source
    def receiverewards(self, currentexperience):
        self.currentexperience += currentexperience
        self.levelup()

    # Death once currenthealth reaches 0 or less - This is implemented in FMTGameLoop in the turns defs
    def death(self):
        self.isalive = False
        # If player has any currentexperience, remove a percentage of it 
        if self.currentexperience >= 0:
            removedexperience = math.floor(self.currentexperience * 0.10) # The multiplier is the percentage of currentexperience removed - for example * 0.10 will remove 10% of current experience rounded down (due to math.floor())
            self.currentexperience -= removedexperience
            print(f"""Player dead
Lost {removedexperience} Experience\n""")
        #else: 
        #    print("Player dead\n") # Not needed? Worst case the above print will state "Lost 0 Experience"