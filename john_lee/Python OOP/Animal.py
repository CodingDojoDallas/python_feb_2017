class Animal(object):
    def __init__(self):
        print 'New Animal!'
        self.health = 0
    def walk(self):
        print "Walked"
        self.health -= 1
        return self
    def run(self):
        print "Ran"
        self.health -= 5
        return self
    def displayHealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150
    def pet(self):
        print "Pet"
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__()
        self.health = 170
    def fly(self):
        print "Flew"
        self.health -= 10
        return self
    def displayHealth(self):
        print "IT'S A DRAGON!"
        super(Dragon, self).displayHealth()
        return self

#DOG
Fido = Dog()
Fido.walk().walk().walk().run().pet().displayHealth()

#DRAGON
Draco = Dragon()
Draco.walk().walk().walk().run().run().fly().fly().displayHealth()
