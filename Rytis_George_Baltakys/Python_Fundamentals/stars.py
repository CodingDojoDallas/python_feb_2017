'''
Assignment: Stars

Part I:
Create a function called draw_stars() that takes a list of numbers and prints out *.
'''
def stars(x):
	for item in x:
		stars = ''
		for i in range(0,item):
			stars += '*'
		print stars

x = [4, 6, 1, 3, 5, 7, 25]
stars(x)

'''
Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
'''
def starsx(x):
	for item in x:
		stars = ''
		if type(item) is str:
			f = item[0].lower()
			letters = ''
			for i in range(0,len(item)):
				letters += f
			print letters
		else:
			for i in range(0,item):
				stars += '*'
			print stars

xx = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
starsx(xx)

