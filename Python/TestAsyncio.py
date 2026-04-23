#import asyncio # For async defs/threading
from threading import Thread # For Thread()

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

#def thread_test_one():
#    for i in range(100):
#        print("Test thread one")

#def thread_test_two():
#    for i in range(100):
#        print("Test thread two")

#async def run_test_threads():
#    await asyncio.gather(thread_test_one(), thread_test_two()) # Make threads loop?

#asyncio.run(run_test_threads())

print("Test")
#thread1 = Thread(target = thread_test_one())
#thread2 = Thread(target = thread_test_two())

#thread1.start()
#thread2.start()

# Queue threads based on attack speed?