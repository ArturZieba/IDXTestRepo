import random

a = [0, 1]
tries = 0

while tries < 2000:
    tries += 1

    # 1 + 499 = 500 weight -> 1/500 -> 0.2% chance
    if random.choices(a, weights=(499,1)) == [1]:
        print(f"Try number: {tries}")