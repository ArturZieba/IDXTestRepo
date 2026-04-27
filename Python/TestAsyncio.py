import asyncio # For async defs/threading
from threading import Thread # For Thread()
import time # For time.sleep()

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

async def thread_test_one(attackspeed):
    time.sleep(attackspeed)
    print("Test thread one")

async def thread_test_two(attackspeed):
    time.sleep(attackspeed)
    print("Test thread two")

async def run_test_threads():
    attackspeedone = 2
    attackspeedtwo = 1
    if attackspeedone > attackspeedtwo:
        await asyncio.gather(thread_test_one(attackspeedone), thread_test_two(attackspeedtwo))
        attackspeedone -= 1.5
        print(attackspeedone)
    if attackspeedtwo > attackspeedone:
        await asyncio.gather(thread_test_two(attackspeedtwo), thread_test_one(attackspeedone))
        attackspeedone += 1.5
        print(attackspeedone)
    # if attackspeedone == attackspeedtwo ?



print("Test")
#thread1 = Thread(target = thread_test_one())
#thread2 = Thread(target = thread_test_two())

#thread1.start()
#thread2.start()

# Queue threads based on attack speed?
while True:
    asyncio.run(run_test_threads())
