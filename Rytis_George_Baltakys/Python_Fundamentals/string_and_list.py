str = "If monkeys like bananas, then I must be a monkey!"
print str
firstMonkey = str.find('monkey')
print firstMonkey
print str[firstMonkey+1:].find('monkey')
print str.replace('monkey', 'aligator')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0:1][0] + " " + x[-1:][0]
xx = [x[0:1][0], x[-1:][0]]
print xx

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
xx = []
for item in x[:]:
	if (item < 0):
		xx.append(item)
		x.remove(item)

x[0] = xx
print x
