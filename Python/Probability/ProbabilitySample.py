import math # For math.pow()
import random # For random.choices()

a = [0, 1] # List used for weighted probability
tries = 0 # Number of tries

# Limit loops to fit in idx Terminal print limit
while tries < 2000:
    tries += 1

    # 1 + 499 = 500 weight -> 1/500 -> 0.2% chance
    if random.choices(a, weights=(499,1)) == [1]:
        probability = 1 - math.pow((1 - 0.002), tries) # 1 - (1 - Probability)^Tries -> formula for calculating an occurence of specific probability happened at least once over the amount of tries
        print(f"Try number: {tries}")
        print(f"Probability of hitting 0.2% at least once up to current try: {probability}")