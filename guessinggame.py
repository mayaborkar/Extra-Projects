import random


# function for saying if too high or too low
def easy_medium_hard(x):
    random_number = random.randint(1, x)
    your_number = None
    # print("input value " + str(x))
    # print("random number " + str(random_number))
    while your_number != random_number:
        your_number = input("Enter a number between 1 and " + str(x) + ": ")
        if random_number < your_number:
            print("The number you entered is too high.")
        elif random_number > your_number:
            print("The number you entered is too low.")
        elif random_number == your_number:
            print("Congratulations you got it!")


# asking what level of difficulty
def play_game():
    difficulty_level = input("Pick difficulty level, choose 1 for Easy, 2 for Medium or 3 for Hard: ")
    if difficulty_level == 1:
        easy_medium_hard(10)
    elif difficulty_level == 2:
        easy_medium_hard(20)
    elif difficulty_level == 3:
        easy_medium_hard(100)


# main
play = "Y"
# playing again function
while play == 'Y':
    play_game()
    play = raw_input("Would you like to play again Y/N: ")
# Done with playing
print("Thank you for playing!")
