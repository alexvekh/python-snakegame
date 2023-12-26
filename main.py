import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game")

def game_loop():
    game_over = False
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10

        x1 += x1_change
        y1 += y1_change


        dis.fill(blue)
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.display.update()

        time.sleep(0.1)

    pygame.quit()
    quit()


game_loop();