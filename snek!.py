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
darkerBackgroundColor = "#4CB4DC"
topMenuColor = (120, 150, 200)
backgroundColor = "#5BC3EB"
logoBackgroundColor = "#6BD3FB"
darkerLogoBackgroundColor = "#3BA3CB"
snakeColor = "#FFA10A"
appleColor = (255, 0, 0)
loadingBarColor = (230, 138, 0)
buttonShadow = "#303030"
buttonColor = "#59656F"

white = (255, 255, 255)
highlight = (255, 220, 255)
black = (0, 0, 0)
red = (255, 0, 0)
raisinBlack = "#1D1E2C"

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
optionsFont = pygame.font.Font(None, 45)

# Constant Variables
username = ""
input_box = pygame.Rect(185, 700, 400, 50)
color_inactive = (100, 100, 100)
color = color_inactive
color_active = (226, 127, 129)

# Boxes / Buttons
playBox = pygame.Rect(80, 700, 95, 50)
optionsBox = pygame.Rect(650, 700, 160, 50)
quitBox = pygame.Rect(750, 5, 95, 40)
quitBoxShadow = pygame.Rect(753, 8, 95, 40)
backBox = pygame.Rect(750, 5, 95, 40)
backBoxShadow = pygame.Rect(753, 8, 95, 40)
topMenuBox = pygame.Rect(0, 0, 851, 51)

optionsPos1 = pygame.Rect(40, 51 + 35, 400, 80)
optionsPos2 = pygame.Rect(450, 56 + 35 * 5 + 80, 30, 30)
optionsPos3 = pygame.Rect(450, 56 + 35 * 5 + 80 * 2, 30, 30)
optionsPos4 = pygame.Rect(450, 56 + 35 * 7 + 80 * 3, 30, 30)
optionsPos5 = pygame.Rect(450, 56 + 35 * 9 + 80 * 4, 30, 30)

# Functions
def resetMainScreen():
    global username, color, run

    active = False
    username_done = False
    highlight_play_button = False
    highlight_options_button = False
    options_button_clicked = False

    while True:
        # Main Logo
        surface.fill(backgroundColor)
        surface.blit(mainFont.render("Welcome to:", True, raisinBlack), (60, 80))
        #for i in range(1, 10):
        #    pygame.draw.rect(surface, darkerLogoBackgroundColor, pygame.Rect(60+i, 160+i, 325, 130), border_radius=30)
