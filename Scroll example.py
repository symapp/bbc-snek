import pygame

pygame.init()
size_x = 851  # 17 felder
size_y = 801  # 15 felder
surface = pygame.display.set_mode((size_x, size_y))

scroll_y = 0


while True:
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4: scroll_y = min(scroll_y + 10, 0)
            if e.button == 5: scroll_y = max(scroll_y - 10, -300)
    print(scroll_y)