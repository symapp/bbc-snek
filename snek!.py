import pygame
from pygame.locals import *
import time
from random import *
from pygame.math import Vector2
import math

random = Random()
pygame.init()

# font
pygame.font.init()
font = pygame.font.SysFont("Uni Sans", 50)

# display
size_x = 851
size_y = 801
surface = pygame.display.set_mode((size_x, size_y))

# colors
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
lightGray = (200, 200, 200)
red = (255, 0, 0)
raisinBlack = "#1D1E2C"
puce = "#CD8E9B"
blackCoral = "#59656F"

color_apple = (255, 0, 0)
color_stem = (134, 89, 45)
color_leaf = (92, 214, 92)
color_leaf_middle = (32, 154, 32)
color_highlight_apple = (255, 255, 255)

# fonts
mainFont = pygame.font.Font(None, 80)
snekFont = pygame.font.Font(None, 150)
font2 = pygame.font.Font(None, 50)
optionsFont = pygame.font.Font(None, 45)
optionsTitleFont = pygame.font.Font(None, 50)
questionMark = pygame.font.Font(None, 30)
optionsFont = pygame.font.Font(None, 40)
leaderboardFont = pygame.font.Font(None, 40)
leaderboardFont2 = pygame.font.Font(None, 40)

# constant variables
username = ""
input_box = pygame.Rect(185, 700, 400, 50)
color_inactive = (100, 100, 100)
color = color_inactive
color_active = (226, 127, 129)

# boxes / buttons
playBox = pygame.Rect(80, 700, 95, 50)
optionsBox = pygame.Rect(650, 700, 160, 50)
quitBox = pygame.Rect(750, 3, 95, 40)
quitBoxShadow = pygame.Rect(753, 6, 95, 40)
backBox = pygame.Rect(750, 5, 95, 40)
backBoxShadow = pygame.Rect(753, 8, 95, 40)
topMenuBox = pygame.Rect(0, 0, 851, 51)
optionsPos1 = pygame.Rect(40, 86, 400, 80)
optionsPos2 = pygame.Rect(450, 311, 30, 30)
optionsPos3 = pygame.Rect(450, 391, 30, 30)
optionsPos4 = pygame.Rect(450, 541, 30, 30)
optionsPos5 = pygame.Rect(450, 691, 30, 30)

# options boxes
oBox1 = pygame.Rect(500, 100, 200, 50)
oBox2 = pygame.Rect(500, 250, 200, 50)
oBox3 = pygame.Rect(500, 400, 200, 50)
oBox4 = pygame.Rect(500, 550, 200, 50)
oBox5 = pygame.Rect(500, 700, 200, 50)

# default options list
numberOfApples = ["0", "1", "5", "10", "30", "50"]
defaultChosenNumberOfApples = 1
chosenNumberOfApples = defaultChosenNumberOfApples
speed = ["cansir", "impossible", "hard", "harder", "default", "easier", "easy", "ez pz"]
speedNumbers = ["0.0001", "1", "0.05", "0.1", "0.2", "0.3", "0.5", "0.02"]
defaultChosenSpeed = 4
chosenSpeed = defaultChosenSpeed
playingFieldSize = ["10x8", "17x15", "24x21"]
defaultChosenPlayingFieldSize = 1
chosenPlayingFieldSize = defaultChosenPlayingFieldSize
chosenSelfCollisions = True
chosenWallCollisions = True

# score
darkStoneGrey = "#817E75"
mediumDarkStoneGrey = "#89767D"
stoneGrey = "#918E85"
dirtBrown = "#594E2E"
lightDirtBrown = "#807041"
skull = pygame.image.load("skull.png")
cloud = pygame.image.load("cloud.png")
flowers = pygame.image.load("flowers.png")
caet = pygame.image.load("caet.png")
caet2 = pygame.image.load("caet2.png")


# letter whitelist
letterWhitelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z", "_", "-", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "ö",
                   "ä", "ü"]

# classes
class SunBeams:

    def __init__(self, angle):
        self.angle = angle


    def rotate(self):
        middle_point = [172, 125]
        radius = 1000
        self.angle += 10
        self.angle_rad = math.radians(self.angle)
        self.point = [middle_point[0] + radius * math.sin(self.angle_rad), middle_point[1] - radius * math.cos(self.angle_rad)]
        self.point2 = [middle_point[0] + 100 * math.sin(self.angle_rad), middle_point[1] - 100 * math.cos(self.angle_rad)]
        pygame.draw.line(surface, "#ffff00", self.point2, self.point, width=3)

class Clouds:
    def __init__(self, position):
        self.position = position

    def move(self):
        self.position[0] += 20
        if self.position[0] > 900:
            self.position[0] = -100
        surface.blit(pygame.transform.scale(cloud, (int(50*1.82), 50)), self.position)


