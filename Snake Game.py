import pygame
from pygame.locals import *
import sys    #https://canberragpn.github.io/static/doc/PygameCheatSheet.pdf
import time
from random import *
from multiprocessing import Process #https://stackoverflow.com/questions/3474382/how-do-i-run-two-python-loops-concurrently
random = Random()
pygame.init()

#Display
size_x = 851 #17 felder
size_y = 801 #15 felder
surface = pygame.display.set_mode((size_x, size_y))

#Some variables
numberOfApplesInGame = 0
numberOfApplesWanted = 1
score = 0

#Colors
lineColor = (0, 0, 0)
backgroundColor = (140, 177, 217)
snakeColor = (230, 138, 0)
appleColor = (255, 0, 0)
white = (255, 255, 255)

#Background
surface.fill(backgroundColor)
for i in range(16):
    pygame.draw.line(surface, lineColor, (0, (i*50)+50), (850, (i*50)+50), width=1)
for i in range(19):
    pygame.draw.line(surface, lineColor, ((i*50), 50), ((i*50), 800), width=1)

pygame.display.flip()

#Functions
def drawSnakeHead(snakeHeadXPosition, snakeHeadYPosition):
    pygame.draw.rect(surface, snakeColor, ((snakeHeadXPosition-1)*50+1, ((snakeHeadYPosition-1)*50+51), 49, 49), border_radius=0)

def drawApple(appleXPosition, appleYPosition):
    pygame.draw.circle(surface, appleColor, ((appleXPosition-1)*50-25, (appleYPosition-1)*50+75), 23)

def spawnApple():
    global numberOfApplesInGame
    random = Random()
    tempAppleXPosition = random.randint(1, 17)
    tempAppleYPosition = random.randint(1, 15)
    drawApple(tempAppleXPosition+1, tempAppleYPosition)
    numberOfApplesInGame += 1
    appleList[tempAppleYPosition-1][tempAppleXPosition-1] = True
    print("gen")
    print(appleList)

def moveForwardLoop():
    global snakeHeadXPosition
    global snakeHeadYPosition
    global direction
    if direction == "right":
        snakeHeadXPosition += 1
    elif direction == "left":
        snakeHeadXPosition -= 1
    elif direction == "down":
        snakeHeadYPosition += 1
    elif direction == "up":
        snakeHeadYPosition -= 1
    time.sleep(1)


#Apple list
appleList = [
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    ]


#Main Loop
def doMainLoop():
    for event in pygame.event.get():    #https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
        global snakeHeadXPosition
        global snakeHeadYPosition
        global direction
        global numberOfApplesInGame
        drawSnakeHead(snakeHeadXPosition, snakeHeadYPosition)
        pygame.display.flip()
        move_ticker = 0
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and (keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]):
            continue
        elif keys[K_RIGHT] and (keys[K_UP] or keys[K_DOWN]):
            continue
        elif keys[K_UP] and keys[K_DOWN]:
            continue
        elif keys[K_LEFT]:
            if move_ticker == 0:
                move_ticker = 10
                direction = "left"
        elif keys[K_RIGHT]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadXPosition += 1
                direction = "right"
        elif keys[K_DOWN]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadYPosition += 1
                direction = "down"
        elif keys[K_UP]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadYPosition -= 1
                direction = "up"
        pygame.display.flip()
        if move_ticker > 0:
            move_ticker -= 1

    #Eating apple
    appleXCounter = 0
    appleYCounter = 0
    for i in appleList:
        appleXCounter = 0
        for j in appleList[appleXCounter]:

            if appleList[snakeHeadYPosition-1][snakeHeadXPosition-1]:
                appleList[snakeHeadYPosition-1][snakeHeadXPosition-1] = False
                score += 1
                numberOfApplesInGame -= 1
                print("detected")
                spawnApple()

            appleXCounter += 1
        appleYCounter += 1
    pygame.display.flip()

# Snake
snakeHeadXPosition = 1
snakeHeadYPosition = 1
running = True
spawnApple()
direction = "right"

while running:
    Process(target=moveForwardLoop()).start()
    Process(target=doMainLoop()).start()



pygame.display.quit()