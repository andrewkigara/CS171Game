#The main purpose of this file is to store the ascii art in form of variables
# It also serves as a host for the counter/tally function
# The source of the lion is this website https://ascii.co.uk/art/lions
# The counter/tally is on the bottom of the program


#testing the flags
#print(africa)
#print(kenya)

score = 0
# The tally function
# Adds one to the score for correct answers
# Adds zero to the score for a wrong answer
# Prints out whether the score is correct of wrong
def tally(x):
    global score
    score += x
    if x == 0:
        print("Wrong answer!")
    else:
        print("Correct answer!")
    print("Your score is:", str(score))



lion = """

                       \|\||
                      -' ||||/
                     /7   |||||/
         |\_        /    |||||||/`-.____________
       -' | \       \-' |||||||||               `-._
      /7     \       -|||||||||||               `` -`.
     /        `-_      ||||||               \   |   `\\
     \-'_        `-.____|||||\  \______...---\_  \    \\
      -- \                 |  \  \           | \  |    ``-.__--.
         /                 |  |\  \         / / | |       ``---'
 _______/    /_       ____/  /_/  /|_______/ /-_| |
(,__________/  `-.___(,_(,__/(,__/_-----(,__/-(,__/


"""


# The maasai ASCII Art was sourced from https://asciiart.website/index.php?art=people/tribal%20people
maasai = """
         www
        /n n\\        /\\
        |/^\\|       /  \\
        | , |       ^||^
         \_/         ||
         _U_         ||
       /`   `''-----'P3
      / |. .|''-----"||
      \\'|   |        ||
       \\|   |        ||
        E   |        ||
       /#####\\       ||
       /#####\\       ||
         |||         ||
         |||         ||
         |||         ||
         |||         ||
        molom        Ll

"""




conti = """
         .    _.----~~~~~~~7
             /              ~-..-~~--..--.
       .'.'.'                             `.
         .~                                 \\
       .'                                    `.
   .   (                                       \\
 '.    )                                        `.
   '  (                                           ~-.
       \                                             ~-~~7
        `.       __.._                                  .'
          ~-.--~~     ~--.                             /
                         ;                          .-~
                         (                        .~
                          `.                    .'
                            ;                   ;
                            `.                  `       _
                             )                   )     / )
                            (                 _.-'  .-' .'
                            `.               (      )   /
                              7             _;      < _/
                               \           /         ~
                                \         /
                                 `. __..-'
                                   ~
"""






kenya = """
████████████████████████████████████████████████████
████████████████████████████████████████████████████
████████████████████████████████████████████████████
████████████████  ██████▒▒██████  ██████████████████
██████████████████  ██▒▒▒▒▒▒██  ████████████████████
████████████████████▒▒  ▒▒  ▒▒██████████████████████
                  ▒▒▒▒  ▒▒  ▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒  ▒▒  ▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒  ▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒  ▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒  ▒▒  ▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                  ▒▒▒▒  ▒▒  ▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██████████  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒████▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

"""
#Kenyan flag

#ascii art for Africa found on https://ascii.co.uk/art/africa
africa = """
        __      _
       / _|    (_)
  __ _| |_ _ __ _  ___ __ _
 / _` |  _| '__| |/ __/ _` |
| (_| | | | |  | | (_| (_| |
 \__,_|_| |_|  |_|\___\__,_|
"""




if __name__ == '__main__':
    # This is non-essential for running of the game
    # It was just for testing purposes
    print(maasai)
