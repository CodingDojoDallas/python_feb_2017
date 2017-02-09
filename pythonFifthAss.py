def whatIsMyGrade(score):
    if ((score <= 100) and (score > 89)):
        print "Score: " + str(score) + "; Your grade is A"
    elif ((score < 90) and (score > 79)):
        print "Score: " + str(score) + "; Your grade is B"
    elif ((score < 80) and (score > 69)):
        print "Score: " + str(score) + "; Your grade is C"
    elif ((score < 70) and (score > 59)):
        print "Score: " + str(score) + "; Your grade is D"
    else :
        print "Study more"

# import random
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))
# whatIsMyGrade((random.random()*100))

def tenRandomScores():
    import random
    count = 1
    while count < 11:
        print whatIsMyGrade((random.random()*100))
        count += 1

tenRandomScores()
