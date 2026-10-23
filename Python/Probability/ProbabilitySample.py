import math # For math.pow()
import random

a = [0, 1]
tries = 0

while tries < 2000:
    tries += 1

    # 1 + 499 = 500 weight -> 1/500 -> 0.2% chance
    if random.choices(a, weights=(499,1)) == [1]:
        probability = 1 - math.pow((1 - 0.002), tries)
        print(f"Try number: {tries}")
        print(f"Probability of hitting 0.2% at least once up to current try: {probability}")