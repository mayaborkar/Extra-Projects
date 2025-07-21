import pygame
import requests
from bs4 import BeautifulSoup
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (83, 141, 78)
YELLOW = (181, 159, 59)
GRAY = (120, 124, 126)

## Getting the hidden word from webscraping
url = "https://www.wordunscrambler.net/word-list/wordle-word-list"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

list_items = soup.find_all("li", class_="invert light")

words = [li.a.text.strip().upper() for li in list_items if li.a]

print(f"Found {len(words)} words.")

hiddenWord = random.choice(words)
print(f"Random word selected: {hiddenWord}")

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Maya's Wordle")
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)

tile_size = 60
margin = 10

count = 0
play = True
guess_list = []

def getHint(yourWord):
    yourWord = yourWord.upper()
    result = [GRAY] * len(yourWord)
    answer_letters = list(hiddenWord)

    for i in range(len(yourWord)):
        if yourWord[i] == hiddenWord[i]:
            result[i] = GREEN
            answer_letters[i] = None

    for i in range(len(yourWord)):
        if result[i] == GRAY and yourWord[i] in answer_letters:
            result[i] = YELLOW
            answer_letters[answer_letters.index(yourWord[i])] = None

    return result

def draw_board():
    global current_guess
    screen.fill(WHITE)
    for row in range(len(guess_list)):
        guess, colors = guess_list[row]
        for col in range(len(guess)):
            x = margin + col * (tile_size + margin)
            y = margin + row * (tile_size + margin)
            pygame.draw.rect(screen, colors[col], (x, y, tile_size, tile_size))
            text = font.render(guess[col], True, WHITE)
            screen.blit(text, (x + 15, y + 10))

    # Draw current guess outline
    row = len(guess_list)
    for col in range(5):
        x = margin + col * (tile_size + margin)
        y = margin + row * (tile_size + margin)
        pygame.draw.rect(screen, BLACK, (x, y, tile_size, tile_size), 2)
        if col < len(current_guess):
            text = font.render(current_guess[col], True, BLACK)
            screen.blit(text, (x + 15, y + 10))

    # Draw prompt
    prompt_text = small_font.render("Type your guess and press Enter", True, BLACK)
    screen.blit(prompt_text, (margin, 560))

    pygame.display.update()

# game loop
current_guess = ""
run = True
while run:
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(current_guess) == 5:
                    colors = getHint(current_guess)
                    guess_list.append((current_guess.upper(), colors))
                    if current_guess.upper() == hiddenWord:
                        print("You guessed it!")
                        # Show all green tiles for correct guess before quitting
                        pygame.time.delay(500)
                        run = False
                    current_guess = ""
                    count += 1
                    if count >= 6:
                        print("Out of guesses. The word was:", hiddenWord)
                        pygame.time.delay(1000)
                        run = False
            elif event.key == pygame.K_BACKSPACE:
                current_guess = current_guess[:-1]
            elif len(current_guess) < 5 and event.unicode.isalpha():
                current_guess += event.unicode.upper()

pygame.quit()