# functions
def resetMainScreen():
    global username, color, run

    active = False
    username_done = False
    highlight_play_button = False
    options_button_clicked = False

    while True:
        surface.fill(backgroundColor)
        # grid
        for i in range(1, 18):
            for j in range(16):
                if i % 2 == 0 or i == 0:
                    if j % 2 == 0 or j == 0:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 100) - 170, (j * 100)-60, 100, 100))
                else:
                    if j % 2 == 1:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 100) - 170, (j * 100)-60, 100, 100))
        # apple
        pygame.draw.rect(surface, color_stem, pygame.Rect(178, -44, 4, 20), border_radius=1)
        pygame.draw.circle(surface, color_apple, (180, 2), 32)
        pygame.draw.ellipse(surface, color_leaf, pygame.Rect(186, -50, 20, 12))
        pygame.draw.rect(surface, color_leaf_middle, pygame.Rect(190, -46, 12, 2))
        pygame.draw.polygon(surface, color_highlight_apple,
                           ((180 - 100 / 50 * 7, -10 - 100 / 50 * 6),
                            (180 - 100 / 50 * 5, -10 - 100 / 50 * 7),
                            (180 - 100 / 50 * 3, -10 - 100 / 50 * 6),
                            (180 - 100 / 50 * 4, -10 - 100 / 50 * 4),
                            (180 - 100 / 50 * 7, -10 - 100 / 50 * 1),
                            (180 - 100 / 50 * 10, -10 - 100 / 50 * 2),
                            (180 - 100 / 50 * 9, -10 - 100 / 50 * 1),
                            (180 - 100 / 50 * 9, -10 - 100 / 50 * 4),
                            ))
        pygame.draw.rect(surface, color_stem, pygame.Rect(478, 154, 4, 20), border_radius=1)
        pygame.draw.circle(surface, color_apple, (480, 202), 32)
        pygame.draw.ellipse(surface, color_leaf, pygame.Rect(486, 150, 20, 12))
        pygame.draw.rect(surface, color_leaf_middle, pygame.Rect(490, 154, 12, 2))
        pygame.draw.polygon(surface, color_highlight_apple,
                            ((480 - 100 / 50 * 7, 190 - 100 / 50 * 6),
                             (480 - 100 / 50 * 5, 190 - 100 / 50 * 7),
                             (480 - 100 / 50 * 3, 190 - 100 / 50 * 6),
                             (480 - 100 / 50 * 4, 190 - 100 / 50 * 4),
                             (480 - 100 / 50 * 7, 190 - 100 / 50 * 1),
                             (480 - 100 / 50 * 10, 190 - 100 / 50 * 2),
                             (480 - 100 / 50 * 9, 190 - 100 / 50 * 1),
                             (480 - 100 / 50 * 9, 190 - 100 / 50 * 4),
                             ))
        pygame.draw.rect(surface, color_stem, pygame.Rect(778, 454, 4, 20), border_radius=1)
        pygame.draw.circle(surface, color_apple, (780, 502), 32)
        pygame.draw.ellipse(surface, color_leaf, pygame.Rect(786, 450, 20, 12))
        pygame.draw.rect(surface, color_leaf_middle, pygame.Rect(790, 454, 12, 2))
        pygame.draw.polygon(surface, color_highlight_apple,
                            ((780 - 100 / 50 * 7, 490 - 100 / 50 * 6),
                             (780 - 100 / 50 * 5, 490 - 100 / 50 * 7),
                             (780 - 100 / 50 * 3, 490 - 100 / 50 * 6),
                             (780 - 100 / 50 * 4, 490 - 100 / 50 * 4),
                             (780 - 100 / 50 * 7, 490 - 100 / 50 * 1),
                             (780 - 100 / 50 * 10, 490 - 100 / 50 * 2),
                             (780 - 100 / 50 * 9, 490 - 100 / 50 * 1),
                             (780 - 100 / 50 * 9, 490 - 100 / 50 * 4),
                             ))

        # background quirks
        pygame.draw.rect(surface, (10, 120, 160), pygame.Rect(41, 131, 350, 190), border_radius=20)
        pygame.draw.rect(surface, (30, 130, 180), pygame.Rect(40, 130, 350, 190), border_radius=20)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(56, 51, 350, 100), border_radius=8)
        pygame.draw.rect(surface, (70, 165, 210), pygame.Rect(55, 50, 350, 100), border_radius=8)
        pygame.draw.rect(surface, (7, 111, 151), pygame.Rect(151, 336, 550, 466), border_top_left_radius=8,
                         border_top_right_radius=8)
        pygame.draw.rect(surface, (27, 131, 171), pygame.Rect(150, 335, 550, 466), border_top_left_radius=8,
                         border_top_right_radius=8)
        pygame.draw.rect(surface, (27, 131, 171), pygame.Rect(1, 671, 851, 131), border_top_left_radius=8,
                         border_top_right_radius=8)
        pygame.draw.rect(surface, (47, 151, 191), pygame.Rect(0, 670, 851, 131), border_top_left_radius=8,
                         border_top_right_radius=8)
        pygame.draw.rect(surface, (70, 160, 190), pygame.Rect(621, 659, 220, 131), border_radius=8)
        pygame.draw.rect(surface, (90, 180, 210), pygame.Rect(620, 658, 220, 131), border_radius=8)

        # main logo
        surface.blit(mainFont.render("Welcome to:", True, raisinBlack), (60, 80))
        for i in range(1, 5):
            surface.blit(snekFont.render("snek!", True, (155, 120, 155)), (70 + i, 170 + i))
        surface.blit(snekFont.render("snek!", True, (255, 220, 255)), (70, 170))

        # draw main screen snake body + sclera
        pygame.draw.circle(surface, snakeColor, (30, 440), 100, draw_top_right=True, width=100)
        pygame.draw.rect(surface, snakeColor, pygame.Rect(0, 340, 30, 100))
        pygame.draw.rect(surface, snakeColor, pygame.Rect(30, 440, 100, 160), border_bottom_left_radius=50,
                         border_bottom_right_radius=50)

        pygame.draw.circle(surface, white, ((30) + int(100 / 50 * 35),
                                            (538) + int(100 / 50 * 15)),
                           int(100 / 50 * 10))
        pygame.draw.circle(surface, white, ((30) + int(100 / 50 * 15),
                                            (538) + int(100 / 50 * 15)),
                           int(100 / 50 * 10))

        pygame.draw.circle(surface, snakeColor, (841, 330), 110, draw_bottom_left=True, width=100)
        pygame.draw.rect(surface, snakeColor, pygame.Rect(841, 340, 20, 100))
        pygame.draw.rect(surface, snakeColor, pygame.Rect(731, 140, 100, 190))
        pygame.draw.circle(surface, snakeColor, (731, 140), 100, draw_top_right=True, width=100)
        pygame.draw.rect(surface, snakeColor, pygame.Rect(631, 40, 100, 100))
        pygame.draw.circle(surface, snakeColor, (631, 40), 100, draw_bottom_left=True, width=100)
        pygame.draw.rect(surface, snakeColor, pygame.Rect(531, 0, 100, 40))


        # draw iris in the direction of mouse (+ distance)
        if (pygame.mouse.get_focused()):
            mouse = pygame.mouse.get_pos()
        else:
            mouse = [480, 190]
        middle_point = [100, 568]
        direction_mouse = mouse - Vector2(middle_point[0], middle_point[1])
        radius, angle = direction_mouse.as_polar()
        angle_rad = math.radians(angle + 90)
        point = [middle_point[0] + (10 / 1000 * radius + 4) * math.sin(angle_rad),
                 middle_point[1] - (10 / 1000 * radius + 4) * math.cos(angle_rad)]

        pygame.draw.circle(surface, black, (point[0], point[1]), 7)

        middle_point = [60, 568]
        direction_mouse = mouse - Vector2(middle_point[0], middle_point[1])
        radius, angle = direction_mouse.as_polar()
        angle_rad = math.radians(angle + 90)
        point = [middle_point[0] + (10 / 1000 * radius + 4) * math.sin(angle_rad),
                 middle_point[1] - (10 / 1000 * radius + 4) * math.cos(angle_rad)]

        pygame.draw.circle(surface, black, (point[0], point[1]), 7)

        # leaderboard
        drawLeaderboard()

        # input box
        pygame.draw.rect(surface, buttonColor, pygame.Rect(185, 700, 400, 50), border_radius=10)
        pygame.draw.rect(surface, white, pygame.Rect(188, 703, 394, 44), border_radius=10)

        # play button clicked
        if username_done:
            # checks if username is valid + saves username / displays message in input box
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

            # draws options button
            pygame.draw.rect(surface, buttonShadow, pygame.Rect(650, 700, 160, 50), border_radius=10)
            pygame.draw.rect(surface, buttonColor, pygame.Rect(646, 696, 160, 50), border_radius=10)
            optionsButtonFont = pygame.font.Font(None, 52)
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))

            # moves button down
            pygame.draw.rect(surface, buttonColor, pygame.Rect(80, 700, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Play", True, white), (90, 708))
            pygame.display.flip()
            time.sleep(0.3)

            # moves button up
            pygame.draw.rect(surface, buttonShadow, pygame.Rect(80, 700, 95, 50), border_radius=10)
            pygame.draw.rect(surface, buttonColor, pygame.Rect(76, 696, 95, 50), border_radius=10)
            play_font = pygame.font.Font(None, 52)
            surface.blit(play_font.render("Play", True, white), (89, 707))
            pygame.display.flip()
            time.sleep(0.1)

            if username != "":
                run = True
                return
            else:
                username_done = False

        # draws button
        pygame.draw.rect(surface, buttonShadow, pygame.Rect(80, 700, 95, 50), border_radius=10)
        pygame.draw.rect(surface, buttonColor, pygame.Rect(76, 696, 95, 50), border_radius=10)
        play_font = pygame.font.Font(None, 52)

        # highlights button
        if highlight_play_button:
            surface.blit(play_font.render("Play", True, highlight), (89, 707))
        else:
            surface.blit(play_font.render("Play", True, white), (89, 707))

        # checks if buttons should be highlighted / were pressed pressed
        mouse = pygame.mouse.get_pos()
        if playBox.collidepoint(mouse):
            highlight_play_button = True
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    username_done = True
                if event.type == pygame.QUIT:
                    pygame.quit()
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

        # input box -> https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if input_box.collidepoint(mouse) and not active:
            color = highlight
        else:
            color = color_active if active else color_inactive

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
                        if event.unicode.lower() in letterWhitelist:
                            username += event.unicode
                        elif event.key != pygame.K_LSHIFT and event.key != pygame.K_RSHIFT:
                            surface.fill((255, 0, 0))
                            pygame.display.flip()
                            time.sleep(0.02)
        if username == "" and not active:
            username_input_color = (200, 200, 200)
            txt_surface = font2.render("Username", True, username_input_color)
        else:
            username_input_color = raisinBlack
            txt_surface = font2.render(username, True, username_input_color)
        input_box.w = 400
        surface.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
        pygame.draw.rect(surface, color, input_box, 4, border_radius=10)

        # options button
        if options_button_clicked:
            # moves button down
            pygame.draw.rect(surface, buttonColor, pygame.Rect(650, 700, 160, 50), border_radius=10)
            play_font = pygame.font.Font(None, 50)
            surface.blit(play_font.render("Options", True, white), (660, 707))
            pygame.display.flip()
            time.sleep(0.3)

            # moves button up
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

        # highlights button
        if highlight_options_button:
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))
        else:
            surface.blit(optionsButtonFont.render("Options", True, white), (659, 707))

        pygame.display.flip()


