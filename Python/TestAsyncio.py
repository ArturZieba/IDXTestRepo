import asyncio # For async defs/threading

#async def player_thread_function(player, enemy):
#    while player.isalive == True: #player.isalive == True and enemy.isalive == True:
#        print("Player attacking")
#        player.attack(enemy)
#        time.sleep(player.attackspeed) # Better way of doing attacks per time interval?

#async def enemy_thread_function(enemy, player):
#    while enemy.isalive == True: #enemy.isalive == True and player.isalive == True:
#        print("Enemy attacking")
#        enemy.attack(player)
#        time.sleep(enemy.attackspeed) # Better way of doing attacks per time interval?

#async def run_threads():
#    await asyncio.gather(player_thread_function(playerinstance, enemyinstance), enemy_thread_function(enemyinstance, playerinstance))

async def thread_test_one():
    print("Test thread one")

async def thread_test_two():
    print("Test thread two")

async def run_test_threads():
    await asyncio.gather(thread_test_one(), thread_test_two()) # Make threads loop?

print("Test")
asyncio.run(run_test_threads())