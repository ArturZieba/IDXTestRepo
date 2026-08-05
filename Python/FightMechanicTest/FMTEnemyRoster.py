# Class containing all of the different enemies with their stats, as well as initialization of a weighted spawn list of those enemies
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

    # List of all monsters available to spawn
    enemyroster = [enemy_goblin, enemy_ogre, enemy_dragon]
        
    # List that is populated with the same dicts as enemyroster, but each dict has as many entries as specified in spawnweight variable
    enemyrosterweighted = []

    # Add as many elements of enemy type to the enemyrosterweighted as high is the spawnweight value
    for element in enemyroster:
        for i in range(element["spawnweight"]):
            enemyrosterweighted.append(element)