def resetBackground():
    global highlight_quit_button, quit_button_clicked, run

    # grid
    surface.fill(backgroundColor)
    if playingFieldSize[chosenPlayingFieldSize] == "17x15":
        for i in range(1, 18):
            for j in range(16):
                if i % 2 == 0 or i == 0:
                    if j % 2 == 0 or j == 0:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 50) - 50, (j * 50) + 50, 50, 50))
                else:
                    if j % 2 == 1:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 50) - 50, (j * 50) + 50, 50, 50))
        pygame.draw.line(surface, darkerBackgroundColor, (0, 49), (851, 49), width=2)

    elif playingFieldSize[chosenPlayingFieldSize] == "10x8":
        for i in range(1, 11):
            for j in range(9):
                if i % 2 == 0 or i == 0:
                    if j % 2 == 0 or j == 0:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 80) - 55, (j * 80) + 60, 80, 80))
                else:
                    if j % 2 == 1:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 80) - 55, (j * 80) + 60, 80, 80))
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(24, 59, 800, 720), width=2)

    elif playingFieldSize[chosenPlayingFieldSize] == "24x21":
        for i in range(1, 25):
            for j in range(22):
                if i % 2 == 0 or i == 0:
                    if j % 2 == 0 or j == 0:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 33) - 4, (j * 33) + 54, 33, 33))
                else:
                    if j % 2 == 1:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 33) - 4, (j * 33) + 54, 33, 33))
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(28, 53, 792, 726), width=2)

    # score
    pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(1, 1, 200, 48), border_bottom_right_radius=8)
    pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(0, 0, 200, 48), border_bottom_right_radius=8)
    surface.blit(font.render("Score: " + str(score), True, raisinBlack), (10, 10))

    # username
    usernameSurface = font.render(username, True, raisinBlack)
    width = max(0, usernameSurface.get_width() + 10)
    pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(420 - width / 2 - 19, 3, width + 30, 45),
                     border_radius=8)
    pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(420 - width / 2 - 20, 2, width + 30, 45),
                     border_radius=8)

    surface.blit(usernameSurface, (420 - width / 2, 10))
    # quit button
    if quit_button_clicked:
        drawSnake()
        drawApple()
        pygame.draw.rect(surface, buttonColor, quitBoxShadow, border_radius=10)
        quit_font = pygame.font.Font(None, 40)
        surface.blit(quit_font.render("Quit", True, white), (768, 15))
        pygame.display.flip()
        time.sleep(0.3)

        # moves button up
        pygame.draw.rect(surface, buttonShadow, quitBoxShadow, border_radius=10)
        pygame.draw.rect(surface, buttonColor, quitBox, border_radius=10)
        quit_font = pygame.font.Font(None, 42)
        surface.blit(quit_font.render("Quit", True, white), (765, 12))
        pygame.display.flip()
        time.sleep(0.1)

        quit_button_clicked = False
        run = False
        doHannahBaker()

    pygame.draw.rect(surface, buttonShadow, quitBoxShadow, border_radius=10)
    pygame.draw.rect(surface, buttonColor, quitBox, border_radius=10)
    quit_font = pygame.font.Font(None, 42)

    if highlight_quit_button:
        surface.blit(quit_font.render("Quit", True, highlight), (765, 12))
    else:
        surface.blit(quit_font.render("Quit", True, white), (765, 12))


def resetOptionsScreen():
    global chosenNumberOfApples, chosenSpeed, chosenPlayingFieldSize, chosenSelfCollisions, chosenWallCollisions
    back_button_clicked = False
    highlight_back_button = False
    while True:
        surface.fill(backgroundColor)
        #grid
        for i in range(1, 18):
            for j in range(16):
                if i % 2 == 0 or i == 0:
                    if j % 2 == 0 or j == 0:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 100) - 170, (j * 100)-60, 100, 100))
                else:
                    if j % 2 == 1:
                        pygame.draw.rect(surface, darkerBackgroundColor,
                                         pygame.Rect((i * 100) - 170, (j * 100)-60, 100, 100))
        # background quirks
        pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(31, 77, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(30, 76, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(31, 227, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(30, 226, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(31, 377, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(30, 376, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(31, 527, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(30, 526, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (30, 125, 170), pygame.Rect(31, 677, 750, 100), border_radius=8)
        pygame.draw.rect(surface, (50, 145, 190), pygame.Rect(30, 676, 750, 100), border_radius=8)

        # SETTINGS
        # settings
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(oBox1), border_radius=15)
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(oBox2), border_radius=15)
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(oBox3), border_radius=15)
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(oBox4), border_radius=15)
        pygame.draw.rect(surface, darkerBackgroundColor, pygame.Rect(oBox5), border_radius=15)

        mouse = pygame.mouse.get_pos()
        # number of apples
        surface.blit(optionsTitleFont.render("Number of apples", True, raisinBlack), (60, 108))
        if oBox1.collidepoint(mouse):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: chosenNumberOfApples = min(chosenNumberOfApples + 1, len(numberOfApples) - 1)
                    if event.button == 5: chosenNumberOfApples = max(chosenNumberOfApples - 1, 0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenNumberOfApples = min(chosenNumberOfApples + 1, len(numberOfApples) - 1)
                    if event.key == pygame.K_DOWN:
                        chosenNumberOfApples = max(chosenNumberOfApples - 1, 0)
        chosenNumberOfApplesRender = optionsFont.render(numberOfApples[chosenNumberOfApples], True,
                                                        raisinBlack if numberOfApples[
                                                                           chosenNumberOfApples] == "1" else white)
        widthNumberOfApplesRender = chosenNumberOfApplesRender.get_width()
        surface.blit(chosenNumberOfApplesRender, (600 - widthNumberOfApplesRender / 2, 113))

        for i in range(len(numberOfApples)):
            if chosenNumberOfApples == i:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(495 + i * 210 / len(numberOfApples), 154, 200 / len(numberOfApples), 10),
                                 border_radius=4)
            else:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(500 + i * 210 / len(numberOfApples), 157, 200 / len(numberOfApples) - 10,
                                             5), border_radius=2)

        # speed
        surface.blit(optionsTitleFont.render("Snake speed", True, raisinBlack), (60, 258))
        if oBox2.collidepoint(mouse):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: chosenSpeed = min(chosenSpeed + 1, len(speed) - 1)
                    if event.button == 5: chosenSpeed = max(chosenSpeed - 1, 0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenSpeed = min(chosenSpeed + 1, len(speed) - 1)
                    if event.key == pygame.K_DOWN:
                        chosenSpeed = max(chosenSpeed - 1, 0)
        chosenSpeedRender = optionsFont.render(speed[chosenSpeed], True,
                                               raisinBlack if speed[chosenSpeed] == "default" else white)
        widthSpeedRender = chosenSpeedRender.get_width()
        surface.blit(chosenSpeedRender, (600 - widthSpeedRender / 2, 263))

        for i in range(len(speed)):
            if chosenSpeed == i:
                pygame.draw.rect(surface, white if i != 4 else raisinBlack,
                                 pygame.Rect(495 + i * 210 / len(speed), 304, 200 / len(speed), 10), border_radius=4)
            else:
                pygame.draw.rect(surface, white if i != 4 else raisinBlack,
                                 pygame.Rect(500 + i * 210 / len(speed), 307, 200 / len(speed) - 10, 5),
                                 border_radius=2)

        # playing field size
        surface.blit(optionsTitleFont.render("Playing field size", True, raisinBlack), (60, 408))
        if oBox3.collidepoint(mouse):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: chosenPlayingFieldSize = min(chosenPlayingFieldSize + 1,
                                                                       len(playingFieldSize) - 1)
                    if event.button == 5: chosenPlayingFieldSize = max(chosenPlayingFieldSize - 1, 0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenPlayingFieldSize = min(chosenPlayingFieldSize + 1, len(playingFieldSize) - 1)
                    if event.key == pygame.K_DOWN:
                        chosenPlayingFieldSize = max(chosenPlayingFieldSize - 1, 0)
        chosenPlayingFieldSizeRender = optionsFont.render(playingFieldSize[chosenPlayingFieldSize], True,
                                                          raisinBlack if playingFieldSize[
                                                                             chosenPlayingFieldSize] == "17x15" else white)
        widthPlayingFieldSizeRender = chosenPlayingFieldSizeRender.get_width()
        surface.blit(chosenPlayingFieldSizeRender, (600 - widthPlayingFieldSizeRender / 2, 413))

        for i in range(len(playingFieldSize)):
            if chosenPlayingFieldSize == i:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(495 + i * 210 / len(playingFieldSize), 454, 200 / len(playingFieldSize),
                                             10), border_radius=4)
            else:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(500 + i * 210 / len(playingFieldSize), 457,
                                             200 / len(playingFieldSize) - 10, 5), border_radius=2)

        # collisions with self
        surface.blit(optionsTitleFont.render("Body collisions", True, raisinBlack), (60, 558))
        if oBox4.collidepoint(mouse):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: chosenSelfCollisions = True
                    if event.button == 5: chosenSelfCollisions = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenSelfCollisions = True
                    if event.key == pygame.K_DOWN:
                        chosenSelfCollisions = False
        chosenSelfCollisionsRender = optionsFont.render("True" if chosenSelfCollisions else "False", True,
                                                        raisinBlack if chosenSelfCollisions else white)
        widthChosenSelfCollionsRender = chosenSelfCollisionsRender.get_width()
        surface.blit(chosenSelfCollisionsRender, (600 - widthChosenSelfCollionsRender / 2, 563))

        for i in range(2):
            if chosenSelfCollisions == i:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(495 + i * 210 / 2, 604, 200 / 2, 10), border_radius=4)
            else:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(500 + i * 210 / 2, 607, 200 / 2 - 10, 5), border_radius=2)

        # collisions with wall
        surface.blit(optionsTitleFont.render("Wall collisions", True, raisinBlack), (60, 708))
        if oBox5.collidepoint(mouse):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: chosenWallCollisions = True
                    if event.button == 5: chosenWallCollisions = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        chosenWallCollisions = True
                    if event.key == pygame.K_DOWM:
                        chosenWallCollisions = False
        chosenWallCollisionsRender = optionsFont.render("True" if chosenWallCollisions else "False", True,
                                                        raisinBlack if chosenWallCollisions else white)
        widthChosenWallCollionsRender = chosenWallCollisionsRender.get_width()
        surface.blit(chosenWallCollisionsRender, (600 - widthChosenWallCollionsRender / 2, 713))

        for i in range(2):
            if chosenWallCollisions == i:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(495 + i * 210 / 2, 754, 200 / 2, 10), border_radius=4)
            else:
                pygame.draw.rect(surface, white if i != 1 else raisinBlack,
                                 pygame.Rect(500 + i * 210 / 2, 757, 200 / 2 - 10, 5), border_radius=2)

        # top menu
        pygame.draw.rect(surface, buttonShadow, pygame.Rect(0, 5, 140, 50),
                         border_bottom_right_radius=5, border_top_right_radius=5)
        pygame.draw.rect(surface, buttonColor, pygame.Rect(0, 1, 135, 50),
                         border_bottom_right_radius=5, border_top_right_radius=5)
        surface.blit(optionsFont.render("Options", True, white), (10, 13))

        if back_button_clicked:
            pygame.draw.rect(surface, buttonColor, backBoxShadow, border_radius=10)
            back_font = pygame.font.Font(None, 40)
            surface.blit(back_font.render("Back", True, white), (768, 15))
            pygame.display.flip()
            time.sleep(0.3)

            # moves button up
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
                if event.type == pygame.QUIT:
                    pygame.quit()
        else:
            highlight_back_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    chosenNumberOfApples = defaultChosenNumberOfApples
                    chosenSpeed = defaultChosenSpeed
                    chosenPlayingFieldSize = defaultChosenPlayingFieldSize
                    chosenSelfCollisions = True
                    chosenWallCollisions = True

        pygame.display.flip()


