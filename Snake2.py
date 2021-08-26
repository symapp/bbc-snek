import pygame
from pygame.locals import *
import time
from random import *

random = Random()
pygame.init()

# Display
size_x = 851  # 17 felder
size_y = 801  # 15 felder
surface = pygame.display.set_mode((size_x, size_y))

# Colors
lineColor = (0, 0, 0)
backgroundColor = (140, 177, 217)
snakeColor = (230, 138, 0)
appleColor = (255, 0, 0)
white = (255, 255, 255)

# Snake
snakeTailX = [4, 3, 2, 1]
snakeTailY = [7, 7, 7, 7]
snakeHeadX = 5
snakeHeadY = 7

# Functions
def resetBackground():
    surface.fill(backgroundColor)
    for i in range(16):
        pygame.draw.line(surface, lineColor, (0, (i * 50) + 50), (850, (i * 50) + 50), width=1)
    for i in range(19):
        pygame.draw.line(surface, lineColor, ((i * 50), 50), ((i * 50), 800), width=1)
    pygame.display.flip()


def drawSnake():
    # Snake Head
    pygame.draw.rect(surface, snakeColor, ((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 51), 49, 49))

    # Snake Body
    for i in reversed(range(len(snakeTailX))):
        tempX = snakeTailX[i]
        tempY = snakeTailY[i]

        pygame.draw.rect(surface, snakeColor, ((tempX * 50 + 1), (tempY * 50 + 51), 49, 49))

    # "Eyes"
    if direction == "right":
        pygame.draw.rect(surface, white, ((snakeHeadX * 50 + 45), (snakeHeadY * 50 + 74), 5, 5))
    if direction == "left":
        pygame.draw.rect(surface, white, ((snakeHeadX * 50 + 1), (snakeHeadY * 50 + 74), 5, 5))
    if direction == "up":
        pygame.draw.rect(surface, white, ((snakeHeadX * 50 + 23), (snakeHeadY * 50 + 51), 5, 5))
    if direction == "down":
        pygame.draw.rect(surface, white, ((snakeHeadX * 50 + 23), (snakeHeadY * 50 + 95), 5, 5))

    pygame.display.flip()


def drawApple():
    for i in range(numApplesWanted):
        if applesX[i] != "":
            pygame.draw.circle(surface, appleColor, (applesX[i] * 50 + 25, applesY[i] * 50 + 75), 23)
    pygame.display.flip()



def moveSnakeForward():
    global snakeHeadX
    global snakeHeadY
    global snakeTailX
    global snakeTailY
    global run

    # Move Body Forward   MAYBE + 1 V
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

    # Collision check
    if snakeHeadX > 17:
        pygame.quit()
        run = False
    elif snakeHeadX < 0:
        pygame.quit()
        run = False
    elif snakeHeadY > 15:
        pygame.quit()
        run = False
    elif snakeHeadY < 0:
        pygame.quit()
        run = False
    for i in range(len(snakeTailX)):
        for j in range(len(snakeTailY)):
            if snakeHeadX == snakeTailX and snakeHeadY == snakeBodyY:
                pygame.quit()
                run = False


# Main Loop
run = True
direction = "right"
numApplesInGame = 0
numApplesWanted = 1
applesX = [""]*numApplesWanted
applesY = [""]*numApplesWanted
score = 0

idk = False


resetBackground()

startTime = time.time()
while run:

    # Set Direction (https://www.pygame.org/docs/ref/event.html)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if idk:
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                if direction != "right":
                    direction = "left"
                    idk = False

            elif keys[K_RIGHT]:
                if direction != "left":
                    direction = "right"
                    idk = False

            elif keys[K_UP]:
                if direction != "down":
                    direction = "up"
                    idk = False

            elif keys[K_DOWN]:
                if direction != "up":
                    direction = "down"
                    idk = False


    # Apple Spawner
    if numApplesWanted > numApplesInGame:
        for i in range(numApplesWanted):
            if applesX[i] == "":
                tempAppleX = random.randint(0, 16)
                tempAppleY = random.randint(0, 14)
                applesX[i] = tempAppleX
                applesY[i] = tempAppleY

    # Apple Checker
    for i in range(len(applesX)):
        for j in range(len(applesY)):
            if applesX[i] == snakeHeadX and applesY[j] == snakeHeadY:
                applesX[i] = ""
                applesY[j] = ""
                score += 1
                numApplesInGame = 0

    # Collision check
    if snakeHeadX > 17:
        pygame.quit()
        run = False
        break
    elif snakeHeadX < 0:
        pygame.quit()
        run = False
        break
    elif snakeHeadY > 15:
        pygame.quit()
        run = False
        break
    elif snakeHeadY < 0:
        pygame.quit()
        run = False
        break
    for i in range(len(snakeTailX)):
        for j in range(len(snakeTailY)):
            if snakeHeadX == snakeTailX and snakeHeadY == snakeBodyY:
                pygame.quit()
                run = False




    # Timer (https://www.programiz.com/python-programming/time)
    elapsedTime = time.time() - startTime
    if elapsedTime > 0.3:
        idk = True
        startTime = time.time()
        resetBackground()
        moveSnakeForward()


    drawApple()
    drawSnake()

    pygame.display.flip()


