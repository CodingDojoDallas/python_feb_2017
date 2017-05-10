class Bike(object):
	
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = 100
	def displayInfo(self):
		print bike1.price
		print bike1.max_speed
		print bike1.miles		
	def ride(self):
		self.miles += 10
	def reverse(self):
		self.miles -= 5
	

bike1 = Bike("$700", "30mph", "20000")
bike2 = Bike("$2200", "50mph", "10000")
bike3 = Bike("$5000", "40mph", "15000")


bike1.displayInfo()
bike2.ride()
bike3.reverse()
print 'Bike 2 Riding: {}'.format(bike2.miles)
print 'Bike 3 Reversing: {}'.format(bike3.miles)





	