def showScore():

    startTime = time.time()
    beam1 = SunBeams(0)
    beam2 = SunBeams(18)
    beam3 = SunBeams(36)
    beam4 = SunBeams(54)
    beam5 = SunBeams(72)
    beam6 = SunBeams(90)
    beam7 = SunBeams(108)
    beam8 = SunBeams(126)
    beam9 = SunBeams(144)
    beam10 = SunBeams(162)
    beam11 = SunBeams(180)
    beam12 = SunBeams(198)
    beam13 = SunBeams(216)
    beam14 = SunBeams(234)
    beam15 = SunBeams(252)
    beam16 = SunBeams(270)
    beam17 = SunBeams(288)
    beam18 = SunBeams(306)
    beam19 = SunBeams(324)
    beam20 = SunBeams(342)
    cloud1 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud2 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud3 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud4 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud5 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud6 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud7 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud8 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud9 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud10 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud11 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud12 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud13 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud14 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud15 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud16 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud17 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud18 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud19 = Clouds([random.randint(-100, 851), random.randint(0, 400)])
    cloud20 = Clouds([random.randint(-100, 851), random.randint(0, 400)])

    while True:
        surface.fill(backgroundColor)
        #background
        pygame.draw.circle(surface, "#ffff00", (172, 125), 85)
        cloud1.move()
        cloud2.move()
        cloud3.move()
        cloud4.move()
        cloud5.move()
        cloud6.move()
        cloud7.move()
        cloud8.move()
        cloud9.move()
        cloud10.move()
        cloud11.move()
        cloud12.move()
        cloud13.move()
        cloud14.move()
        cloud15.move()
        cloud16.move()
        cloud17.move()
        cloud18.move()
        cloud19.move()
        cloud20.move()
        beam1.rotate()
        beam2.rotate()
        beam3.rotate()
        beam4.rotate()
        beam5.rotate()
        beam6.rotate()
        beam7.rotate()
        beam8.rotate()
        beam9.rotate()
        beam10.rotate()
        beam11.rotate()
        beam12.rotate()
        beam13.rotate()
        beam14.rotate()
        beam15.rotate()
        beam16.rotate()
        beam17.rotate()
        beam18.rotate()
        beam19.rotate()
        beam20.rotate()
        pygame.draw.rect(surface, "#008013", pygame.Rect(0, 501, 851, 300))

        #grave
        for i in range(15):
            pygame.draw.rect(surface, darkStoneGrey, pygame.Rect(251+i, 200-(i/15*10), 300, 400), border_radius=15, border_top_left_radius=150, border_top_right_radius=150)
        pygame.draw.rect(surface, stoneGrey, pygame.Rect(250, 200, 300, 400), border_radius=15, border_top_left_radius=150, border_top_right_radius=150)
        surface.blit(pygame.font.Font(None, 100).render("RIP", True, (50, 50, 50)), (340, 280))
        pygame.draw.line(surface, (50, 50, 50), (290, 350), (510, 350), width=3)
        surface.blit(pygame.font.Font(None, 70).render("Score:", True, (50, 50, 50)), (330, 450))
        x = 100
        while True:
            usernameText = pygame.font.Font(None, x).render(username, True, (50, 50, 50))
            if usernameText.get_width() < 250:
                break
            else:
                x -= 10
        surface.blit(usernameText, (400-(usernameText.get_width()/2), 365+(100-x)/4))
        scoreText = pygame.font.Font(None, 60).render(str(score), True, (50, 50, 50))
        widthScoreText = scoreText.get_width()
        surface.blit(scoreText, (400-(widthScoreText/2), 520))
        surface.blit(pygame.transform.scale(skull, (50, 50)), (375, 220))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (580, 500))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (680, 500))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (780, 500))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (120, 500))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (20, 500))
        surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (-80, 500))
        for i in range(10):
            surface.blit(pygame.transform.scale(flowers, (int(100*1.174), 100)), (-80+i*100, 620))
        surface.blit(pygame.transform.scale(caet, (100, 100)), (500, 520))

        # checks if timer is done or if keys are pressed
        elapsedTime = time.time() - startTime
        if elapsedTime > 3:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return

        # loading snake
        pygame.draw.rect(surface, snakeColor, pygame.Rect(0, 751, (851 / 3) * elapsedTime, 50))
        pygame.draw.rect(surface, snakeColor, pygame.Rect((851 / 3) * elapsedTime, 751, 50, 50),
                         border_top_right_radius=25, border_bottom_right_radius=25)
        pygame.draw.circle(surface, white, (((851 / 3) * elapsedTime) + 35, 751 + 15), 8)
        pygame.draw.circle(surface, white, (((851 / 3) * elapsedTime) + 35, 751 + 35), 8)
        pygame.draw.circle(surface, black, (((851 / 3) * elapsedTime) + 37, 751 + 15), 4)
        pygame.draw.circle(surface, black, (((851 / 3) * elapsedTime) + 37, 751 + 35), 4)

        # random cat
        surface.blit(pygame.transform.scale(caet2, (100, 100)), (-10, 701))

        pygame.display.flip()


