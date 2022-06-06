import random
rockpaperscissors = ["rock", "paper", "scissors"]
play = True
while play:
    choice = input("Rock, paper, scissors shoot! ")
    computerchoice = random.choice(rockpaperscissors)
    if(choice == computerchoice):
        print("It is a tie, play again")
    elif (choice == "paper" and computerchoice == "rock"):
        print("The computer won! ")
        play = False
