def odd_even():
	for x in xrange(1,12):
		oddeven = ''
		if x % 2 == 0:
			oddeven = 'even'
		else:
			oddeven = 'odd'
		print 'Number is {}. This is an {} number.'.format(x, oddeven)

odd_even()

def multiply(a, multiplier):
	m = []
	for x in a:
		m.append(x * multiplier)
	return m

a = [2,4,10,16]

b = multiply(a, 5)
print b
