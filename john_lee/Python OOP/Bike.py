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
    def ride(self):
        print "Riding the Bike!"
        self.miles += 10
    def reverse(self):
        print "Reversing!"
        self.miles -= 5

biker1 = Bike('biking',200,"20 mph",0)
biker2 = Bike('biking',200,"20 mph",0)
biker3 = Bike('biking',200,"20 mph",0)

def instance1():
    biker1.ride()
    biker1.ride()
    biker1.ride()
    biker1.reverse()
    biker1.displayInfo()

def instance2():
    biker2.ride()
    biker2.ride()
    biker2.reverse()
    biker2.reverse()
    biker2.displayInfo()

def instance3():
    biker3.reverse()
    biker3.reverse()
    biker3.reverse()
    if biker3.miles > 0:
        biker3.displayInfo()
    else:
        print "Traveled too far back"

instance1()
instance2()
instance3()
