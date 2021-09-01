import pygame
from pygame.locals import *
import time
from random import *

random = Random()
pygame.init()

# Font
pygame.font.init()
font = pygame.font.SysFont("Uni Sans", 50)

# Display
size_x = 851  # 17 felder
size_y = 801  # 15 felder
surface = pygame.display.set_mode((size_x, size_y))

# Colors
lineColor = (120, 150, 200)
backgroundColor = (140, 177, 217)
logoBackgroundColor = (175, 208, 214)
darkerLogoBackgroundColor = (120, 163, 169)
snakeColor = (230, 138, 0)
darkerSnakeColor = (255, 163, 0)
appleColor = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

color_apple = (255, 0, 0)
color_stem = (134, 89, 45)
color_leaf = (92, 214, 92)
color_leaf_middle = (32, 154, 32)
color_highlight_apple = (255, 255, 255)

# Fonts
fontSize = 80
mainFont = pygame.font.Font(None, fontSize)
snekFont = pygame.font.Font(None, 150)
font2 = pygame.font.Font(None, 50)

# Constant Variables
username = ""
input_box = pygame.Rect(185, 700, 400, 50)
playBox = pygame.Rect(80, 700, 95, 50)
menuBox = pygame.Rect(650, 700, 160, 50)
color_inactive = (100, 100, 100)
color = color_inactive
color_active = (226, 127, 129)

# Functions
def resetMainScreen():
    global username, color

    active = False
    username_done = False
    highlight_play_button = False
    highlight_menu_button = False
    menu_button_clicked = False

    while True:
        # Main Logo
        surface.fill(backgroundColor)
        pygame.draw.rect(surface, darkerLogoBackgroundColor, pygame.Rect(55, 155, 330, 135), border_radius=30)
        pygame.draw.rect(surface, logoBackgroundColor, pygame.Rect(60, 160, 325, 130), border_radius=30)
        surface.blit(mainFont.render("Welcome to:", True, (54, 57, 59)), (60, 80))

        for i in range(1, 6):
            surface.blit(snekFont.render("snek!", True, (155, 120, 155)), (80+i, 170+i))

        surface.blit(snekFont.render("snek!", True, (255, 220, 255)), (80, 170))

        # Leaderboard

        # Options Menu Button
        if menu_button_clicked:
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(646, 700, 160, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Options", True, (255, 255, 255)), (660, 707))
            pygame.display.flip()
            time.sleep(0.3)

            # Moves Button Up
            pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(650, 700, 160, 50), border_radius=10)
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(646, 696, 160, 50), border_radius=10)
            play_font = pygame.font.Font(None, 52)
            surface.blit(play_font.render("Options", True, (255, 255, 255)), (659, 706))
            pygame.display.flip()
            time.sleep(0.1)

            menu_button_clicked = False
            resetOptionsScreen()

        pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(650, 700, 160, 50), border_radius=10)
        pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(646, 696, 160, 50), border_radius=10)
        menuButtonFont = pygame.font.Font(None, 52)

        if highlight_menu_button:
            surface.blit(menuButtonFont.render("Options", True, (255, 220, 255)), (659, 707))
        else:
            surface.blit(menuButtonFont.render("Options", True, (255, 255, 255)), (659, 707))

        mouse = pygame.mouse.get_pos()
        if menuBox.collidepoint(mouse):
            highlight_menu_button = True
            for eventOptionsButton in pygame.event.get():
                if eventOptionsButton.type == pygame.MOUSEBUTTONDOWN:
                    menu_button_clicked = True
        else:
            highlight_menu_button = False


        # Input Box
        pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(185, 700, 400, 50), border_radius=10)
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(188, 703, 394, 44), border_radius=10)

        # Play Button Clicked
        if username_done:
            # Checks If Username Is Valid + Keeps Username / Writes Message In Input Box
            if username == "":
                username_input_color = (200, 200, 200)
                txt_surface = font2.render("Pls Username uwu", True, username_input_color)
                input_box.w = 400
                surface.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
                pygame.draw.rect(surface, color, input_box, 4, border_radius=10)

            else:
                username_input_color = (54, 57, 59)
                txt_surface = font2.render(username, True, username_input_color)
                input_box.w = 400
                surface.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
                pygame.draw.rect(surface, color, input_box, 4, border_radius=10)

            # Moves Button Down
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(80, 700, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Play", True, (255, 255, 255)), (90, 708))
            pygame.display.flip()
            time.sleep(0.3)

            # Moves Button Up
            pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(80, 700, 95, 50), border_radius=10)
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(76, 696, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 52)
            surface.blit(play_font.render("Play", True, (255, 255, 255)), (89, 707))
            pygame.display.flip()
            time.sleep(0.1)

            if username != "":
                return
            else:
                username_done = False

        # Draws Button
        pygame.draw.rect(surface, (50, 50, 50), pygame.Rect(80, 700, 95, 50), border_radius=10)
        pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(76, 696, 95, 50), border_radius=10)
        play_font = pygame.font.Font(None, 52)

        # Highlights Button
        if highlight_play_button:
            surface.blit(play_font.render("Play", True, (255, 220, 255)), (89, 707))
        else:
            surface.blit(play_font.render("Play", True, (255, 255, 255)), (89, 707))

        # Checks If Button Should Be Highlighted
        mouse = pygame.mouse.get_pos()
        if playBox.collidepoint(mouse) and not username_done:
            highlight_play_button = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    username_done = True
        else:
            highlight_play_button = False


        # Input Box -> https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if input_box.collidepoint(mouse) and not active:
            color = (255, 220, 255)
        else:
            color = color_active if active else color_inactive

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username_done = True
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_DOLLAR:
                        username = ""
                    elif txt_surface.get_width() <= 350 and event.key != pygame.K_RETURN:
                        username += event.unicode
        if username == "" and not active:
            username_input_color = (200, 200, 200)
            txt_surface = font2.render("Username", True, username_input_color)
        else:
            username_input_color = (54, 57, 59)
            txt_surface = font2.render(username, True, username_input_color)
        input_box.w = 400
        surface.blit(txt_surface, (input_box.x+10, input_box.y+10))
        pygame.draw.rect(surface, color, input_box, 4, border_radius=10)


        pygame.display.flip()


