import flag
import project
from time import sleep
import easylevel
import mediumlevel
import hardlevel


# This is the function that controls the end of the easy level
def end_easy_game():
    print("\nCongratulations! You made it to the end of the game!\n")
    sleep(2)
    print("I hope you didn't google the answers ;)\n")
    sleep(1)
    print("Now, how about a small guessing game?\n")
    sleep(2)
    print("Which classical animation is based off of\nThe Big Five wild animals?")
    sleep(3)
    print("\nHere's a hint...\n")
    print(flag.lion)
    print("HAKUNA MATATA!")
    sleep(2)
    print("Would you like to see the questions asked?")
    equestion_print = str(input("y or n :"))
    if equestion_print == "y":
        easylevel.easy_questions_print()
    elif equestion_print == "n":
        print("Okay. Goodbye!")
    else:
        return


# This is a function that controls the end of the medium level
def end_medium_game():
    print("\nCongratulations! You made it to the end of the game!\n")
    sleep(2)
    print("I hope you didn't google the answers ;)\n")
    sleep(1)
    print("Please take the time to play the other levels for more African facts")
    sleep(3)
    print("Now, how about a small guessing game?\n")
    sleep(2)
    print("Guess the Wonder of the World\nLocated in the North Eastern part of Africa?\n")
    sleep(3)
    print("Here's a hint...\n")
    sleep(1)
    size = 15
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            print("* ", end=' ')
        print(" ")
    sleep(3)
    print("\nI hope you enjoyed the game :)\nGoodbye!")
    sleep(2)
    print("Would you like to see the questions asked?")
    mquestion_print = str(input("y or n :"))
    if mquestion_print == "y":
        mediumlevel.medium_questions_print()
    elif mquestion_print == "n":
        print("Okay. Goodbye!")
    else:
        return



# This is the function that controls the end of the hard level
def end_hard_game():
    print("\nCongratulations! You made it to the end of the game!\n")
    sleep(2)
    print("I hope you didn't google the answers ;)\n")
    sleep(2)
    print("For your guts and apparent knowledge ;) of Africa,\n")
    sleep(1)
    print("Here's an ASCII Art poster of the lovely continent")
    sleep(4)
    print(flag.conti)
    sleep(2)
    print("Karibu AFRICA!\n\nHAKUNA MATATA!")
    sleep(2)
    print("Oh wait...\n\nThere's more...\n\n")
    sleep(2)
    print("How about a small guessing game?\n")
    sleep(3)
    print("Which is the popular tribe in Kenya\nKnown for their tapestry and ability to jump over 10 feet high?")
    sleep(3)
    print("Here's a hint...\n")
    sleep(2)
    print(flag.maasai)
    sleep(2)
    print("Would you like to see the questions asked?")
    hquestion_print = str(input("y or n :"))
    if hquestion_print == "y":
        hardlevel.hard_questions_print()
    elif hquestion_print == "n":
        print("Okay. Goodbye!")
    else:
        return

# I used this function to determine the most appropriate height and width of the test_pyramid
# by changing the value of the size variable
'''def test_pyramid():
    size = 15
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            print("* ", end=' ')
        print(" ")'''



if __name__ == '__main__':
    # This is non-essential for running of the game
    # It was just for testing purposes

    #print(flag.lion)
    end_hard_game()
    #test_pyramid()
