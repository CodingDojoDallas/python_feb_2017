class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = 100
	def displayInfo1(self):
		print bike1.price
		print bike1.max_speed
		print bike1.miles
		return self		
	def displayInfo2(self):
		print bike2.price
		print bike2.max_speed
		print bike2.miles
		return self	
	def displayInfo3(self):
		print bike3.price
		print bike3.max_speed
		print bike3.miles
		return self		
	def ride(self):
		self.miles += 10
		print 'Riding'
		return self
	def reverse(self):
		self.miles -= 5
		print 'Reversing'
		return self
	

bike1 = Bike("$700", "30mph", "20000")
bike2 = Bike("$2200", "50mph", "10000")
bike3 = Bike("$5000", "40mph", "15000")


bike1.ride().ride().ride().reverse().displayInfo1()
bike2.ride().ride().reverse().reverse().displayInfo2()
bike3.reverse().reverse().reverse().displayInfo3()






	




