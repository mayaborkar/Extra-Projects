import random


def play_game(random_x):
    guess_count = 0
    random_number = random.randint(1, random_x)
    your_number = None
    # print("input value " + str(x))
    print("random number " + str(random_number))
    while your_number != random_number:
        your_number = input("Enter a number between 1 and " + str(random_x) + ": ")
        guess_count += 1
        if random_number < your_number:
            print("The number you entered is too high.")
        elif random_number > your_number:
            print("The number you entered is too low.")
        elif random_number == your_number:
            print("Congratulations you got it!")
    return guess_count


def play_round(random_y, guesses):
    person1_guess_count = 0
    person2_guess_count = 0
    while person1_guess_count < guesses and person2_guess_count < guesses:
        print("Person 1 Lets Play: ")
        person1_guess_count += play_game(random_y)
        print("Person 2 Lets Play: ")
        person2_guess_count += play_game(random_y)
        print(person1_guess_count, person2_guess_count)
    if person2_guess_count > person1_guess_count:
        print("Person 1 won this round with " + str(person1_guess_count) + " number of guesses ")
        return "Person1"
    elif person2_guess_count < person1_guess_count:
        print("Person 2 won this round with " + str(person2_guess_count) + " number of guesses ")
        return "Person2"
    elif person2_guess_count == person1_guess_count:
        print("Tie")
        return "Tie"


difficulty_level = input("Pick difficulty level, choose 1 for Easy, 2 for Medium or 3 for Hard: ")
if difficulty_level == 1:
    max_random = 10
    limit_guesses = 10
elif difficulty_level == 2:
    max_random = 20
    limit_guesses = 15
elif difficulty_level == 3:
    max_random = 100
    limit_guesses = 30
person1_round = 0
person2_round = 0
round_count = 0
while person1_round != 3 and person2_round != 3:
    round_count += 1
    print ('Starting round : ' + str(round_count))
    result = play_round(max_random, limit_guesses)
    if result == "Person1":
        person1_round += 1
    elif result == "Person2":
        person2_round += 1
    print(round_count)
if person2_round > person1_round:
    print("Person 1 won")
elif person2_round < person1_round:
    print("Person 2 won")
elif person2_round == person1_round:
    print("Person 1 and Person 2 Tie")
