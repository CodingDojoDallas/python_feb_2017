# Find and Replace
str = "If monkeys like bananas, then I must be a monkey!"
start = 0
output = []
while True:
    index = str.find('monkey', start, len(str))
    if index == -1:
        break
    else:
        output.append(index)
        start = index + 1
print output
# # print str.find('monkey', 0, len(str))
# # print str.find("monkey", 10, len(str))
print str.replace("monkey", "alligator")

#Min and Max
x = [2,-54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
y = ["hello",2,54,-2,7,12,98,"world"]
first = y[0]
new_list = []
# last = y[len(y) - 1]
last = y[-1]
new_list.append(first)
new_list.append(last)
print new_list

#New List
arr = [19,2,54,-2,7,12,98,32,10,-3,6]
arr.sort()
# for value in arr:
#     #where i represents the value
#     print value
for i in range(0, len(arr)):
    #where i represents the index
    if arr[i] > -1:
        break
positive_nums = arr[i:]
positive_nums.insert(0, arr[0:i])
print positive_nums
