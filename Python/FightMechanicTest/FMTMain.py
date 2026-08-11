import math # For math.floor()
import random # For def randominteger()
import time # For time()

import FMTEnemyRoster # What does this conatin?
import FMTGameLoop # What does this contain?
import FMTPlayer # What does this contain?

def changeturnlength():
    print(f"Current turn length is: {turnlength}")
    userinput = input("\nInput desired turn length: ")
    print(" ")
    #turnlength = float(userinput) # Change string from input to 

if __name__ == "__main__":
        # Start the full game loop
    FMTGameLoop.game_loop()

    #Check nad remove unused imports
    #Update import comments
    #Create new class for gameloop related defs (for example turns, turnlength change etc.)
    #Move existing gameloop related defs into a new class
    #Separate defs and classes into another file?

    #Add legitimate way to revive player
    #Add gear/attributes/something to adjust player stats