
def draw_stars(x):
    for i in x:
        if(isinstance((i), basestring) == True):
            print i[0] * len(i)
        else:
            print i * '*'

x = draw_stars([4,"Tom",1,"Michael",5,7,"Jimmy Smith"])
