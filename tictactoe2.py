# VERSION 2
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BOX_HEIGHT = 200
BOX_WIDTH = 200

# main
pygame.init()
mttt_screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maya's Tic Tac Toe")

location_array = [[[0, 0], [200, 0], [400, 0]],
                  [[0, 200], [200, 200], [400, 200]],
                  [[0, 400], [200, 400], [400, 400]]]

value_array = [[-1, -1, -1],
               [-1, -1, -1],
               [-1, -1, -1]]

play = True
row = 0
column = 0
font = pygame.font.Font(None, 300)

pygame.draw.rect(mttt_screen, BLACK, (location_array[0][0][0], location_array[0][0][1], 600, 600))

for i in range(0, 3):
    for j in range(0, 3):
        pygame.draw.rect(mttt_screen, WHITE, (location_array[i][j][0], location_array[i][j][1], BOX_WIDTH - 10, BOX_HEIGHT - 10))

while play:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.rect(mttt_screen, WHITE, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
                print("up")
                row -= 1
                row = row % 3
                pygame.draw.rect(mttt_screen, RED, ( location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
            elif event.key == pygame.K_DOWN:
                pygame.draw.rect(mttt_screen, WHITE, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
                print("down")
                row += 1
                row = row % 3
                pygame.draw.rect(mttt_screen, RED, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
            elif event.key == pygame.K_LEFT:
                pygame.draw.rect(mttt_screen, WHITE, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
                print("left")
                column -= 1
                column = column % 3
                pygame.draw.rect(mttt_screen, RED, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
            elif event.key == pygame.K_RIGHT:
                pygame.draw.rect(mttt_screen, WHITE, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
                print("right")
                column += 1
                column = column % 3
                pygame.draw.rect(mttt_screen, RED, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))
            elif event.key == pygame.K_SPACE:
                print("space")
                tic_tac = font.render("x", True, BLUE)
                mttt_screen.blit(tic_tac, (location_array[row][column][0] + 35, location_array[row][column][1]))
                column += 1
                column = column % 3
                pygame.draw.rect(mttt_screen, RED, (location_array[row][column][0], location_array[row][column][1], BOX_WIDTH - 20, BOX_HEIGHT - 20))




    pygame.display.update()

pygame.quit()

