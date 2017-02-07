def layered(x):
    (arr, multiplier) = x
    newarr = []
    for index in arr:
        insert = []
        one = index * multiplier
        while one>0:
            insert.append(1)
            one = one - 1
        newarr.append(insert)
    print newarr
    return newarr

x = layered(([2,4,5],3))
