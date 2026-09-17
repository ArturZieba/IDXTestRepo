import FMTGameLoop # For game_loop() def

if __name__ == "__main__":
    # Start the full game loop
    FMTGameLoop.game_loop()

    #Keep gameloop menu in a separate def or move back to gameloop? Separating would allow different options to be added
    #Update comments
    #Move player dead prompts to a separate def
    #Game loop for certain number of kills? (i.e. stop after 5 kills or player death)
    #Further work on a legitimate way to revive player
    #Add option to revive player for free/gold?
    #Add a safeguard for starting the game if player is dead
    #Add gear/attributes/something to adjust player stats