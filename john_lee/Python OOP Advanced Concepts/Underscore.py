class Underscore(object):
    def map(self,list,function):
        newlist = []
        for element in list:
            if type(element) is list:
                for array_index in element:
                    newlist.append(function(array_index))
            else:
                newlist.append(function(element))
        print newlist

    def reduce(self,list,context):
        newlist = []
        for element in list:
            newlist.append(element)
        print newlist * context

    def find(self,list,function):
        find = 0
        for element in list:
            if function(element):
                find = element
                break
        print find

    def filter(self,list,function):
        filtered = []
        for element in list:
            if function(element):
                filtered.append(element)
        print filtered

    def reject(self,list,function):
        reject = []
        for element in list:
            if function(element):
                reject.append(element)
        print reject

Underscore().map([1,2,3], lambda x: x * 3 )
Underscore().reduce([1,2,3], 2)
Underscore().find([1,3,4,5,6],lambda x: x % 2 == 0)
Underscore().filter([2,3,4,5,6,7,8],lambda x: x % 2 == 0)
Underscore().reject([2,3,4,5,6,7,8],lambda x: x % 2 != 0)
