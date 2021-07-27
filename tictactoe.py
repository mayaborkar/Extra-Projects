# VERSION 1
import pygame, sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def make_grid():
    pygame.draw.line(screen, WHITE, (0, 200), (600, 200))
    pygame.draw.line(screen, WHITE, (0, 400), (600, 400))
    pygame.draw.line(screen, WHITE, (200, 0), (200, 600))
    pygame.draw.line(screen, WHITE, (400, 0), (400, 600))


# start of main
pygame.init()
screen = pygame.display.set_mode((600, 600))

make_grid()

pygame.display.update()

font_x = pygame.font.Font(None, 200)
x_surface = font_x.render("x", True, WHITE)
x = 0
y = 0
play = True
pygame.display.set_caption("Maya's Tic Tac Toe")
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
                y -= 200
            elif event.key == pygame.K_DOWN:
                print("down")
                y += 200
            elif event.key == pygame.K_LEFT:
                print("left")
                x -= 200
            elif event.key == pygame.K_RIGHT:
                print("right")
                x += 200
            elif event.key == pygame.K_SPACE:
                print("space")

            pygame.draw.rect(screen, RED, (x, y, 200, 200))
            # screen.fill(BLACK)

    pygame.display.update()