def drawSnake():
    global snakeGirth, correctionX, correctionY, snakeTailX, snakeTailY, snakeHeadX, snakeHeadY, oldX, oldY, nearestAppleDistance, applesX, applesY

    for i in reversed(range(len(snakeTailX))):
        temp_x = snakeTailX[i]
        temp_y = snakeTailY[i]

        # define color
        if i < 50:
            snakeTailColor = (255, 161, 10 + i * 5)
        elif 50 <= i < 102:
            snakeTailColor = (255 - (i - 50) * 5, 161, 255)
        elif 102 <= i < 134:
            snakeTailColor = (0, 160 - (i - 102) * 5, 255)
        elif 134 <= i < 186:
            snakeTailColor = (0 + (i - 134) * 5, 1, 255)
        elif 186 <= i < 238:
            snakeTailColor = (255, 0 + (i - 186) * 5, 255)
        elif 238 <= i < 250:
            snakeTailColor = (255, 255, 255)
        else:
            snakeTailColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # define thickness for curved parts of body
        snakeCurveRadius = snakeGirth - ((snakeGirth / 3 * 2) / ((borderX + 1) * borderY) * i)
        snakeThickness = int(snakeGirth - 2 * ((snakeGirth / 3 * 2) / ((borderX + 1) * borderY) * i))
        if snakeThickness < snakeGirth / 3:
            snakeCurveRadius = snakeGirth / 3 * 2
            snakeThickness = int(snakeGirth / 3)

        # draws body with curves if necessary
        if i == 0:  # first body part (after head)
            if (snakeHeadX == snakeTailX[i] + 1 or (snakeHeadX == 0 and snakeTailX[i] == borderX)) and snakeHeadY == \
                    snakeTailY[i] and (
                    snakeTailY[i] + 1 == snakeTailY[i + 1] or (snakeTailY[i] == borderY and snakeTailY[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_left=True)
            elif (snakeHeadX + 1 == snakeTailX[i] or (snakeHeadX == borderX and snakeTailX[i] == 0)) and snakeHeadY == \
                    snakeTailY[i] and (
                    snakeTailY[i] + 1 == snakeTailY[i + 1] or (snakeTailY[i] == borderY and snakeTailY[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_right=True)
            elif snakeHeadX == snakeTailX[i] and (
                    snakeHeadY == snakeTailY[i] + 1 or (snakeHeadY == 0 and snakeTailY[i] == borderY)) and (
                    snakeTailX[i] == snakeTailX[i + 1] + 1 or (snakeTailX[i] == 0 and snakeTailX[i + 1] == borderX)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_right=True)
            elif snakeHeadX == snakeTailX[i] and (
                    snakeHeadY + 1 == snakeTailY[i] or (snakeHeadY == borderY and snakeTailY[i] == 0)) and (
                    snakeTailX[i] == snakeTailX[i + 1] + 1 or (snakeTailX[i] == 0 and snakeTailX[i + 1] == borderX)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_right=True)
            elif snakeHeadX == snakeTailX[i] and (
                    snakeHeadY == snakeTailY[i] + 1 or (snakeHeadY == 0 and snakeTailY[i] == borderY)) and (
                    snakeTailX[i] + 1 == snakeTailX[i + 1] or (snakeTailX[i] == borderX and snakeTailX[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_left=True)
            elif snakeHeadX == snakeTailX[i] and (
                    snakeHeadY + 1 == snakeTailY[i] or (snakeHeadY == borderY and snakeTailY[i] == 0)) and (
                    snakeTailX[i] + 1 == snakeTailX[i + 1] or (snakeTailX[i] == borderX and snakeTailX[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_left=True)
            elif (snakeHeadX + 1 == snakeTailX[i] or (snakeHeadX == borderX and snakeTailX[i] == 0)) and snakeHeadY == \
                    snakeTailY[i] and (
                    snakeTailY[i] == snakeTailY[i + 1] + 1 or (snakeTailY[i] == 0 and snakeTailY[i + 1] == borderY)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_right=True)
            elif (snakeHeadX == snakeTailX[i] + 1 or (snakeHeadX == 0 and snakeTailX[i] == borderX)) and snakeHeadY == \
                    snakeTailY[i] and (
                    snakeTailY[i] == snakeTailY[i + 1] + 1 or (snakeTailY[i] == 0 and snakeTailY[i + 1] == borderY)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_left=True)
            else:
                pygame.draw.rect(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY), snakeGirth, snakeGirth))

        elif 0 < i < (len(snakeTailX) - 1):  # rest of body except last part (tail)
            if (snakeTailX[i - 1] == snakeTailX[i] + 1 or (snakeTailX[i - 1] == 0 and snakeTailX[i] == borderX)) and \
                    snakeTailY[i - 1] == snakeTailY[i] and (
                    snakeTailY[i] + 1 == snakeTailY[i + 1] or (snakeTailY[i] == borderY and snakeTailY[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_left=True)

            elif (snakeTailX[i - 1] + 1 == snakeTailX[i] or (snakeTailX[i - 1] == borderX and snakeTailX[i] == 0)) and \
                    snakeTailY[i - 1] == snakeTailY[i] and (
                    snakeTailY[i] + 1 == snakeTailY[i + 1] or (snakeTailY[i] == borderY and snakeTailY[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_right=True)

            elif snakeTailX[i - 1] == snakeTailX[i] and (snakeTailY[i - 1] == snakeTailY[i] + 1 or (
                    snakeTailY[i - 1] == 0 and snakeTailY[i] == borderY)) and (
                    snakeTailX[i] == snakeTailX[i + 1] + 1 or (snakeTailX[i] == 0 and snakeTailX[i + 1] == borderX)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_right=True)
            elif snakeTailX[i - 1] == snakeTailX[i] and (snakeTailY[i - 1] + 1 == snakeTailY[i] or (
                    snakeTailY[i - 1] == borderY and snakeTailY[i] == 0)) and (
                    snakeTailX[i] == snakeTailX[i + 1] + 1 or (snakeTailX[i] == 0 and snakeTailX[i + 1] == borderX)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_right=True)
            elif snakeTailX[i - 1] == snakeTailX[i] and (snakeTailY[i - 1] == snakeTailY[i] + 1 or (
                    snakeTailY[i - 1] == 0 and snakeTailY[i] == borderY)) and (
                    snakeTailX[i] + 1 == snakeTailX[i + 1] or (snakeTailX[i] == borderX and snakeTailX[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY + snakeGirth)),
                                   snakeCurveRadius, snakeThickness, draw_top_left=True)
            elif snakeTailX[i - 1] == snakeTailX[i] and (snakeTailY[i - 1] + 1 == snakeTailY[i] or (
                    snakeTailY[i - 1] == borderY and snakeTailY[i] == 0)) and (
                    snakeTailX[i] + 1 == snakeTailX[i + 1] or (snakeTailX[i] == borderX and snakeTailX[i + 1] == 0)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_left=True)
            elif (snakeTailX[i - 1] + 1 == snakeTailX[i] or (snakeTailX[i - 1] == borderX and snakeTailX[i] == 0)) and \
                    snakeTailY[i - 1] == snakeTailY[i] and (
                    snakeTailY[i] == snakeTailY[i + 1] + 1 or (snakeTailY[i] == 0 and snakeTailY[i + 1] == borderY)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_right=True)
            elif (snakeTailX[i - 1] == snakeTailX[i] + 1 or (snakeTailX[i - 1] == 0 and snakeTailX[i] == borderX)) and \
                    snakeTailY[i - 1] == snakeTailY[i] and (
                    snakeTailY[i] == snakeTailY[i + 1] + 1 or (snakeTailY[i] == 0 and snakeTailY[i + 1] == borderY)):
                pygame.draw.circle(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth), (temp_y * snakeGirth + correctionY)),
                                   snakeCurveRadius, snakeThickness, draw_bottom_left=True)
            else:
                if snakeTailX[i - 1] == snakeTailX[i] == snakeTailX[i + 1]:
                    pygame.draw.rect(surface, snakeTailColor, (
                        (temp_x * snakeGirth + correctionX + (snakeGirth - snakeThickness) / 2),
                        (temp_y * snakeGirth + correctionY), snakeThickness,
                        snakeGirth))
                if snakeTailY[i - 1] == snakeTailY[i] == snakeTailY[i + 1]:
                    pygame.draw.rect(surface, snakeTailColor, (
                        (temp_x * snakeGirth + correctionX),
                        (temp_y * snakeGirth + correctionY + (snakeGirth - snakeThickness) / 2), snakeGirth,
                        snakeThickness))

        else:  # draw tail (last part of body)
            if (snakeTailX[i - 1] + 1 == snakeTailX[i] or (snakeTailX[i - 1] == borderX and snakeTailX[i] == 0)) and \
                    snakeTailY[i - 1] == snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX),
                    (temp_y * snakeGirth + correctionY + (snakeGirth - snakeThickness) / 2), int(snakeGirth / 2),
                    snakeThickness),
                                 border_top_right_radius=int(snakeGirth / 5 * 2),
                                 border_bottom_right_radius=int(snakeGirth / 5 * 2))
            elif (snakeTailX[i - 1] == snakeTailX[i] + 1 or (snakeTailX[i - 1] == 0 and snakeTailX[i] == borderX)) and \
                    snakeTailY[i - 1] == snakeTailY[i]:
                pygame.draw.rect(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + snakeGirth / 2),
                    (temp_y * snakeGirth + correctionY + (snakeGirth - snakeThickness) / 2), int(snakeGirth / 2) + 1,
                    snakeThickness),
                                 border_top_left_radius=int(snakeGirth / 5 * 2),
                                 border_bottom_left_radius=int(snakeGirth / 5 * 2))
            elif snakeTailX[i - 1] == snakeTailX[i] and (
                    snakeTailY[i - 1] + 1 == snakeTailY[i] or (snakeTailY[i - 1] == borderY and snakeTailY[i] == 0)):
                pygame.draw.rect(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + (snakeGirth - snakeThickness) / 2),
                    (temp_y * snakeGirth + correctionY), snakeThickness, int(snakeGirth / 2)),
                                 border_bottom_left_radius=int(snakeGirth / 5 * 2),
                                 border_bottom_right_radius=int(snakeGirth / 5 * 2))
            elif snakeTailX[i - 1] == snakeTailX[i] and (
                    snakeTailY[i - 1] == snakeTailY[i] + 1 or (snakeTailY[i - 1] == 0 and snakeTailY[i] == borderY)):
                pygame.draw.rect(surface, snakeTailColor, (
                    (temp_x * snakeGirth + correctionX + (snakeGirth - snakeThickness) / 2),
                    (temp_y * snakeGirth + correctionY + snakeGirth / 2), snakeThickness, int(snakeGirth / 2) + 1),
                                 border_top_left_radius=int(snakeGirth / 5 * 2),
                                 border_top_right_radius=int(snakeGirth / 5 * 2))

    # draws head with curves if necessary
    body_comes_from_bottom = True if snakeHeadX == snakeTailX[0] and (
            snakeHeadY + 1 == snakeTailY[0] or (snakeHeadY == borderY and snakeTailY[0] == 0)) else False
    body_comes_from_top = True if snakeHeadX == snakeTailX[0] and (
            snakeHeadY == snakeTailY[0] + 1 or (snakeHeadY == 0 and snakeTailY[0] == borderY)) else False
    body_comes_from_left = True if (snakeHeadX == snakeTailX[0] + 1 or (
            snakeHeadX == 0 and snakeTailX[0] == borderX)) and snakeHeadY == snakeTailY[0] else False
    body_comes_from_right = True if (snakeHeadX + 1 == snakeTailX[0] or (
            snakeHeadX == borderX and snakeTailX[0] == 0)) and snakeHeadY == snakeTailY[0] else False

    # draw head and sclera
    if direction == "right":
        if body_comes_from_bottom:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_right_radius=int(snakeGirth / 2), border_top_left_radius=int(snakeGirth / 5))
        elif body_comes_from_top:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_bottom_right_radius=int(snakeGirth / 2),
                             border_bottom_left_radius=int(snakeGirth / 5))
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_right_radius=int(snakeGirth / 2),
                             border_bottom_right_radius=int(snakeGirth / 2))

        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)),
                           int(snakeGirth / 50 * 10))
        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)),
                           int(snakeGirth / 50 * 10))

        middlePoint1 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)]
        middlePoint2 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)]

    elif direction == "left":
        if body_comes_from_bottom:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_left_radius=int(snakeGirth / 2), border_top_right_radius=int(snakeGirth / 5))
        elif body_comes_from_top:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_bottom_left_radius=int(snakeGirth / 2),
                             border_bottom_right_radius=int(snakeGirth / 5))
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_left_radius=int(snakeGirth / 2), border_bottom_left_radius=int(snakeGirth / 2))

        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)),
                           int(snakeGirth / 50 * 10))
        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)),
                           int(snakeGirth / 50 * 10))

        middlePoint1 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)]
        middlePoint2 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)]

    elif direction == "up":
        if body_comes_from_left:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_right_radius=int(snakeGirth / 2),
                             border_bottom_right_radius=int(snakeGirth / 5))
        elif body_comes_from_right:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_left_radius=int(snakeGirth / 2), border_bottom_left_radius=int(snakeGirth / 5))
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_top_right_radius=int(snakeGirth / 2), border_top_left_radius=int(snakeGirth / 2))

        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)),
                           int(snakeGirth / 50 * 10))
        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)),
                           int(snakeGirth / 50 * 10))

        middlePoint1 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)]
        middlePoint2 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 15)]


    elif direction == "down":
        if body_comes_from_left:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_bottom_right_radius=int(snakeGirth / 2),
                             border_top_right_radius=int(snakeGirth / 5))
        elif body_comes_from_right:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_bottom_left_radius=int(snakeGirth / 2), border_top_left_radius=int(snakeGirth / 5))
        else:
            pygame.draw.rect(surface, snakeColor, pygame.Rect((snakeHeadX * snakeGirth + correctionX),
                                                              (snakeHeadY * snakeGirth + correctionY), snakeGirth,
                                                              snakeGirth),
                             border_bottom_right_radius=int(snakeGirth / 2),
                             border_bottom_left_radius=int(snakeGirth / 2))

        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)),
                           int(snakeGirth / 50 * 10))
        pygame.draw.circle(surface, white, ((snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                                            (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)),
                           int(snakeGirth / 50 * 10))

        middlePoint1 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 15),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)]
        middlePoint2 = [(snakeHeadX * snakeGirth + correctionX) + int(snakeGirth / 50 * 35),
                        (snakeHeadY * snakeGirth + correctionY) + int(snakeGirth / 50 * 35)]

    # find distance to apple
    if chosenNumberOfApples != 0:
        xd = snakeHeadX - applesX[0]
        yd = snakeHeadY - applesY[0]
        nearestAppleDistance = math.sqrt(xd * xd + yd * yd)
        nearestAppleIndex = 0
        for i in range(len(applesX)):
            xd = snakeHeadX - applesX[i]
            yd = snakeHeadY - applesY[i]
            distance = math.sqrt(xd * xd + yd * yd)
            if distance < nearestAppleDistance:
                nearestAppleDistance = distance
                nearestAppleIndex = i

        # find direction, angle from eyes to nearest apple
        direction_eyes1 = [(applesX[nearestAppleIndex] * snakeGirth + snakeGirth / 2 + correctionX),
                           (applesY[nearestAppleIndex] * snakeGirth + snakeGirth / 2 + correctionY)] - Vector2(
            middlePoint1[0], middlePoint1[1])
        direction_eyes2 = [(applesX[nearestAppleIndex] * snakeGirth + snakeGirth / 2 + correctionX),
                           (applesY[nearestAppleIndex] * snakeGirth + snakeGirth / 2 + correctionY)] - Vector2(
            middlePoint2[0], middlePoint2[1])

    else:
        direction_eyes1 = pygame.mouse.get_pos() - Vector2(middlePoint1[0], middlePoint1[1])
        direction_eyes2 = pygame.mouse.get_pos() - Vector2(
            middlePoint2[0], middlePoint2[1])

    radius1, angle1 = direction_eyes1.as_polar()
    radius2, angle2 = direction_eyes2.as_polar()
    angle_rad1 = math.radians(angle1 + 90)
    angle_rad2 = math.radians(angle2 + 90)

    # define point looking to nearest apple from each eye and draw the iris
    point1 = [middlePoint1[0] + (snakeGirth / 50 * 5) * math.sin(angle_rad1),
              middlePoint1[1] - (snakeGirth / 50 * 5) * math.cos(angle_rad1)]
    point2 = [middlePoint2[0] + (snakeGirth / 50 * 5) * math.sin(angle_rad2),
              middlePoint2[1] - (snakeGirth / 50 * 5) * math.cos(angle_rad2)]
    pygame.draw.circle(surface, black,
                       (point1[0], point1[1]),
                       int(snakeGirth / 50 * 4))
    pygame.draw.circle(surface, black,
                       (point2[0], point2[1]),
                       int(snakeGirth / 50 * 4))


