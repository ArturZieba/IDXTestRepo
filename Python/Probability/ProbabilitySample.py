import random

a = [0, 1]
tries = 0

while True:
    tries += 1
    print(f"Try number: {tries}")
    print(random.choices(a, weights=(499,1)))