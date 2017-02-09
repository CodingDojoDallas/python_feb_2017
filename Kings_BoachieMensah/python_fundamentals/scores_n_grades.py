# #Answer Key Way
from random import randint

print "Scores and Grades"
for count in range(0, 10):
	score = randint(70, 100)

	if(score <= 70):
		grade = "D"
	elif(score <= 80):
		grade = "C"
	elif(score <= 90):
		grade = "B"
	else:
		grade = "A"

	print "Score: %d; Your grade is %s" %(score, grade)

print "End of program. Bye!"


'''I don't know how I got this code..
I don't think I actually wrote this..
Hmmm... It doesn't even work properly'''
# def scores_and_grades():
#
#     for i in range(0,11):
#         data = raw_input('What is your score?')
#         try:
#             score = int(data)
#         except ValueError:
#             print 'Please insert a valid integer'
#         else:
#             if 60 <= score <= 69:
#                 print 'Score:' , score , '; Your grade is D'
#
#             elif 70 <= score <= 79:
#                 print 'Score:' , score , '; Your grade is C'
#
#             elif 80 <= score <= 89:
#                 print 'Score:' , score , '; Your grade is B'
#
#             elif 90 <= score <= 100:
#                 print 'Score:' , score , '; Your grade is A'
#
#     print 'End of the program.Bye!'
#
# scores_and_grades()