def drawApple():
    global snakeGirth, correctionX, correctionY
    for i in range(numApplesWanted):
        if applesX[i] != "":
            # apple design
            pygame.draw.rect(surface, color_stem,
                             pygame.Rect((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 1,
                                         (applesY[
                                              i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 18,
                                         snakeGirth / 50 * 2, snakeGirth / 50 * 10),
                             border_radius=1)
            pygame.draw.circle(surface, color_apple, ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX), (
                    applesY[i] * snakeGirth + snakeGirth / 2) + snakeGirth / 50 * 6 + correctionY),
                               snakeGirth / 50 * 16)
            pygame.draw.ellipse(surface, color_leaf,
                                pygame.Rect(
                                    (applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) + snakeGirth / 50 * 3,
                                    (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 20,
                                    snakeGirth / 50 * 10, snakeGirth / 50 * 6))
            pygame.draw.rect(surface, color_leaf_middle,
                             pygame.Rect((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) + snakeGirth / 50 * 5,
                                         (applesY[
                                              i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 18,
                                         snakeGirth / 50 * 6, snakeGirth / 50 * 1))
            pygame.draw.polygon(surface, color_highlight_apple,
                                (((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 7,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 6),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 5,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 7),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 3,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 6),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 4,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 4),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 7,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 1),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 10,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 2),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 9,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 1),
                                 ((applesX[i] * snakeGirth + snakeGirth / 2 + correctionX) - snakeGirth / 50 * 9,
                                  (applesY[i] * snakeGirth + snakeGirth / 2 + correctionY) - snakeGirth / 50 * 4),
                                 ))


