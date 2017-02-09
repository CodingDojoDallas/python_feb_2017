import random
def cointoss():
    heads = 0
    tails = 0
    result = ''
    for num in range(5001):
        flip = random.randint(0,1)
        if(flip == 0):
            result = "head"
            heads = heads + 1
        elif(flip == 1):
            result = "tail"
            tails = tails + 1
        print "Attempt #" + str(num) + ": Throwing a coin..." + "It's a " + str(result) +"!...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

cointoss()