#
        #pygame.draw.rect(surface, logoBackgroundColor, pygame.Rect(60, 160, 325, 130), border_radius=30)


        for i in range(1, 5):
            surface.blit(snekFont.render("snek!", True, (155, 120, 155)), (85+i, 170+i))

        surface.blit(snekFont.render("snek!", True, (255, 220, 255)), (85, 170))

        # Leaderboard


        # Input Box
        pygame.draw.rect(surface, buttonColor, pygame.Rect(185, 700, 400, 50), border_radius=10)
        pygame.draw.rect(surface, white, pygame.Rect(188, 703, 394, 44), border_radius=10)

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
                username_input_color = raisinBlack
                txt_surface = font2.render(username, True, username_input_color)
                input_box.w = 400
                surface.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
                pygame.draw.rect(surface, color, input_box, 4, border_radius=10)

            # Draws Options Button
            pygame.draw.rect(surface, buttonShadow, pygame.Rect(650, 700, 160, 50), border_radius=10)
            pygame.draw.rect(surface, buttonColor, pygame.Rect(646, 696, 160, 50), border_radius=10)
            optionsButtonFont = pygame.font.Font(None, 52)
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))

            # Moves Button Down
            pygame.draw.rect(surface, buttonColor, pygame.Rect(80, 700, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Play", True, white), (90, 708))
            pygame.display.flip()
            time.sleep(0.3)

            # Moves Button Up
            pygame.draw.rect(surface, buttonShadow, pygame.Rect(80, 700, 95, 50), border_radius=10)
            pygame.draw.rect(surface, buttonColor, pygame.Rect(76, 696, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 52)
            surface.blit(play_font.render("Play", True,white), (89, 707))
            pygame.display.flip()
            time.sleep(0.1)

            if username != "":
                run = True
                return
            else:
                username_done = False

        # Draws Button
        pygame.draw.rect(surface, buttonShadow, pygame.Rect(80, 700, 95, 50), border_radius=10)
        pygame.draw.rect(surface, buttonColor, pygame.Rect(76, 696, 95, 50), border_radius=10)
        play_font = pygame.font.Font(None, 52)

        # Highlights Button
        if highlight_play_button:
            surface.blit(play_font.render("Play", True, highlight), (89, 707))
        else:
            surface.blit(play_font.render("Play", True, white), (89, 707))

        # Checks If Buttons Should Be Highlighted / Were Pressed Pressed
        mouse = pygame.mouse.get_pos()
        if playBox.collidepoint(mouse):
            highlight_play_button = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    username_done = True
        else:
            highlight_play_button = False

        mouse = pygame.mouse.get_pos()
        if optionsBox.collidepoint(mouse):
            highlight_options_button = True
            for eventOptionsButton in pygame.event.get():
                if eventOptionsButton.type == pygame.MOUSEBUTTONDOWN:
                    options_button_clicked = True
        else:
            highlight_options_button = False

        # Input Box -> https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if input_box.collidepoint(mouse) and not active:
            color = highlight
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
                if event.key == pygame.K_o:
                    options_button_clicked = True
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
            username_input_color = raisinBlack
            txt_surface = font2.render(username, True, username_input_color)
        input_box.w = 400
        surface.blit(txt_surface, (input_box.x+10, input_box.y+10))
        pygame.draw.rect(surface, color, input_box, 4, border_radius=10)

        # Options Button
        if options_button_clicked:
            # Moves Button Down
            pygame.draw.rect(surface, buttonColor, pygame.Rect(650, 700, 160, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Options", True, white), (660, 707))
            pygame.display.flip()
            time.sleep(0.3)

            # Moves Button Up
            pygame.draw.rect(surface, buttonShadow, pygame.Rect(650, 700, 160, 50), border_radius=10)
            pygame.draw.rect(surface, buttonColor, pygame.Rect(646, 696, 160, 50), border_radius=10)
            play_font = pygame.font.Font(None, 52)
            surface.blit(play_font.render("Options", True, white), (659, 706))
            pygame.display.flip()
            time.sleep(0.1)
            options_button_clicked = False
            resetOptionsScreen()

        pygame.draw.rect(surface, buttonShadow, pygame.Rect(650, 700, 160, 50), border_radius=10)
        pygame.draw.rect(surface, buttonColor, pygame.Rect(646, 696, 160, 50), border_radius=10)
        optionsButtonFont = pygame.font.Font(None, 52)

        # Highlights Button
        if highlight_options_button:
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))
        else:
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))

        pygame.display.flip()


def resetBackground():
    global highlight_quit_button, quit_button_clicked, run

    surface.fill(backgroundColor)
    for i in range(1, 18):
        for j in range(16):
            if (i) % 2 == 0 or i == 0:
                if (j) % 2 == 0 or j == 0:
                    pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect((i * 50)-50, (j*50) + 50, 50, 50))
            else:
                if (j) % 2 == 1:
                    pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect((i * 50)-50, (j * 50) + 50, 50, 50))
    pygame.draw.line(surface, darkerBackgroundColor, (0, 49), (851, 49), width=2)

    # Score
    surface.blit(font.render("Score: " + str(score), True, raisinBlack), (10, 10))

    # Username
    usernameSurface = font.render(username, True, raisinBlack)
    width = max(0, usernameSurface.get_width() + 10)
    surface.blit(usernameSurface, (420-width/2, 10))

    # Quit
    if quit_button_clicked:
        drawSnake()
        drawApple()
        pygame.draw.rect(surface, buttonColor, quitBoxShadow, border_radius=10)
        quit_font = pygame.font.Font(None, 40)
        surface.blit(quit_font.render("Quit", True, white), (768, 15))
        pygame.display.flip()
        time.sleep(0.3)

        # Moves Button Up
        pygame.draw.rect(surface, buttonShadow, quitBoxShadow, border_radius=10)
        pygame.draw.rect(surface, buttonColor, quitBox, border_radius=10)
        quit_font = pygame.font.Font(None, 42)
        surface.blit(quit_font.render("Quit", True, white), (765, 12))
        pygame.display.flip()
        time.sleep(0.1)

        quit_button_clicked = False
        run = False

    pygame.draw.rect(surface, buttonShadow, quitBoxShadow, border_radius=10)
    pygame.draw.rect(surface, buttonColor, quitBox, border_radius=10)
    quit_font = pygame.font.Font(None, 42)

    if highlight_quit_button:
        surface.blit(quit_font.render("Quit", True, highlight), (765, 12))
    else:
        surface.blit(quit_font.render("Quit", True, white), (765, 12))


