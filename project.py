# Andrew M Kigara
# ID : 14381581
# Email : amk526@drexel.edu
# CS 171 Game Project

# Name of the Game is :  AFRICA AT 60!

# This is the main program that initiates the game
# I have 5 more programs that support the running of the program

# Comments have been incorporated on random positions of the program
# to enhance the understandability of the program.

#Responces of the program are either "1", "2", "3", "y" or "n"

from os import system, name # for the clear screen function
import time # for the sleep command
from time import sleep # for the sleep command
import easylevel # the easy game is in this module
import mediumlevel # the medium game is in this module
import hardlevel # the hard game is in this module
import endgame # the end of the game commands are housed in this module
import flag # not required in this module, but it just highlights it's presence

# This is a function that clears the terminal window before the game starts
# The function calls the appropriate terminal commands to clear the terminal window
# depending on the operating system of the computer.
# The source is https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    print("Welcome to the game!")
    sleep(1)
    global player_name
    player_name = str(input("Please enter your name: "))
    if player_name == "":
        main()
    else:
        print("Hallo " + player_name + ". Welcome to Africa at 60!\n")
        print(flag.africa)
    tally = 0
    start()

#This function prompts the player to select the level that they wish to play
def start():
    level = str(input("Enter your level: (1, 2 or 3)")) #3 levels
    if level == "1":
        print("Great choice " + player_name + ". You selected Easy!\n")
        easy_level()
    elif level == "2":
        print("Great choice " + player_name + ". You selected Medium!\n")
        medium_level()
    elif level == "3":
        print("Great choice " + player_name + ". You selected Hard!\n")
        hard_level()
    else:
        start()

# The easy level is initiated in this function
def easy_level():
    sleep(1)
    print("The following questions are general facts about Africa.")
    sleep(2)
    print("For a fun gaming experience, please refrain from googling.\n")
    sleep(2)
    print("Now to the fun stuff...\n")
    sleep(3)
    easylevel.easyquestions()

# The medium level is initiated in this function
def medium_level():
    sleep(1)
    print("The following questions are based off facts about African geography and history.")
    sleep(2)
    print("For a fun gaming experience, please refrain from googling.\n")
    sleep(2)
    print("Let the games begin...")
    sleep(3)
    mediumlevel.mediumquestions()

# The hard level is initiated in this function
def hard_level():
    sleep(1)
    print("The following questions are more in depth facts about Africa.")
    sleep(2)
    print("For a fun gaming experience, please refrain from googling.\n")
    sleep(2)
    print("Alright tough guy, let the games begin...")
    sleep(3)
    hardlevel.hardquestions()

# Here, the game is initiated
if __name__ == '__main__':
    clear()
    main()
