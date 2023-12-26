import pygame

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
    y2 = dis_height / 2

    h1_change = 0
    y1_change = 0

    while not game_over:
        ...


game_loop();