class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:			
			self.tax = '0.15'
		else:	
			self.tax = '0.12'
	def displayAll(self):
		print 'Price is: $' + str(self.price)
		print 'Speed is: ' + str(self.speed) + ' mph'
		print 'Fuel Economy is: ' + str(self.fuel) + ' mpg'
		print 'Mileage is: ' + str(self.mileage) + ' miles'
		print 'Tax: ' + str(self.tax)

car1 = Car(10000, 100, 20, 1000)
car2 = Car(20000, 120, 40, 2000)
car3 = Car(15000, 140, 23, 5000)
car4 = Car(6000, 110, 45, 3000)
car5 = Car(12000, 100, 36, 7000)
car6 = Car(8000, 125, 34, 9000)

print 'Car 1 INFO:'
car1.displayAll()
print 'Car 2 INFO:'
car2.displayAll()
print 'Car 3 INFO:'
car3.displayAll()
print 'Car 4 INFO:'
car4.displayAll()
print 'Car 5 INFO:'
car5.displayAll()
print 'Car 6 INFO:'
car6.displayAll()