def moveSnakeForward():
    global snakeHeadX, snakeHeadY, snakeTailX, snakeTailY, run, elapsedTime, borderX, borderY

    # move body forward
    for i in reversed(range(len(snakeTailX))):
        if i != 0:
            snakeTailX[i] = snakeTailX[i - 1]
            snakeTailY[i] = snakeTailY[i - 1]
        else:
            snakeTailX[i] = snakeHeadX
            snakeTailY[i] = snakeHeadY

    # move head forward
    if direction == "right":
        snakeHeadX += 1
    if direction == "left":
        snakeHeadX -= 1
    if direction == "up":
        snakeHeadY -= 1
    if direction == "down":
        snakeHeadY += 1

    if not chosenWallCollisions:
        if snakeHeadX > borderX:
            snakeHeadX = 0
        elif snakeHeadX < 0:
            snakeHeadX = borderX
        elif snakeHeadY > borderY:
            snakeHeadY = 0
        elif snakeHeadY < 0:
            snakeHeadY = borderY


def doCollisionCheck():
    global run, borderX, borderY

    if chosenWallCollisions:
        if snakeHeadX > borderX:
            return True
        elif snakeHeadX < 0:
            return True
        elif snakeHeadY > borderY:
            return True
        elif snakeHeadY < 0:
            return True
    if chosenSelfCollisions:
        for a in range(0, len(snakeTailX), 1):
            if snakeTailX[a] == snakeHeadX and snakeTailY[a] == snakeHeadY:
                return True
    return False


def drawLeaderboard():
    # fetching usernames and scores by gamemode
    scoresInGamemode = []
    usernamesInGamemode = []
    scoreFile = open("scores.txt", "r")
    scoreFileLines = scoreFile.readlines()
    for lineNum in range(len(scoreFileLines)):
        isUsername = True
        fileUsername = ""
        isChosenNumberOfApples = False
        fileChosenNumberOfApples = ""
        isChosenSpeed = False
        fileChosenSpeed = ""
        isChosenPlayingFieldSize = False
        fileChosenPlayingFieldSize = ""
        isChosenSelfCollisions = False
        fileChosenSelfCollisions = ""
        isChosenWallCollisions = False
        fileChosenWallCollisions = ""
        isScore = False
        fileScore = ""
        if scoreFileLines[lineNum][0] != "#":
            for char in scoreFileLines[lineNum]:
                if isUsername:
                    if char != ";":
                        fileUsername += char
                    else:
                        isUsername = False
                        isChosenNumberOfApples = True
                elif isChosenNumberOfApples:
                    if char != ";":
                        fileChosenNumberOfApples += char
                    else:
                        isChosenNumberOfApples = False
                        isChosenSpeed = True
                elif isChosenSpeed:
                    if char != ";":
                        fileChosenSpeed += char
                    else:
                        isChosenSpeed = False
                        isChosenPlayingFieldSize = True
                elif isChosenPlayingFieldSize:
                    if char != ";":
                        fileChosenPlayingFieldSize += char
                    else:
                        isChosenPlayingFieldSize = False
                        isChosenSelfCollisions = True
                elif isChosenSelfCollisions:
                    if char != ";":
                        fileChosenSelfCollisions += char
                    else:
                        isChosenSelfCollisions = False
                        isChosenWallCollisions = True
                elif isChosenWallCollisions:
                    if char != ";":
                        fileChosenWallCollisions += char
                    else:
                        isChosenWallCollisions = False
                        isScore = True
                elif isScore:
                    if char != "-":
                        fileScore += char
                    else:
                        isScore = False

        if fileChosenNumberOfApples == str(
                chosenNumberOfApples) and fileChosenSpeed == str(
            chosenSpeed) and fileChosenPlayingFieldSize == str(
            chosenPlayingFieldSize) and fileChosenSelfCollisions == str(
            chosenSelfCollisions) and fileChosenWallCollisions == str(chosenWallCollisions):
            scoresInGamemode.append(int(fileScore))
            usernamesInGamemode.append(fileUsername)
    scoreFile.close()

    # sorting scores
    for i in range(len(scoresInGamemode)):
        for j in range(len(scoresInGamemode)):
            if i < j:
                if scoresInGamemode[i] < scoresInGamemode[j]:
                    temp = scoresInGamemode[j]
                    scoresInGamemode[j] = scoresInGamemode[i]
                    scoresInGamemode[i] = temp
                    temp2 = usernamesInGamemode[j]
                    usernamesInGamemode[j] = usernamesInGamemode[i]
                    usernamesInGamemode[i] = temp2

    # menu / display
    surface.blit(font2.render("Top Scores", True, blackCoral), (182, 352))
    surface.blit(font2.render("Top Scores", True, white), (180, 350))
    pygame.draw.rect(surface, blackCoral, pygame.Rect(171, 396, 508, 258), border_radius=10)
    pygame.draw.rect(surface, white, pygame.Rect(175, 400, 500, 250), border_radius=10)

    pygame.draw.line(surface, lightGray, (240, 410), (240, 640), width=2)
    pygame.draw.line(surface, lightGray, (340, 410), (340, 640), width=2)

    surface.blit(leaderboardFont2.render("pos.", True, raisinBlack), (182, 410))
    surface.blit(leaderboardFont2.render("score", True, raisinBlack), (250, 410))
    surface.blit(leaderboardFont2.render("username", True, raisinBlack), (350, 410))

    pygame.draw.line(surface, lightGray, (185, 442), (650, 442), width=2)

    for i in range(min(5, len(scoresInGamemode))):
        surface.blit(leaderboardFont2.render(str(usernamesInGamemode[i]), True,
                                             darkerLogoBackgroundColor if i == 0 else blackCoral), (350, 40 * i + 450))
        surface.blit(leaderboardFont2.render(str(scoresInGamemode[i]), True,
                                             darkerLogoBackgroundColor if i == 0 else blackCoral), (255, 40 * i + 450))
        surface.blit(leaderboardFont2.render(str(i + 1), True, darkerLogoBackgroundColor if i == 0 else blackCoral),
                     (200, 40 * i + 450))

    return


