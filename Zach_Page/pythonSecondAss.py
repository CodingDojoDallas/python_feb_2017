string = "If monkeys like bananas, then I must be a monkey!"
string.replace("monkey","aligator")
print string

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y =  ['hello',2,54,-2,7,12,98,'world']
print y[0]
print y[(len(y)-1)]


z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
newArr = []
for i in z[:]:
    if i < 0 :
        newArr.append(i)
        z.remove(i)
    else :
        pass

z.insert(0,newArr)
print z
