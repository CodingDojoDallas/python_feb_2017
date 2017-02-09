# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# def students1():
#     for j in students:
#         print j['first_name']  + ' ' + j['last_name']
# students1()

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def data(info, header):
    print header
    print '-------------'
    for i in range(len(info)):
        fullname = info[i]['first_name'] + ' ' + info[i]['last_name']
        print str(i+1) + ' - ' + fullname + ' - ' + str(len(fullname)-1)


data(users['Students'], 'Students')
data(users['Instructors'], 'Instructors')
