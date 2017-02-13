# #this is the first part of the assignment
count = 1
while count < 1001:
    print count
    count += 1
# #this is the second part
count2 = 1
while count2 < 1000000:
    if count2 % 5 == 0 :
        print count2
        count2 += 1
    else :
        count2 += 1
# #this is the third part of the assignment

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a[:]:
    sum = sum + i
print sum

## this the fourth part of the assignment

b = [1, 2, 5, 10, 255, 3]
sum1 = 0
avg = 0
for i in b[:]:
    sum1 = sum1 + i
    avg = sum1/len(b)
print avg
