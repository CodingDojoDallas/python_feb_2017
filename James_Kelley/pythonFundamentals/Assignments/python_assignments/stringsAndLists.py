'''print the position for all instances of the word "monkey".
 Then create a new string where the word "monkey" is replaced 
 with the word "alligator".'''

str = "If monkeys like bananas, then I must be a monkey!"
print str.find('monkey')
print str.replace('monkey', 'alligator')

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

my_list = [2,54,-2,7,12,98]
print min(my_list)
print max(my_list)


#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
#Now create a new list containing only the first and last values in the original list.

x = ["hello",2,54,-2,7,12,98,"world"]
print x[:1]
print x[7:]

x = ["hello",2,54,-2,7,12,98,"world"]
x.remove(2)
x.remove(54)
x.remove(-2)
x.remove(7)
x.remove(12)
x.remove(98)
print x


#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
#Sort it, then slice out all of the values that are negative, placing those values in a new list. 
#Then add your new list into the original one at position 0. 
#The output should be: [[-3, -2], 2, 6, 7, 10, 12, 19, 32, 54, 98]. This one is tough!


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
newList = []
for i in x[:]:
	if i < 0:
		newList.append(i)
		x.remove(i)
x.insert(0,newList)
print x





