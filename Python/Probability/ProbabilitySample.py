import math # For math.pow()
import random # For random.choices()

a = [0, 1] # List used for weighted probability
tries = 0 # Number of tries

successfultries02 = []
successfulprobability02 = []
successfultries01 = []
successfulprobability01 = []

# 1 - (1 - Probability)^Tries -> formula for calculating an occurence of specific probability happened at least once over the number of tries; Rounded to 4 decimal places for clarity
def probability(chanceofoccurence, tries):
    return round(1 - math.pow((1 - chanceofoccurence), tries), 4)

# Print info about specific percentage chance rolls, their successful rols, how probable it is for it to happen at least once, and other information related to it
def printinfo(percentage, successfultries, successfulprobability, tries):
    # No successful rolls print
    if len(successfultries) == 0:
        print(f"\n{ percentage * 100 }% info:")
        print("No tries")

    # One successful roll print
    elif len(successfultries) == 1:
        print(f"\n{ percentage * 100 }% info:")
        print("1 try")

    # More than one successful rolls print
    elif len(successfultries) > 1:
        successfultries.append(tries)
        successfulprobability.append(probability(percentage, tries))
        print(f"\n{ percentage * 100 }% info:")
        print(f"   Successful tries: { len(successfultries) }")
        print(f"   Successful try numbers: {successfultries}")
        print(f"   Probability for successful try at least once up to the successful try: {successfulprobability}")
        print(f"   Lowest probability: {min(successfulprobability)}")
        print(f"   Highest probability: {max(successfulprobability)}")

# Limit loops to fit in idx Terminal print limit
while tries < 2000:
    tries += 1

    # 1 + 499 = 500 weight -> 1/500 -> 0.2% chance
    if random.choices(a, weights=(499,1)) == [1]:
        successfultries02.append(tries)
        successfulprobability02.append(probability(0.002, tries))

    # 1 + 999 = 1000 weight -> 1/1000 -> 0.1% chance
    if random.choices(a, weights=(999,1)) == [1]:
        successfultries01.append(tries)
        successfulprobability01.append(probability(0.001, tries))

# Different percentage rolls
print("Stats for 2000 rolls of x% probability:")

printinfo(0.002, successfultries02, successfulprobability02, tries) # 0.2%
printinfo(0.001, successfultries01, successfulprobability01, tries) # 0.1%

# Update no roll and 1 roll cases
# Add more rolls