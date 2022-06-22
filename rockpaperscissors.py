import random

rockpaperscissors = ["rock", "paper", "scissors"]
play = True
while play:
    choice = input("Rock, paper, scissors shoot! ")
    computerchoice = random.choice(rockpaperscissors)
    if choice == computerchoice:
        print("The computer picked: " + computerchoice)
        print("It is a tie, play again")
    elif choice == "paper" and computerchoice != "scissors":
        print("The computer picked: " + computerchoice)
        print("You won! ")
        play = False
    elif choice == "paper" and computerchoice == "scissors":
        print("The computer picked: " + computerchoice)
        print("Computer won! ")
        play = False
    elif choice == "rock" and computerchoice != "paper":
        print("The computer picked: " + computerchoice)
        print("You won! ")
        play = False
    elif choice == "rock" and computerchoice == "paper":
        print("The computer picked: " + computerchoice)
        print("Computer won! ")
        play = False
    elif choice == "scissors" and computerchoice != "rock":
        print("The computer picked: " + computerchoice)
        print("You won! ")
        play = False
    elif choice == "scissors" and computerchoice == "rock":
        print("The computer picked: " + computerchoice)
        print("Computer won! ")
        play = False
    askPlay = input("Would you like to play again? (Y/N) ")
    if askPlay == "Y":
        play = True
    else:
        play = False
