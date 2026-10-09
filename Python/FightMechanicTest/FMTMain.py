import FMTGameLoop # For game_loop() def

if __name__ == "__main__":
    # Start the full game loop
    FMTGameLoop.game_loop()
    
    #Add feedback on return in run_turns_multiple and make sure non-ints cant be passed
    #Change check of userinput in run_turns_multiple for only range of integers 1 - 100
    #Fix the loop in run_turns_multiple starting another turn after finishing
    #Change def run tuns defs naming scheme
    #Split multiple turn runs and multiple enemy fights
    
    #Game loop for certain number of kills? (i.e. stop after 5 kills or player death)
    #Further work on a legitimate way to revive player
    #Add option to revive player for free/gold?
    #Add a safeguard for starting the game if player is dead
    #Add gear/attributes/something to adjust player stats