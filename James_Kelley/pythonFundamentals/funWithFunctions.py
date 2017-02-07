'''
Create a function called odd_even that counts from 1 to 2000. 
As your loop executes have your program print the number of that iteration 
and specify whether it's an odd or even number.'''

# def odd_even():
	
# 	for num in range (1, 2001):
# 		if (num % 2 == 0):
# 			print "number is {} This is an even number".format(num)
# 		else:
# 			print "number is {} This is an odd number".format(num)

# print odd_even()
 				
'''Create a function called 'multiply' that iterates through each value 
in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value 
has been multiplied by 5.'''

def multiply():
	a = [2, 4, 10, 16]
	newlist = []
	product = 0

	for num in a:
		product = num * 5
		newlist.append(product)
	print newlist

multiply()






