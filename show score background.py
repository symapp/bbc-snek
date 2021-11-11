import pygame
from pygame.locals import *
import time
import math
import random

pygame.init()
size_x = 851
size_y = 801
surface = pygame.display.set_mode((size_x, size_y))
random = random.Random()

backgroundColor = "#5BC3EB"
raisinBlack = "#1D1E2C"
snakeColor = "#FFA10A"
white = "#FFFFFF"
black = "#000000"
score = 40
username = "asdfa"

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
            continue
            #return
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


showScore()
time.sleep(5)
