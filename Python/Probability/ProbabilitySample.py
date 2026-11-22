import math # For math.pow()
import random # For random.choices()

a = [0, 1] # List used for weighted probability
tries = 0 # Number of tries

# Lists for specific % chance rolls
successfultries10 = []
successfulprobability10 = []
successfultries09 = []
successfulprobability09 = []
successfultries08 = []
successfulprobability08 = []
successfultries07 = []
successfulprobability07 = []
successfultries06 = []
successfulprobability06 = []
successfultries05 = []
successfulprobability05 = []
successfultries04 = []
successfulprobability04 = []
successfultries03 = []
successfulprobability03 = []
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
        print(f"\n{ round(percentage * 100, 1) }% info:")
        print("   No successful rolls")

    # One successful roll print
    elif len(successfultries) == 1:
        print(f"\n{ round(percentage * 100, 1) }% info:")
        print(f"   Successful roll number: {successfultries}")
        print(f"   Probability for successful roll to occur at least once up to the successful roll: {successfulprobability}")
        print(f"   Probability based on successful rolls per { rolls } rolls: { round(((1 / rolls) * 100), 4) }%")

    # More than one successful rolls print
    elif len(successfultries) > 1:
        print(f"\n{ round(percentage * 100, 1) }% info:")
        print(f"   Successful rolls: { len(successfultries) }")
        print(f"   Successful roll numbers: { successfultries }")
        print(f"   Probability for successful roll to occur at least once up to the successful roll: {successfulprobability}")
        print(f"   Lowest probability: { min(successfulprobability) }")
        print(f"   Highest probability: { max(successfulprobability) }")
        print(f"   Probability based on successful rolls per { rolls } rolls: { round(((len(successfultries) / rolls) * 100), 1) }%")

# Limit loops to fit in idx Terminal print limit
rolls = 2000

for x in range(rolls):
    tries += 1

    # 1 + 99 = 100 weight -> 1/100 -> 1% chance
    if random.choices(a, weights=(99,1)) == [1]:
        successfultries10.append(tries)
        successfulprobability10.append(probability(0.01, tries))

    # 1 + 111 = 112 weight -> 1/112 -> 0.9% chance
    if random.choices(a, weights=(111,1)) == [1]:
        successfultries09.append(tries)
        successfulprobability09.append(probability(0.009, tries))

    # 1 + 124 = 125 weight -> 1/125 -> 0.8% chance
    if random.choices(a, weights=(124,1)) == [1]:
        successfultries08.append(tries)
        successfulprobability08.append(probability(0.008, tries))

    # 1 + 142 = 143 weight -> 1/143 -> 0.7% chance
    if random.choices(a, weights=(142,1)) == [1]:
        successfultries07.append(tries)
        successfulprobability07.append(probability(0.007, tries))

    # 1 + 166 = 167 weight -> 1/167 -> 0.6% chance
    if random.choices(a, weights=(166,1)) == [1]:
        successfultries06.append(tries)
        successfulprobability06.append(probability(0.006, tries))

    # 1 + 199 = 200 weight -> 1/200 -> 0.5% chance
    if random.choices(a, weights=(199,1)) == [1]:
        successfultries05.append(tries)
        successfulprobability05.append(probability(0.005, tries))

    # 1 + 249 = 250 weight -> 1/250 -> 0.4% chance
    if random.choices(a, weights=(249,1)) == [1]:
        successfultries04.append(tries)
        successfulprobability04.append(probability(0.004, tries))

    # 1 + 333 = 334 weight -> 1/334 -> 0.3% chance
    if random.choices(a, weights=(333,1)) == [1]:
        successfultries03.append(tries)
        successfulprobability03.append(probability(0.003, tries))

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

printinfo(0.01, successfultries10, successfulprobability10, tries) # 1%
printinfo(0.009, successfultries09, successfulprobability09, tries) # 0.9%
printinfo(0.008, successfultries08, successfulprobability08, tries) # 0.8%
printinfo(0.007, successfultries07, successfulprobability07, tries) # 0.7%
printinfo(0.006, successfultries06, successfulprobability06, tries) # 0.6%
printinfo(0.005, successfultries05, successfulprobability05, tries) # 0.5%
printinfo(0.004, successfultries04, successfulprobability04, tries) # 0.4%
printinfo(0.003, successfultries03, successfulprobability03, tries) # 0.3%
printinfo(0.002, successfultries02, successfulprobability02, tries) # 0.2%
printinfo(0.001, successfultries01, successfulprobability01, tries) # 0.1%

# 0.9999 rolling into 1.0? (see 0.6%+ rolls)