def coinTosser(attempts):
    heads = 0
    tails = 0
    count = 1
    import random
    while count <= attempts:
        toss = round((random.random()*100)+1)
        string = "Attempt #"+str(count)+"Throwing coin..."
        if
