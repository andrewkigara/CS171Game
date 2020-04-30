import project
import flag
import endgame
from time import sleep

# Looping element to print the questions that were asked
def hard_questions_print():
    project.clear()
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for q in questions:
        print(q1)
        sleep(5)


q1 = """
Which is the largest trade block in Africa?
(a) The Southern African Development Community (SADC)
(b) The Common Market for Eastern and Southern Africa (COMESA)
(c) The Economic Community of West African States (ECOWAS)
"""

q2 = """
Which country is not crossed by the equator?
(a) Tanzania
(b) Gabon
(c) Republic of the Congo
"""

q3 = """
Which combination of  countries share a border point?
(a) Rwanda, Burundi, Democratic Republic of the Congo, Republic of the Congo
(b) Zambia, Zimbabwe, Botswana, Namibia
(c) Cameroon, Gabon, Republic of the Congo, Equatorial Guinea
"""

q4 = """
Which African leader is referred to as Madiba?
(a) Tom Mboya
(b) Léopold Sédar Senghor
(c) Nelson Mandela
"""

q5 = """
Which is the most prominent language in Africa?
(a) Swahili
(b) Arabic
(c) Amharic
"""

q6 = """
Which African leader served the longest time as president?
(a) Teodoro Obiang Nguema Mbasogo
(b) Paul Biya
(c) Yoweri Museveni
"""
q7 = """
Which popular African musician had the pop star, Rihanna, lip-sync to his music on her Instagram story?
(a) Diamond
(b) Burna Boy
(c) Sho Madjozi
"""
q8 = """
Which country owns this flag?
(a) Kenya
(b) Benin
(c) Chad
"""
q9 = """
Which color is not part of the Tunisian Flag?
(a) Red
(b) Green
(c) White
"""
q10 = """
Which is not an oil producing country?
(a) Libya
(b) Angola
(c) Lesotho
"""

#The function starts the hard level questions trivia
def hardquestions():

    #This function starts off the hard level.

    # The conditional if statements after each answer input request send either
    # a 0 for wrong answers or a 1 for correct answers to the tally function
    # that counts the correct answers.

    def hquestion1():
        print(q1)
        ans1 = str(input())
        if ans1 == "a":
            flag.tally(0)
        elif ans1 == "b":
            flag.tally(1)
        elif ans1 == "c":
            flag.tally(0)
        else:
            hquestion1()

    def hquestion2():
        print(q2)
        ans2 = str(input())
        if ans2 == "a":
            flag.tally(1)
        elif ans2 == "b":
            flag.tally(0)
        elif ans2 == "c":
            flag.tally(0)
        else:
            hquestion2()

    def hquestion3():
        print(q3)
        ans3 = str(input())
        if ans3 == "a":
            flag.tally(0)
        elif ans3 == "b":
            flag.tally(1)
        elif ans3 == "c":
            flag.tally(0)
        else:
            hquestion3()

    def hquestion4():
        print(q4)
        ans4 = str(input())
        if ans4 == "a":
            flag.tally(0)
        elif ans4 == "b":
            flag.tally(0)
        elif ans4 == "c":
            flag.tally(1)
        else:
            hquestion4()

    def hquestion5():
        print(q5)
        ans5 = str(input())
        if ans5 == "a":
            flag.tally(0)
        elif ans5 == "b":
            flag.tally(1)
        elif ans5 == "c":
            flag.tally(0)
        else:
            hquestion5()

    def hquestion6():
        print(q6)
        ans6 = str(input())
        if ans6 == "a":
            flag.tally(0)
        elif ans6 == "b":
            flag.tally(1)
        elif ans6 == "c":
            flag.tally(0)
        else:
            hquestion6()

    def hquestion7():
        print(q7)
        ans7 = str(input())
        if ans7 == "a":
            flag.tally(0)
        elif ans7 == "b":
            flag.tally(1)
        elif ans7 == "c":
            flag.tally(0)
        else:
            hquestion7()

    def hquestion8():
        print(q8)
        print(flag.kenya)
        ans8 = str(input())
        if ans8 == "a":
            flag.tally(1)
        elif ans8 == "b":
            flag.tally(0)
        elif ans8 == "c":
            flag.tally(0)
        else:
            hquestion8()

    def hquestion9():
        print(q9)
        ans9 = str(input())
        if ans9 == "a":
            flag.tally(0)
        elif ans9 == "b":
            flag.tally(1)
        elif ans9 == "c":
            flag.tally(0)
        else:
            hquestion9()

    def hquestion10():
        print(q10)
        ans10 = str(input())
        if ans10 == "a":
            flag.tally(0)
        elif ans10 == "b":
            flag.tally(0)
        elif ans10 == "c":
            flag.tally(1)
        else:
            hquestion10()

        if (flag.score == 5) or (flag.score > 5):
            print("Congratulations!\n\nYour final score is", flag.score, "\nYou win!")
        else:
            print("Oof!\n\nYour final score is ", flag.score, "\nYou lose!")

    hquestion1()
    hquestion2()
    hquestion3()
    hquestion4()
    hquestion5()
    hquestion6()
    hquestion7()
    hquestion8()
    hquestion9()
    hquestion10()
    endgame.end_hard_game()

if __name__ == '__main__':
    hard_questions_print()