def resetBackground():
    surface.fill(backgroundColor)
    for i in range(16):
        pygame.draw.line(surface, lineColor, (0, (i * 50) + 50), (850, (i * 50) + 50), width=1)
    for i in range(19):
        pygame.draw.line(surface, lineColor, ((i * 50), 50), ((i * 50), 800), width=1)

    # Score
    surface.blit(font.render("Score: " + str(score), True, (54, 57, 59)), (10, 10))

    # Username
    usernameSurface = font.render(username, True, (54, 57, 59))
    width = max(0, usernameSurface.get_width() + 10)
    surface.blit(usernameSurface, (840-width, 10))


def resetOptionsScreen():
    surface.fill(backgroundColor)
    pygame.display.flip()
    time.sleep(1)


def showScore():

    for i in range(500):
        surface.fill(backgroundColor)
        fontBigScore = pygame.font.SysFont("Uni Sans", int(50 + i/10))
        surface.blit(fontBigScore.render("Score: " + str(score), True, (54, 57, 59)), (10+i*0.48, 10+i*0.38))
        pygame.display.flip()

    while True:
        surface.fill(backgroundColor)
        mouse = pygame.mouse.get_pos()
        fontBigScore = pygame.font.SysFont("Uni Sans", 100)
        surface.blit(fontBigScore.render("Score: " + str(score), True, (54, 57, 59)), (250, 200))

        if 400 < mouse[1] < 500 and 300 < mouse[0] < 500:
            pygame.draw.rect(surface, (40, 40, 40), pygame.Rect(300, 400, 210, 110), border_radius=10)
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(295, 395, 210, 110), border_radius=10)
            font = pygame.font.SysFont("Uni Sans", 52)
            surface.blit(font.render("Try again", True, (255, 255, 255)), (324, 429))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return

        else:
            pygame.draw.rect(surface, (40, 40, 40), pygame.Rect(305, 405, 200, 100), border_radius=10)
            pygame.draw.rect(surface, (100, 100, 100), pygame.Rect(300, 400, 200, 100), border_radius=10)
            font = pygame.font.SysFont("Uni Sans", 50)
            surface.blit(font.render("Try again", True, (255, 255, 255)), (325, 430))


        pygame.display.flip()

        # Makes Sure Screen Continues Responding
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                continue


