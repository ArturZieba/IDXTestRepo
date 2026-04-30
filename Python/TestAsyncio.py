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

while True:
    asyncio.run(run_test_threads())
