'''I had to look at the answer key to answer
this one so I gotta go back later sometime and take a
look at this one. Alrighty.'''

import random
import math

print "Starting the program..."

heads_count = 0
tails_count = 0

for i in range(1,5001):
    rand = round(random.random())
    if rand == 0:
        face = "tails"
        tails_count += 1
    else:
        face = "heads"
        heads_count += 1
    print "Attempt #" + str(i) + ": Throwing a coin... It's " + face + "!... Got " + str(heads_count) + " head(s) and " + str(tails_count) + " tail(s) so far"

print "Ending the program, thank you!"
