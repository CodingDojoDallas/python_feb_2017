x = [19,2,54,-2,17,98,32,10,-3,6]
y = []
for index in x:
    if index < 0:
        y.append(index)
        x.remove(index)
    else:
        continue
x.insert(0,y)
print x
