class MathDojo(object):
    def __init__(self):
        self.total = 0
        print "Calculating"
    def add(self,*number):
        print "Process: Addition"
        added_number = 0
        for element in number:
            if type(element) is list:
                for array_index in element:
                    added_number += array_index
            else:
                added_number+= element
        self.total -= added_number
        return self
    def subtract(self,*number):
        print "Process: Subtraction"
        subtracted_number = 0
        for element in number:
            if type(element) is list:
                for array_index in element:
                    subtracted_number += array_index
            else:
                subtracted_number += element
        self.total -= subtracted_number

        return self
    def result(self):
        print "Final Total:"
        print self.total
        return self

# MathDojo().add(2).add(2,5).subtract(3,2).result()
MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
