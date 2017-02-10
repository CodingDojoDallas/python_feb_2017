def coinTosser(attempts):
    heads = 0
    tails = 0
    import random
    count = 0
    while count < attempts:
        toss = random.random()*100
        toss = round(toss)
        string = "Attempt #"+str(count)+"Throwing coin..."
        if toss < 50:
            heads += 1
            string += "head! ... Got "+str(heads)+"head(s) so far and "+str(tails)+" tail(s) so far"
            print string
        else :
            tails += 1
            string += "tail! ... Got "+str(tails)+"tail(s) so far and "+str(heads)+" head(s) so far"
            print string
        count +=1


coinTosser(20)
