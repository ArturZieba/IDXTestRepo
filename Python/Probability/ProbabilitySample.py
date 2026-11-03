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

def printinfo(percentage, successfultries, successfulprobability, tries):
    successfultries.append(tries)
    successfulprobability.append(probability(percentage, tries))
    print(f"\n{ percentage * 100 }% info:")
    print(f"   Successful tries: { len(successfultries) }")
    print(f"   Successful try numbers: {successfultries}")
    print(f"   Probability for successful try at least once up to the successful try: {successfulprobability}")

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

print("Stats for 2000 rolls of x% probability:")

# Print total amount and try numbers of all hit probabilities in one message instead of each being separate
print("\n0.2% info:")
print(f"   Successful tries: { len(successfultries02) }")
print(f"   Successful try numbers: {successfultries02}")
print(f"   Probability for successful try at least once up to the successful try: {successfulprobability02}")

print("\n0.1% info:")
print(f"   Successful tries: { len(successfultries01) }")
print(f"   Successful try numbers: {successfultries01}")
print(f"   Probability for successful try at least once up to the successful try: {successfulprobability01}")

# Add lowest and highest probability as separate notes
# Move prints for % into separate def
# Add more rolls