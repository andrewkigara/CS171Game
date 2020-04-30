import project
import flag
import endgame
from time import sleep

# Looping element to print the questions that were asked
def medium_questions_print():
    project.clear()
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for q in questions:
        print(q1)
        sleep(5)

q1 = """
Which is the most populated country in Africa?
(a) South Africa
(b) Algeria
(c) Nigeria
"""

q2 = """
Which was the first country in Africa to gain independence?
(a) Ghana
(b) South Africa
(c) Nigeria
"""

q3 = """
Where is the Cradle of Humankind located?
(a) South Africa
(b) Ethiopia
(c) Kenya
"""

q4 = """
Which country in the list is not land locked?
(a) Central African Republic
(b) Democratic Republic of the Congo
(c) South Sudan
"""

q5 = """
Which is the lowest point in Africa?
(a) Danakil Depression
(b) Lake Assal
(c) Afar Depression
"""

q6 = """
Which is not a desert in Sub-Saharan Africa?
(a) Namib desert
(b) Chalbi desert
(c) Libyan desert
"""

q7 = """
Which is the biggest lake in Africa?
(a) Lake Tanganyika
(b) Lake Victoria
(c) Lake Malawi
"""

q8 = """
Which is the oceanic water body on the Western part of Africa?
(a) Red Sea
(b) Atlantic Ocean
(c) Pacific Ocean
"""

q9 = """
Which is the oceanic water body on the Eastern part of Africa?
(a) Atlantic Ocean
(b) Indian Ocean
(c) Mediterranean Sea
"""

q10 = """
Which is the largest waterfall in Africa?
(a) Fouteen Falls
(b) Lumangwe Falls
(c) Victoria Falls
"""

#The function starts the medium level questions trivia
def mediumquestions():
    #This function starts off the medium level.

    # The conditional if statements after each answer input request send either
    # a 0 for wrong answers or a 1 for correct answers to the tally function
    # that counts the correct answers.
    def mquestion1():
        print(q1)
        ans1 = str(input())
        if ans1 == "a":
            flag.tally(0)
        elif ans1 == "b":
            flag.tally(0)
        elif ans1 == "c":
            flag.tally(1)
        else:
            mquestion1()

    def mquestion2():
        print(q2)
        ans2 = str(input())
        if ans2 == "a":
            flag.tally(0)
        elif ans2 == "b":
            flag.tally(1)
        elif ans2 == "c":
            flag.tally(0)
        else:
            mquestion2()

    def mquestion3():
        print(q3)
        ans3 = str(input())
        if ans3 == "a":
            flag.tally(1)
        elif ans3 == "b":
            flag.tally(0)
        elif ans3 == "c":
            flag.tally(0)
        else:
            mquestion3()

    def mquestion4():
        print(q4)
        ans4 = str(input())
        if ans4 == "a":
            flag.tally(0)
        elif ans4 == "b":
            flag.tally(1)
        elif ans4 == "c":
            flag.tally(0)
        else:
            mquestion4()

    def mquestion5():
        print(q5)
        ans5 = str(input())
        if ans5 == "a":
            flag.tally(0)
        elif ans5 == "b":
            flag.tally(0)
        elif ans5 == "c":
            flag.tally(1)
        else:
            mquestion5()

    def mquestion6():
        print(q6)
        ans6 = str(input())
        if ans6 == "a":
            flag.tally(0)
        elif ans6 == "b":
            flag.tally(0)
        elif ans6 == "c":
            flag.tally(1)
        else:
            mquestion6()

    def mquestion7():
        print(q7)
        ans7 = str(input())
        if ans7 == "a":
            flag.tally(0)
        elif ans7 == "b":
            flag.tally(1)
        elif ans7 == "c":
            flag.tally(0)
        else:
            mquestion7()

    def mquestion8():
        print(q8)
        ans8 = str(input())
        if ans8 == "a":
            flag.tally(0)
        elif ans8 == "b":
            flag.tally(1)
        elif ans8 == "c":
            flag.tally(0)
        else:
            mquestion8()

    def mquestion9():
        print(q9)
        ans9 = str(input())
        if ans9 == "a":
            flag.tally(0)
        elif ans9 == "b":
            flag.tally(1)
        elif ans9 == "c":
            flag.tally(0)
        else:
            mquestion9()

    def mquestion10():
        print(q10)
        ans10 = str(input())
        if ans10 == "a":
            flag.tally(0)
        elif ans10 == "b":
            flag.tally(0)
        elif ans10 == "c":
            flag.tally(1)
        else:
            mquestion10()

        # This is essentially part of the Question 10 function so that it can
        # use the score value that is produced after the last question
        if (flag.score == 5) or (flag.score > 5):
            print("Congratulations!\n\nYour final score is", flag.score, "\nYou win!")
        else:
            print("Oof!\n\nYour final score is ", flag.score, "\nYou lose!")

    # Because I wanted each of the questions to be manipulated individually,
    # I separated them into smaller functions.
    # Here, I call them individually.
    mquestion1()
    mquestion2()
    mquestion3()
    mquestion4()
    mquestion5()
    mquestion6()
    mquestion7()
    mquestion8()
    mquestion9()
    mquestion10()
    endgame.end_medium_game() # calls the end of medium game function

if __name__ == '__main__':
    # for testing
    medium_questions_print()
