import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def getHint(yourWord):
    newString = ""
    for i in range(0, len(hiddenWord)):
        letter = yourWord[i]
        for j in range(0, len(hiddenWord)):
            currentLetter = hiddenWord[j]
            print (letter)
            print (currentLetter)
            if(letter == currentLetter):
                print('is equal')
                if(i != j):
                    newString += "+"
                    # yourWord.replace(yourWord[j], "+")
                    print('is equal 1')
                else:
                    newString += "*"
                    # yourWord.replace(yourWord[j], "*")
                    print('is equal 2')
        if newString[i] != "+" and newString[i] != "+":
            newString += yourWord[i]
    print(newString)
    return newString


# making the visuals
'''
pygame.init()

wordle_screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maya's Wordle")

pygame.draw.rect(wordle_screen, BLACK, (0, 0, 600, 600))

for i in range(0, 3):
    for j in range(0, 3):
        pygame.draw.rect(wordle_screen, WHITE, (600, 600, 100, 100))
pygame.display.update()
'''

# game loop
hiddenWord = input("What is the answer to the puzzle? ")
count = 0
play = True
while count <= 6 or play:
    guess = input("What is your guess? ")
    if(guess == hiddenWord):
        play = False
        break
    getHint(guess)
    count += 1

'''
for i in range(0, len(guess))
    if( guess[i] == "+")
        make box yellow
    if (guess[i] == "*")
        make box green
    else
        make box grey
if all boxes green exit the loop
'''

# make sure the input is 5 letters long
# make sure it works if there is 2 or more of the same letter
