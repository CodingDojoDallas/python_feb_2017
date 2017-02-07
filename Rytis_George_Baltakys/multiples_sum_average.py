'''
Assignment: Multiples, Sum, Average

Multiples:
Part I
Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use an array to do this exercise.
'''
for x in range(1,1000,2):
	print x

'''
Part II
Create another program that prints all the multiples of 5 from 5 to 1,000,000.
'''
for x in range(5,5000,5):
	print x

'''
Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
a = [1, 2, 5, 10, 255, 3]
sum = 0
for value in a:
	sum += value
print sum

'''
Assignment: Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
print sum / len(a)
