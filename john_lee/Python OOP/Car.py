class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        print 'Car Created.'
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def displayInfo(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax
    def tax(self):
        print "Tax"
        if self.price > 10000:
            self.tax = (self.price)*.15
        else:
            self.tax = (self.price)*.12

car1 = Car(9999,"200 mph","25 Gallons", 20000)

def instance():
    car1.tax()
    car1.displayInfo()

instance()
