class Bike(object):
    def __init__(self,name,price,max_speed,miles):
        print 'Bike!'
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding the Bike!"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing!"
        self.miles -= 5
        return self

biker1 = Bike('biking',200,"20 mph",0)
biker2 = Bike('biking',200,"20 mph",0)
biker3 = Bike('biking',200,"20 mph",0)

biker1.ride().ride().ride().reverse().displayInfo()

biker2.ride().ride().reverse().reverse().displayInfo()

biker3.reverse().reverse().reverse().displayInfo()
