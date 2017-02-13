def printName(x):

    for i in range(len(x)):
        name = x[i]['first_name']+" "+x[i]['last_name']
        print name

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
printName(students)
