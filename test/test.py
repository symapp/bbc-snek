import pygame
from random import *

random = Random()
pygame.init()


# display
size_x = 851
size_y = 801
surface = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("snek! by simao")


while True:
    pygame.draw.rect(surface, "#ffffff", pygame.Rect(100, 100, 100, 100))
    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse)
            if pygame.Rect(100, 100, 100, 100).collidepoint(mouse):
                print("bla")