def doHannahBaker():
    showScore()

    # fetch old scores
    scoreFile = open("scores.txt", "r")
    scoreFileLines = scoreFile.readlines()
    playerFound = False
    for lineNum in range(len(scoreFileLines)):
        isUsername = True
        fileUsername = ""
        isChosenNumberOfApples = False
        fileChosenNumberOfApples = ""
        isChosenSpeed = False
        fileChosenSpeed = ""
        isChosenPlayingFieldSize = False
        fileChosenPlayingFieldSize = ""
        isChosenSelfCollisions = False
        fileChosenSelfCollisions = ""
        isChosenWallCollisions = False
        fileChosenWallCollisions = ""
        isScore = False
        fileScore = ""
        if scoreFileLines[lineNum][0] != "#":
            for char in scoreFileLines[lineNum]:
                if isUsername:
                    if char != ";":
                        fileUsername += char
                    else:
                        isUsername = False
                        isChosenNumberOfApples = True
                elif isChosenNumberOfApples:
                    if char != ";":
                        fileChosenNumberOfApples += char
                    else:
                        isChosenNumberOfApples = False
                        isChosenSpeed = True
                elif isChosenSpeed:
                    if char != ";":
                        fileChosenSpeed += char
                    else:
                        isChosenSpeed = False
                        isChosenPlayingFieldSize = True
                elif isChosenPlayingFieldSize:
                    if char != ";":
                        fileChosenPlayingFieldSize += char
                    else:
                        isChosenPlayingFieldSize = False
                        isChosenSelfCollisions = True
                elif isChosenSelfCollisions:
                    if char != ";":
                        fileChosenSelfCollisions += char
                    else:
                        isChosenSelfCollisions = False
                        isChosenWallCollisions = True
                elif isChosenWallCollisions:
                    if char != ";":
                        fileChosenWallCollisions += char
                    else:
                        isChosenWallCollisions = False
                        isScore = True
                elif isScore:
                    if char != "-":
                        fileScore += char
                    else:
                        isScore = False

        # update score if player is registered
        if fileUsername == username and fileChosenNumberOfApples == str(
                chosenNumberOfApples) and fileChosenSpeed == str(
            chosenSpeed) and fileChosenPlayingFieldSize == str(
            chosenPlayingFieldSize) and fileChosenSelfCollisions == str(
            chosenSelfCollisions) and fileChosenWallCollisions == str(chosenWallCollisions):
            playerFound = True
            if fileScore < str(score):
                scoreFileLines[lineNum] = fileUsername + ";" + str(fileChosenNumberOfApples) + ";" + str(
                    chosenSpeed) + ";" + str(chosenPlayingFieldSize) + ";" + str(
                    chosenSelfCollisions) + ";" + str(chosenWallCollisions) + ";" + str(score) + "-"
                with open("scores.txt", "w") as file:
                    file.writelines(scoreFileLines)
    scoreFile.close()

    # write new score if player isn't registered yet
    if not playerFound:
        scoreFile = open("scores.txt", "a")
        scoreFile.write("\n" + username + ";" + str(chosenNumberOfApples) + ";" + str(chosenSpeed) + ";" + str(
            chosenPlayingFieldSize) + ";" + str(chosenSelfCollisions) + ";" + str(
            chosenWallCollisions) + ";" + str(score) + "-")
        scoreFile.close()


# main loop
run = True
while True:
    resetMainScreen()

    # set variables based on playing field size
    if playingFieldSize[chosenPlayingFieldSize] == "10x8":
        borderX = 9
        borderY = 8
        snakeGirth = 80
        correctionX = 25
        correctionY = 60
        snakeTailX = [3, 2, 1, 0]
        snakeTailY = [4, 4, 4, 4]
        snakeHeadX = 4
        snakeHeadY = 4
        oldX = -1
        oldY = 4
    elif playingFieldSize[chosenPlayingFieldSize] == "24x21":
        borderX = 23
        borderY = 21
        snakeGirth = 33
        correctionX = 29
        correctionY = 54
        snakeTailX = [4, 3, 2, 1]
        snakeTailY = [11, 11, 11, 11]
        snakeHeadX = 5
        snakeHeadY = 11
        oldX = 0
        oldY = 11
    else:
        borderX = 16
        borderY = 14
        snakeGirth = 50
        correctionX = 1
        correctionY = 51
        snakeTailX = [4, 3, 2, 1]
        snakeTailY = [7, 7, 7, 7]
        snakeHeadX = 5
        snakeHeadY = 7
        oldX = 0
        oldY = 7

    # reset variables
    direction = "right"
    speedSnake = float(speedNumbers[chosenSpeed])
    numApplesWanted = int(numberOfApples[chosenNumberOfApples]) if numberOfApples[
                                                                       chosenNumberOfApples] != "custom" else 0
    freespaces = 17 * 15 - len(snakeTailX) - 1
    score = 0
    nearestApple = 0
    nearestAppleDistance = (0, 0)
    applesX = [8008] * numApplesWanted
    applesY = [8008] * numApplesWanted
    highlight_quit_button = False
    quit_button_clicked = False
    timerIsDone = False
    stopSnake = False
    startTime = time.time()

    resetBackground()

    while run:
        # highlight quit button
        mouse = pygame.mouse.get_pos()
        if quitBox.collidepoint(mouse):
            highlight_quit_button = True
            for eventOptionsButton in pygame.event.get():
                if eventOptionsButton.type == pygame.MOUSEBUTTONDOWN:
                    quit_button_clicked = True

        else:
            highlight_quit_button = False

        # set direction (https://www.pygame.org/docs/ref/event.html)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if timerIsDone:
                keys = pygame.key.get_pressed()
                if keys[K_LEFT] or keys[K_a]:
                    if direction != "right" and direction != "left":
                        direction = "left"
                        timerIsDone = False

                elif keys[K_RIGHT] or keys[K_d]:
                    if direction != "left" and direction != "right":
                        direction = "right"
                        timerIsDone = False

                elif keys[K_UP] or keys[K_w]:
                    if direction != "down" and direction != "up":
                        direction = "up"
                        timerIsDone = False

                elif keys[K_DOWN] or keys[K_s]:
                    if direction != "up" and direction != "down":
                        direction = "down"
                        timerIsDone = False

        # apple spawner V2
        if freespaces < numApplesWanted:
            numApplesWanted -= 1

        for i in range(len(applesX)):
            if applesX[i] == 8008:
                tmpX = random.randint(0, borderX)
                tmpY = random.randint(0, borderY)
                if tmpX != snakeHeadX or tmpY != snakeHeadY:
                    applesX[i] = tmpX
                    applesY[i] = tmpY

            for a in range(len(applesX)):
                if applesX[a] == snakeHeadX and applesY[a] == snakeHeadY:
                    applesX[a] = 8008
                    applesY[a] = 8008
                    score += 1
                    snakeTailX.append(oldX)
                    snakeTailY.append(oldY)
                else:
                    for i in range(len(snakeTailX)):
                        if applesX[a] == snakeTailX[i] and applesY[a] == snakeTailY[i]:
                            applesX[a] = 8008
                            applesY[a] = 8008
                    for j in range(len(applesX)):
                        if j != a:
                            if applesX[a] == applesX[j] and applesY[a] == applesY[j]:
                                applesX[a] = 8008
                                applesY[a] = 8008

        if not doCollisionCheck() and not stopSnake:
            drawApple()
            drawSnake()
            pygame.display.flip()
            # timer (https://www.programiz.com/python-programming/time)
            elapsedTime = time.time() - startTime
            if elapsedTime > speedSnake:
                timerIsDone = True
                startTime = time.time()

                # remember last tail position
                oldX = snakeTailX[len(snakeTailX) - 1]
                oldY = snakeTailY[len(snakeTailY) - 1]

                resetBackground()
                moveSnakeForward()
        else:
            run = False
            time.sleep(0.5)
            doHannahBaker()
