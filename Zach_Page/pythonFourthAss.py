# def odd_even():
#     count = 1
#     while count < 2001 :
#         if count%2==0 :
#             count +=1
#             print "Number is "+ str(count) + ". This is an even number."
#         else :
#             print "Number is "+ str(count) + ". This is an odd number."
#             count += 1
#
# odd_even()

myArr = [1,2,3,4,5]
newArr = []
def mulitply(myArr,x):
    for i in myArr:
        new = i * x
        newArr.append(new)
    print newArr
mulitply(myArr,5)
