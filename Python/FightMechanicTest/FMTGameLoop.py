import math # For math.floor()
import time # For time()

import FMTEnemy # For Enemy() class
import FMTPlayer #  For Player() class

global turnlength # Initialize turnlength as global variable so that it can be used in different defs
turnlength = 0.5 # Float variable used to adjust time between attack turns (lower means faster, higher means slower - for example 0.5 means it takes 0.5s between turns, while 2.0 means it takes 2s between turns)

# Create initial Player and Enemy instances
playerinstance = FMTPlayer.Player()
enemyinstance = FMTEnemy.Enemy()

# Adjust turnlength value while the program is running
def changeturnlength():
    global turnlength
    print(f"Current turn length is: {turnlength}")
    userinput = input("\nInput desired turn length: ")
    print(" ")
    turnlength = float(userinput) # Change string from input to float to make sure it works with other defs using this variable
    print(f"\nTurn length set to: {turnlength}\n")

def playerrevive():
    playerinstance.currenthealth = playerinstance.maximumhealth
    playerinstance.isalive = True

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
                enemyinstance.spawnrandomenemy()
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
                enemyinstance.spawnrandomenemy()
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
            if playerinstance.isalive == True:
                run_turns(turnlength, playerinstance, enemyinstance)
            else:
                print("Player is dead\n")
                userinput = input("""\n1 - Revive for X gold with full Health
2 - Revive for free with half Health                
Choose a way to revive: """)
                if userinput == "1":
                    playerrevive()
                    print("""\nPaid X gold
Reviving with full Health\n""")
                elif userinput == "2":
                    playerrevive()
                    playerinstance.currenthealth = math.floor(playerinstance.maximumhealth / 2)
                    print("\nReviving with half Health\n")

        # 2 - Fight once
        elif userinput == "2":
            if playerinstance.isalive == True:
                run_turns_once(turnlength, playerinstance, enemyinstance)
            else:
                print("Player is dead\n")
                userinput = input("""\n1 - Revive for X gold with full Health
2 - Revive for free with half Health                
Choose a way to revive: """)
                if userinput == "1":
                    playerrevive()
                    print("""\nPaid X gold
Reviving with full Health\n""")
                elif userinput == "2":
                    playerrevive()
                    playerinstance.currenthealth = math.floor(playerinstance.maximumhealth / 2)
                    print("\nReviving with half Health\n")
            
        
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
            playerrevive()
            print("Revived player with current health set to maximum health\n")

        # g - Set current and maximum player health
        elif userinput == "g":
            userinput = input("\nInput desired player maximum health: ")
            print(" ")
            playerinstance.maximumhealth = int(userinput) # Change string from input to integer to avoid issues with value comparison
            playerinstance.currenthealth = playerinstance.maximumhealth
            print(f"Maximum health set to {userinput}\n")

        # n - Reroll current enemy
        elif userinput == "n":
            enemyinstance.spawnrandomenemy()
            print(f"Enemy rerolled to {enemyinstance.name}\n")

        # t - Set turn length
        elif userinput == "t":
            changeturnlength()

        # Input not listed is provided
        else:
            print(f"No {userinput} option, type in one of listed numbers")