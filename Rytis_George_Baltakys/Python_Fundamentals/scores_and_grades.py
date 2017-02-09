'''
Assignment: Scores and Grades

Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score.
'''

import random

def grade(score):
	if score > 89:
		return 'A'
	elif score > 79:
		return 'B'
	elif score > 69:
		return 'C'
	else:
		return 'D'

for x in xrange(1,10):
	score = int(random.random() * 40 + 61)
	print 'Score is {}. Your grade is {}'.format(score, grade(score))