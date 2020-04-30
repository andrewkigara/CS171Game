import project
import flag
import endgame
from time import sleep

# Looping element to print the questions that were asked
def easy_questions_print():
    project.clear()
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for q in questions:
        print(q1)
        sleep(5)

q1 = """
How many countries are there in Africa?
(a) 54
(b) 55
(c) 56
"""

q2 = """
Which was the last African country to gain independence?
(a) Kenya
(b) South Sudan
(c) Nigeria
"""

q3 = """
Which of the three is not part of the big five wild animals that Africa is popular for?
(a) Elephant
(b) Python
(c) Cheetah
"""

q4 = """
Which is not an island country in Africa?
(a) Mauritius
(b) Madagascar
(c) Eswatini
"""

q5 = """
Which is the most Easterly country in mainland Africa?
(a) Somalia
(b) Cote D’Ivore
(c) Tunisia
"""

q6 = """
Which is the most Westerly country in mainland Africa?
(a) Western Sahara
(b) Equatorial Guinea
(c) Senegal
"""

q7 = """
Which is the largest country in Africa?
(a) Democratic Republic of the Congo
(b) Sudan
(c) Algeria
"""

q8 = """
Which is the smallest country in Africa?
(a) Mauritius
(b) Rwanda
(c) Seychelles
"""

q9 = """
Which is the highest mountain in Africa?
(a) Mount Kilimanjaro
(b) Table Mountains
(c) Atlas mountains
"""

q10 = """
Which is the longest river in Africa?
(a) River Nile
(b) Delta river
(c) Niger river
"""


def easyquestions():
    #This function starts off the easy level.

    # The conditional if statements after each answer input request send either
    # a 0 for wrong answers or a 1 for correct answers to the tally function
    # that counts the correct answers.

    #Question 1
    def equestion1():
        print(q1)
        ans1 = str(input())
        if ans1 == "a":
            flag.tally(0) # wrong answer
        elif ans1 == "b":
            flag.tally(1) #correct answer
        elif ans1 == "c":
            flag.tally(0)
        else:
            equestion1()

    #Question 2
    def equestion2():
        print(q2)
        ans2 = str(input())
        if ans2 == "a":
            flag.tally(0)
        elif ans2 == "b":
            flag.tally(1)
        elif ans2 == "c":
            flag.tally(0)
        else:
            equestion2()

    #Question 3
    def equestion3():
        print(q3)
        ans3 = str(input())
        if ans3 == "a":
            flag.tally(0)
        elif ans3 == "b":
            flag.tally(1)
        elif ans3 == "c":
            flag.tally(0)
        else:
            equestion3()

    #Question 4
    def equestion4():
        print(q4)
        ans4 = str(input())
        if ans4 == "a":
            flag.tally(0)
        elif ans4 == "b":
            flag.tally(0)
        elif ans4 == "c":
            flag.tally(1)
        else:
            equestion4()

    #Question 5
    def equestion5():

        print(q5)
        ans5 = str(input())
        if ans5 == "a":
            flag.tally(1)
        elif ans5 == "b":
            flag.tally(0)
        elif ans5 == "c":
            flag.tally(0)
        else:
            equestion5()

    #Question 6
    def equestion6():
        print(q6)
        ans6 = str(input())
        if ans6 == "a":
            flag.tally(0)
        elif ans6 == "b":
            flag.tally(0)
        elif ans6 == "c":
            flag.tally(1)
        else:
            equestion6()

    #Question 7
    def equestion7():
        print(q7)
        ans7 = str(input())
        if ans7 == "a":
            flag.tally(0)
        elif ans7 == "b":
            flag.tally(0)
        elif ans7 == "c":
            flag.tally(1)
        else:
            equestion7()

    #Question 8
    def equestion8():
        print(q8)
        ans8 = str(input())
        if ans8 == "a":
            flag.tally(0)
        elif ans8 == "b":
            flag.tally(0)
        elif ans8 == "c":
            flag.tally(1)
        else:
            equestion8()

    #Question 9
    def equestion9():
        print(q9)
        ans9 = str(input())
        if ans9 == "a":
            flag.tally(1)
        elif ans9 == "b":
            flag.tally(0)
        elif ans9 == "c":
            flag.tally(0)
        else:
            equestion9()

    #Question 10
    def equestion10():
        print(q10)
        ans10 = str(input())
        if ans10 == "a":
            flag.tally(1)
        elif ans10 == "b":
            flag.tally(0)
        elif ans10 == "c":
            flag.tally(0)
        else:
            equestion10()

        # This is essentially part of the Question 10 function so that it can
        # use the score value that is produced after the last question
        if (flag.score == 5) or (flag.score > 5):
            print("Congratulations!\n\nYour final score is", flag.score, "\nYou win!")
        else:
            print("Oof!\n\nYour final score is ", flag.score, "\nYou lose!")

    # Because I wanted each of the questions to be manipulated individually,
    # I separated them into smaller functions.
    # Here, I call them individually.
    equestion1()
    equestion2()
    equestion3()
    equestion4()
    equestion5()
    equestion6()
    equestion7()
    equestion8()
    equestion9()
    equestion10()
    endgame.end_easy_game()
