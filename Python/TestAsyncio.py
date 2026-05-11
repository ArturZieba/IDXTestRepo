import asyncio # For async defs/threading
import time # For time.sleep()

async def thread_test_one(attackspeed):
    time.sleep(attackspeed)
    print("Test thread one")

async def thread_test_two(attackspeed):
    time.sleep(attackspeed)
    print("Test thread two")

async def run_test_threads():
    attackspeedone = 1
    attackspeedtwo = 1
    if attackspeedone > attackspeedtwo:
        await asyncio.gather(thread_test_one(attackspeedone), thread_test_two(attackspeedtwo))
        print(f"Bigger: {attackspeedone}")
    if attackspeedone < attackspeedtwo:
        await asyncio.gather(thread_test_two(attackspeedtwo), thread_test_one(attackspeedone))
        print(f"Lesser: {attackspeedone}")
    if attackspeedone == attackspeedtwo:
        time.sleep(attackspeedone)
        print("Both deal and take damage at the same time")
        print(f"Equal: {attackspeedone}")

def player_turn(attackspeed):
    time.sleep(1/attackspeed)
    print("Player attacks")
    
def enemy_turn(attackspeed):
    time.sleep(1/attackspeed)
    print("Enemy attacks")

def run_turns():
    attackspeedplayer = 1
    attackspeedenemy = 1
    if attackspeedplayer > attackspeedenemy:
        player_turn(attackspeedplayer)
        enemy_turn(attackspeedenemy)
        print(f"Bigger: {attackspeedplayer}")
    if attackspeedplayer < attackspeedenemy:
        enemy_turn(attackspeedenemy)
        player_turn(attackspeedplayer)
        print(f"Lesser: {attackspeedplayer}")
    if attackspeedplayer == attackspeedenemy:
        time.sleep(1/attackspeedplayer) # 1/attackspeed -> 1/1 = 1 (1s sleep); 1/0.5 = 2 (2s sleep); 1/2 = 0.5 (0.5s sleep) - higher value == higher attack speed == shorter sleep
        print("Both deal and take damage at the same time")
        print(f"Equal: {attackspeedplayer}")

while True:
    #asyncio.run(run_test_threads())
    run_turns()


