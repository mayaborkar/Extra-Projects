import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()
    width = 970
    height = 520

    p_width = 40
    p_height = 150
    p_speed = 1

    p1_y = height/2 - (p_height / 2)
    p2_y = height/2 - (p_height / 2)

    ball_width = ball_height = 20

    key_pressed = False
    key_released = False
    what_key = ""

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((width, height))

    paddle1 = pygame.Surface((p_width, p_height)).convert()
    paddle1.fill(WHITE)
    paddle2 = pygame.Surface((p_width, p_height)).convert()
    paddle2.fill(WHITE)
    '''
    ball = pygame.Surface(ball_width, ball_height).convert
    ball_rect = pygame.Rect(width/2 - (ball_width/2), height/2 - (ball_height/2), ball_width, ball_height)
    ball.fill(WHITE)
    '''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key_pressed = True
                # key_released = False
                if event.key == pygame.K_w:
                    what_key = "w"
                elif event.key == pygame.K_s:
                    what_key = "s"
                elif event.key == pygame.K_DOWN:
                    what_key = "d"
                elif event.key == pygame.K_UP:
                    what_key = "u"
            elif event.type == pygame.KEYUP:
                key_pressed = False
                # key_released = True

        if key_pressed :
            if what_key == "w":
                p1_y -= p_speed
            elif what_key == "s":
                p1_y += p_speed
        if key_pressed:
            if what_key == "u":
                p2_y -= p_speed
            elif what_key == "d":
                p2_y += p_speed

        screen.fill(BLACK)
        if 0 < p1_y < height - p_height:
            screen.blit(paddle1, (width/20, p1_y))
        if 0 < p2_y < height - p_height:
            screen.blit(paddle2, (930-(width/20), p2_y))
        pygame.display.flip()


if __name__ == "__main__":
    main()