def drawSnake():
    for i in reversed(range(len(snakeTailX))):
        temp_x = snakeTailX[i]
        temp_y = snakeTailY[i]


        # Snake Color
        if i < 52:
            snake_tail_color = (230, 138, 0+i*5)
        elif 52 <= i < 98:
            snake_tail_color = (230-(i-52)*5, 138, 255)
        elif 98 <= i < 126:
            snake_tail_color = (0, 138-(i-98)*5, 255)
        elif 126 <= i < 177:
            snake_tail_color = (0+(i-126)*5, 3, 255)
        elif 177 <= i < 227:
            snake_tail_color = (255, 0+(i-177)*5, 255)
        elif 227 <= i:
            snake_tail_color = (255, 255, 255)


        # Draws Body With Curves If Necessary
        if i == 0:
            if snakeHeadX > snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] < snakeTailY[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeHeadX < snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] < snakeTailY[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY > snakeTailY[i] and snakeTailX[i] > snakeTailX[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY < snakeTailY[i] and snakeTailX[i] > snakeTailX[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY > snakeTailY[i] and snakeTailX[i] < snakeTailX[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY < snakeTailY[i] and snakeTailX[i] < snakeTailX[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            elif snakeHeadX < snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] > snakeTailY[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeHeadX > snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] > snakeTailY[i+1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            else:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50))
        elif 0 < i < (len(snakeTailX)-1):
            if snakeTailX[i-1] > snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] < snakeTailY[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeTailX[i-1] < snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] < snakeTailY[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] > snakeTailY[i] and snakeTailX[i] > snakeTailX[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] < snakeTailY[i] and snakeTailX[i] > snakeTailX[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] > snakeTailY[i] and snakeTailX[i] < snakeTailX[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] < snakeTailY[i] and snakeTailX[i] < snakeTailX[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            elif snakeTailX[i-1] < snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] > snakeTailY[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeTailX[i-1] > snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] > snakeTailY[i + 1]:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            else:
                pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50))
        else:
            pygame.draw.rect(surface, snake_tail_color, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50))

    # Draws Head With Curves If Necessary
    body_comes_from_bottom = True if snakeHeadX == snakeTailX[0] and snakeHeadY < snakeTailY[0] else False
    body_comes_from_top = True if snakeHeadX == snakeTailX[0] and snakeHeadY > snakeTailY[0] else False
    body_comes_from_left = True if snakeHeadX > snakeTailX[0] and snakeHeadY == snakeTailY[0] else False
    body_comes_from_right = True if snakeHeadX < snakeTailX[0] and snakeHeadY == snakeTailY[0] else False

    if direction == "right":
        if body_comes_from_bottom:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_right_radius=25, border_top_left_radius=10)
        elif body_comes_from_top:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_bottom_right_radius=25, border_bottom_left_radius=10)
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_right_radius=25, border_bottom_right_radius=25)

        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 15), 8)
        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 35), 8)

        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 38, (snakeHeadY * 50 + 51) + 15), 3)
        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 38, (snakeHeadY * 50 + 51) + 35), 3)

    elif direction == "left":
        if body_comes_from_bottom:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_left_radius=25, border_top_right_radius=10)
        elif body_comes_from_top:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_bottom_left_radius=25, border_bottom_right_radius=10)
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_left_radius=25, border_bottom_left_radius=25)

        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 15), 8)
        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 35), 8)

        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 12, (snakeHeadY * 50 + 51) + 15), 3)
        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 12, (snakeHeadY * 50 + 51) + 35), 3)

    elif direction == "up":
        if body_comes_from_left:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_right_radius=25, border_bottom_right_radius=10)
        elif body_comes_from_right:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                            border_top_left_radius=25, border_bottom_left_radius=10)
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_top_right_radius=25, border_top_left_radius=25)

        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 15), 8)
        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 15), 8)

        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 12), 3)
        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 12), 3)

    elif direction == "down":
        if body_comes_from_left:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_bottom_right_radius=25, border_top_right_radius=10)
        elif body_comes_from_right:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                            border_bottom_left_radius=25, border_top_left_radius=10)
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 50, 50),
                             border_bottom_right_radius=25, border_bottom_left_radius=25)

        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 35), 8)
        pygame.draw.circle(surface, white, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 35), 8)

        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 15, (snakeHeadY * 50 + 51) + 38), 3)
        pygame.draw.circle(surface, black, ((snakeHeadX * 50 + 1) + 35, (snakeHeadY * 50 + 51) + 38), 3)


def drawApple():
    for i in range(numApplesWanted):
        if applesX[i] != "":
            # Apple Design
            pygame.draw.rect(surface, color_stem, pygame.Rect((applesX[i]*50+25) - 1, (applesY[i]*50+75) - 18, 2, 10), border_radius=1)
            pygame.draw.circle(surface, color_apple, ((applesX[i]*50+25), (applesY[i]*50+75) + 6), 16)
            pygame.draw.ellipse(surface, color_leaf, pygame.Rect((applesX[i]*50+25) + 3, (applesY[i]*50+75) - 20, 10, 6))
            pygame.draw.rect(surface, color_leaf_middle, pygame.Rect((applesX[i]*50+25) + 5, (applesY[i]*50+75) - 18, 6, 1))
            pygame.draw.polygon(surface, color_highlight_apple, (((applesX[i]*50+25) - 7, (applesY[i]*50+75) - 6),
                                                               ((applesX[i]*50+25) - 5, (applesY[i]*50+75) - 7),
                                                               ((applesX[i]*50+25) - 3, (applesY[i]*50+75) - 6),
                                                               ((applesX[i]*50+25) - 4, (applesY[i]*50+75) - 4),
                                                               ((applesX[i]*50+25) - 7, (applesY[i]*50+75) - 1),
                                                               ((applesX[i]*50+25) - 10, (applesY[i]*50+75) - 2),
                                                               ((applesX[i]*50+25) - 9, (applesY[i]*50+75) - 1),
                                                               ((applesX[i]*50+25) - 9, (applesY[i]*50+75) - 4),
                                                               ))