def resetOptionsScreen():
    back_button_clicked = False
    highlight_back_button = False
    while True:
        surface.fill(backgroundColor)

        # Top Menu
        pygame.draw.rect(surface, buttonShadow, pygame.Rect(0, 5, 140, 50),
                         border_bottom_right_radius=5, border_top_right_radius=5)
        pygame.draw.rect(surface, buttonColor, pygame.Rect(0, 1, 135, 50),
                         border_bottom_right_radius=5, border_top_right_radius=5)
        surface.blit(optionsFont.render("Options", True, white), (10, 10))

        if back_button_clicked:
            pygame.draw.rect(surface, buttonColor, backBoxShadow, border_radius=10)
            back_font = pygame.font.Font(None, 40)
            surface.blit(back_font.render("Back", True, white), (768, 15))
            pygame.display.flip()
            time.sleep(0.3)

            # Moves Button Up
            pygame.draw.rect(surface, buttonShadow, backBoxShadow, border_radius=10)
            pygame.draw.rect(surface, buttonColor, backBox, border_radius=10)
            back_font = pygame.font.Font(None, 42)
            surface.blit(back_font.render("Back", True, white), (765, 12))
            pygame.display.flip()
            time.sleep(0.1)

            return

        pygame.draw.rect(surface, buttonShadow, backBoxShadow, border_radius=10)
        pygame.draw.rect(surface, buttonColor, backBox, border_radius=10)
        back_font = pygame.font.Font(None, 42)

        if highlight_back_button:
            surface.blit(back_font.render("Back", True, highlight), (765, 12))
        else:
            surface.blit(back_font.render("Back", True, white), (765, 12))

        mouse = pygame.mouse.get_pos()
        if backBox.collidepoint(mouse):
            highlight_back_button = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    back_button_clicked = True
        else:
            highlight_back_button = False

        # SETTINGS
        # Setting name
        pygame.draw.rect(surface, white, pygame.Rect(40, 51 + 35, 400, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(40, 51 + 35*3 + 80, 400, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(40, 51 + 35*5 + 80*2, 400, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(40, 51 + 35*7 + 80*3, 400, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(40, 51 + 35*9 + 80*4, 400, 80), border_radius=15)

        # More information
        pygame.draw.rect(surface, white, pygame.Rect(450, 56 + 35, 30, 30), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(450, 56 + 35 * 3 + 80, 30, 30), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(450, 56 + 35 * 5 + 80 * 2, 30, 30), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(450, 56 + 35 * 7 + 80 * 3, 30, 30), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(450, 56 + 35 * 9 + 80 * 4, 30, 30), border_radius=15)

        # Setting
        pygame.draw.rect(surface, white, pygame.Rect(550, 51 + 35, 200, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(550, 51 + 35 * 3 + 80, 200, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(550, 51 + 35 * 5 + 80 * 2, 200, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(550, 51 + 35 * 7 + 80 * 3, 200, 80), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(550, 51 + 35 * 9 + 80 * 4, 200, 80), border_radius=15)

        # Custom
        pygame.draw.rect(surface, white, pygame.Rect(760, 56 + 35, 50, 50), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(760, 56 + 35 * 3 + 80, 50, 50), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(760, 56 + 35 * 5 + 80 * 2, 50, 50), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(760, 56 + 35 * 7 + 80 * 3, 50, 50), border_radius=15)
        pygame.draw.rect(surface, white, pygame.Rect(760, 56 + 35 * 9 + 80 * 4, 50, 50), border_radius=15)





        for event in pygame.event.get():
            continue

        pygame.display.flip()


def showScore():

    for i in range(500):
        surface.fill(backgroundColor)
        fontBigScore = pygame.font.SysFont("Uni Sans", int(50 + i/5))

        surface.blit(fontBigScore.render("Score: " + str(score), True, raisinBlack), (10+i*0.38, 10+i*0.38))
        pygame.display.flip()

    startTime = time.time()
    while True:
        surface.fill(backgroundColor)
        fontBigScore = pygame.font.SysFont("Uni Sans", int(50 + i / 5))
        surface.blit(fontBigScore.render("Score: " + str(score), True, raisinBlack), (200, 200))

        # Checks If Timer Is Done Or If Keys Are Pressed
        elapsedTime = time.time() - startTime
        if elapsedTime > 3:
            return
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return

        # Loading Snake
        pygame.draw.rect(surface, snakeColor, pygame.Rect(0, 751, (851/3)*elapsedTime, 50))
        pygame.draw.rect(surface, snakeColor, pygame.Rect((851/3)*elapsedTime, 751, 50, 50),
                         border_top_right_radius=25, border_bottom_right_radius=25)
        pygame.draw.circle(surface, white, (((851/3)*elapsedTime) + 35, 751 + 15), 8)
        pygame.draw.circle(surface, white, (((851/3)*elapsedTime) + 35, 751 + 35), 8)

        pygame.draw.circle(surface, black, (((851/3)*elapsedTime) + 37, 751 + 15), 4)
        pygame.draw.circle(surface, black, (((851/3)*elapsedTime) + 37, 751 + 35), 4)

        pygame.display.flip()


def drawSnake():
    colorState = 0
    lastStateI = 0
    for i in reversed(range(len(snakeTailX))):
        temp_x = snakeTailX[i]
        temp_y = snakeTailY[i]

        if i < 50:
            snakeTailColor = (255, 161, 10+i*5)
        elif 50 <= i < 102:
            snakeTailColor = (255-(i-50)*5, 161, 255)
        elif 102 <= i < 134:
            snakeTailColor =  (0, 160-(i-102)*5, 255)
        elif 134 <= i < 186:
            snakeTailColor = (0+(i-134)*5, 1, 255)
        elif 186 <= i < 238:
            snakeTailColor = (255, 0+(i-186)*5, 255)
        else:
            snakeTailColor = (255, 255, 255)


        # Draws Body With Curves If Necessary
        if i == 0:
            if snakeHeadX > snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] < snakeTailY[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeHeadX < snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] < snakeTailY[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY > snakeTailY[i] and snakeTailX[i] > snakeTailX[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY < snakeTailY[i] and snakeTailX[i] > snakeTailX[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY > snakeTailY[i] and snakeTailX[i] < snakeTailX[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeHeadX == snakeTailX[i] and snakeHeadY < snakeTailY[i] and snakeTailX[i] < snakeTailX[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            elif snakeHeadX < snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] > snakeTailY[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeHeadX > snakeTailX[i] and snakeHeadY == snakeTailY[i] and snakeTailY[i] > snakeTailY[i+1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            else:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50))
        elif 0 < i < (len(snakeTailX)-1):
            if snakeTailX[i-1] > snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] < snakeTailY[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeTailX[i-1] < snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] < snakeTailY[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] > snakeTailY[i] and snakeTailX[i] > snakeTailX[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] < snakeTailY[i] and snakeTailX[i] > snakeTailX[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] > snakeTailY[i] and snakeTailX[i] < snakeTailX[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=25)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] < snakeTailY[i] and snakeTailX[i] < snakeTailX[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            elif snakeTailX[i-1] < snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] > snakeTailY[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_right_radius=25)
            elif snakeTailX[i-1] > snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i] and snakeTailY[i] > snakeTailY[i + 1]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=25)
            else:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50))
        else:
            if snakeTailX[i-1] < snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_right_radius=20, border_bottom_right_radius=20)
            elif snakeTailX[i-1] > snakeTailX[i] and snakeTailY[i-1] == snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=20, border_bottom_left_radius=20)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] < snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_bottom_left_radius=20, border_bottom_right_radius=20)
            elif snakeTailX[i-1] == snakeTailX[i] and snakeTailY[i-1] > snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, ((temp_x * 50 + 1), (temp_y * 50 + 51), 50, 50),
                                 border_top_left_radius=20, border_top_right_radius=20)

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
    global snakeHeadX, snakeHeadY, snakeTailX, snakeTailY, run, elapsedTime

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
run = True
while True:
    resetMainScreen()

    # Snake
    snakeTailX = [4, 3, 2, 1]
    snakeTailY = [7, 7, 7, 7]
    snakeHeadX = 5
    snakeHeadY = 7
    freespaces = 17 * 15 - len(snakeTailX) - 1

    # Reset Variables
    direction = "right"
    speed = 0.2
    numApplesWanted = 50
    score = 0
    applesX = [""]*numApplesWanted
    applesY = [""]*numApplesWanted
    highlight_quit_button = False
    quit_button_clicked = False
    timerIsDone = False
    stopSnake = False
    startTime = time.time()

    resetBackground()

    while run:
        # Highlight Quit Button
        mouse = pygame.mouse.get_pos()
        if quitBox.collidepoint(mouse):
            highlight_quit_button = True
            for eventOptionsButton in pygame.event.get():
                if eventOptionsButton.type == pygame.MOUSEBUTTONDOWN:
                    quit_button_clicked = True

        else:
            highlight_quit_button = False

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
                if tmpX != snakeHeadX or tmpY != snakeHeadY:
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


        if not doCollisionCheck() and not stopSnake:
            drawApple()
            drawSnake()
            pygame.display.flip()
            # Timer (https://www.programiz.com/python-programming/time)
            elapsedTime = time.time() - startTime
            if elapsedTime > speed:
                timerIsDone = True
                startTime = time.time()

                # Remember Last Tail Position
                oldX = snakeTailX[len(snakeTailX)-1]
                oldY = snakeTailY[len(snakeTailY)-1]

                resetBackground()
                moveSnakeForward()
        else:
            time.sleep(0.5)
            run = False



    showScore()