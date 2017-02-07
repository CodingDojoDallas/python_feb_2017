def oddeven(a,b):
    for count in range(a,b):
        if count%2 == 0:
            print "Number is " + str(count )+ "." + "This is an even number."
        elif count%2 == 1:
            print "Number is " + str(count) + "." + "This is an odd number."
    return count

oddeven(1,2001)