def moveSnakeForward():
    global snakeHeadX, snakeHeadY, snakeTailX, snakeTailY, run

    # Move Body Forward
    for i in reversed(range(len(snakeTailX))):
        if i != 0:
            snakeTailX[i] = snakeTailX[i - 1]
            snakeTailY[i] = snakeTailY[i - 1]
        else:
            snakeTailX[i] = snakeHeadX
            snakeTailY[i] = snakeHeadY

    # Move Head Forward
    if direction == "right":
        snakeHeadX += 1
    if direction == "left":
        snakeHeadX -= 1
    if direction == "up":
        snakeHeadY -= 1
    if direction == "down":
        snakeHeadY += 1


def doCollisionCheck():
    global run

    if snakeHeadX > 16:
        return True
    elif snakeHeadX < 0:
        return True
    elif snakeHeadY > 14:
        return True
    elif snakeHeadY < 0:
        return True
    for a in range(0, len(snakeTailX), 1):
        if snakeTailX[a] == snakeHeadX and snakeTailY[a] == snakeHeadY:
            return True
    return False


# Main Loop
while True:

    resetMainScreen()

    # Snake
    snakeTailX = [4, 3, 2, 1]
    snakeTailY = [7, 7, 7, 7]
    snakeHeadX = 5
    snakeHeadY = 7
    freespaces = 17 * 15 - len(snakeTailX) - 1

    # Reset Variables
    run = True
    direction = "right"
    numApplesWanted = 40
    applesX = [""]*numApplesWanted
    applesY = [""]*numApplesWanted
    score = 0
    timerIsDone = False
    startTime = time.time()

    resetBackground()

    while run:

        # Set Direction (https://www.pygame.org/docs/ref/event.html)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if timerIsDone:
                keys = pygame.key.get_pressed()
                if keys[K_LEFT] or keys[K_a]:
                    if direction != "right":
                        direction = "left"
                        timerIsDone = False

                elif keys[K_RIGHT] or keys[K_d]:
                    if direction != "left":
                        direction = "right"
                        timerIsDone = False

                elif keys[K_UP] or keys[K_w]:
                    if direction != "down":
                        direction = "up"
                        timerIsDone = False

                elif keys[K_DOWN] or keys[K_s]:
                    if direction != "up":
                        direction = "down"
                        timerIsDone = False

        # Apple Spawner V2

        if freespaces < numApplesWanted:
            numApplesWanted -= 1

        for i in range(len(applesX)):
            if applesX[i] == "":
                tmpX = random.randint(0, 16)
                tmpY = random.randint(0, 14)
                if tmpX != snakeHeadX and tmpY != snakeHeadY:
                    applesX[i] = tmpX
                    applesY[i] = tmpY

            for a in range(len(applesX)):
                if applesX[a] == snakeHeadX and applesY[a] == snakeHeadY:
                    applesX[a] = ""
                    applesY[a] = ""
                    score += 1
                    snakeTailX.append(oldX)
                    snakeTailY.append(oldY)
                else:
                    for i in range(len(snakeTailX)):
                        if applesX[a] == snakeTailX[i] and applesY[a] == snakeTailY[i]:
                            applesX[a] = ""
                            applesY[a] = ""
                    for j in range(len(applesX)):
                        if j != a:
                            if applesX[a] == applesX[j] and applesY[a] == applesY[j]:
                                applesX[a] = ""
                                applesY[a] = ""


        if not doCollisionCheck():
            drawApple()
            drawSnake()
            pygame.display.flip()
            # Timer (https://www.programiz.com/python-programming/time)
            elapsedTime = time.time() - startTime
            if elapsedTime > 0.5:
                timerIsDone = True
                startTime = time.time()

                # Remember Last Tail Position
                oldX = snakeTailX[len(snakeTailX)-1]
                oldY = snakeTailY[len(snakeTailY)-1]

                resetBackground()
                moveSnakeForward()
        elif doCollisionCheck():
            run = False



    showScore()