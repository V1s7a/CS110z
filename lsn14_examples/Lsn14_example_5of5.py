""" lsn14_examples_5of5.py - example code from lesson 14 """
__author__ = "CS110Z"
import random

rolls = []
# Ask the user for a number of dice rolls (2 six sided dice)
num_rolls = int(input('How many rolls: '))

# Store num_rolls rolls of the two dice in a list
for i in range(num_rolls):
    rolls.append(random.randint(1, 6) + random.randint(1,6))
            
# We want to track the occurances of each dice roll result
# We should see results close to the computed probabilities
# 2 or 12 = 2.78%, 3 or  11 = 5.56%, 4 or 10 = 8.33%
# 5 or 9 = 11.11%, 6 or 8 = 13.89%, 7 = 16.67%

# Start by delaring a list ot hold the results and initialize
# each element to 0
stats = []
for i in range(11):
    stats.append(0)

# Determine how many of each of each result there is    
for i in range(num_rolls):
    if rolls[i] == 2:
        stats[0] += 1
    elif rolls[i] == 3:
        stats[1] += 1
    elif rolls[i] == 4:
        stats[2] += 1
    elif rolls[i] == 5:
        stats[3] += 1
    elif rolls[i] == 6:
        stats[4] += 1
    elif rolls[i] == 7:
        stats[5] += 1
    elif rolls[i] == 8:
        stats[6] += 1
    elif rolls[i] == 9:
        stats[7] += 1
    elif rolls[i] == 10:
        stats[8] += 1
    elif rolls[i] == 11:
        stats[9] += 1
    else:
        stats[10] += 1
        
# Print the results (should be close to computed given
# enough rolls)
for i in range(len(stats)):
    print('%d = %0.2f%%' % (i, (stats[i] / num_rolls) * 100))

