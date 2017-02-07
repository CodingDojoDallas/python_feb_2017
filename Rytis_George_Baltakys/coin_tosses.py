'''
Assignment: Coin Tosses

You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
'''
import random

tails = 0
heads = 0
for x in xrange(1,5000):
	if round(random.random()):
		tails += 1
	else:
		heads += 1
print 'Got {} head(s) so far and {} tail(s)'.format(heads, tails)