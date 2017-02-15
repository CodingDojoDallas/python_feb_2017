scores = []
def generator():
    for i in range(1,11):
        import random
        test = random.randint(60,100)
        scores.append(test)
    return scores

def grader():
    print "Scores and Grades"
    for index in scores:
        letter = ''
        if(index>89):
            letter = 'A'
        elif(90>index>79):
            letter = 'B'
        elif(80>index>69):
            letter = 'C'
        elif(70>index>59):
            letter = 'D'
        print "Score: " + str(index) + "; Your grade is " + str(letter)
    print "End of the program. Bye!"

generator()
print grader()
