import random # For random.choice() def

# Class containing all of the different enemies with their stats, as well as initialization of a weighted spawn list of those enemies
class EnemyRoster():
    # Goblin (Level 1)
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

    #Ogre (Level 2)
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

    # Dragon (Level 3)
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

    # List of all monsters available to spawn
    enemyroster = [enemy_goblin, enemy_ogre, enemy_dragon]
        
    # List initialization that is populated in the following loop with the same dicts as enemyroster, but each dict has as many entries as specified in spawnweight variable
    enemyrosterweighted = []

    # Populate enemyrosterweighted with elements of enemy type based on their individual spawnweight value (for example: goblin spawnweight is 10 so add 10 goblin elements to the list; dragon spawnweight is 1 so add 1 dragon element to the list)
    for element in enemyroster:
        for i in range(element["spawnweight"]):
            enemyrosterweighted.append(element)
    
    # Choose a random enemy from the weighted list
    def chooserandomenemy():
        chosenenemy = random.choice(EnemyRoster.enemyrosterweighted)
        return chosenenemy