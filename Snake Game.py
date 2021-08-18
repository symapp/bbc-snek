import pygame
from pygame.locals import *
import sys    #https://canberragpn.github.io/static/doc/PygameCheatSheet.pdf
import time
from random import *
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
for i in range(19): #bei 0 0 = 50 0 . 50 850
    pygame.draw.line(surface, lineColor, ((i*50), 50), ((i*50), 800), width=1)

pygame.display.flip()

#Functions
def drawSnakeHead(snakeHeadXPosition, snakeHeadYPosition):
    pygame.draw.rect(surface, snakeColor, ((snakeHeadXPosition-1)*50+1, ((snakeHeadYPosition-1)*50+51), 49, 49), border_radius=0)

def drawApple(appleXPosition, appleYPosition):
    pygame.draw.circle(surface, appleColor, ((appleXPosition-1)*50-25, (appleYPosition-1)*50+75), 23)

#Apple list

appleList = [[False]*15]*17
print(appleList)

#Snake
snakeHeadXPosition = 1
snakeHeadYPosition = 1
running = True
while running:
    for event in pygame.event.get():    #https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

        #Snake Head
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
                snakeHeadXPosition -= 1
                if snakeHeadXPosition == 0:
                    snakeHeadXPosition = 1
        elif keys[K_RIGHT]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadXPosition += 1
                if snakeHeadXPosition == 18:
                    snakeHeadXPosition = 17
        elif keys[K_DOWN]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadYPosition += 1
                if snakeHeadYPosition == 16:
                    snakeHeadYPosition = 15
        elif keys[K_UP]:
            if move_ticker == 0:
                move_ticker = 10
                snakeHeadYPosition -= 1
                if snakeHeadYPosition == 0:
                    snakeHeadYPosition = 1
        pygame.display.flip()
        if move_ticker > 0:
            move_ticker -= 1

    #Apples
    while numberOfApplesInGame < numberOfApplesWanted:
        tempAppleXPosition = random.randint(1, 17)
        tempAppleYPosition = random.randint(1, 15)
        drawApple(tempAppleXPosition, tempAppleYPosition)
        numberOfApplesInGame += 1
        appleList[tempAppleYPosition-1][tempAppleXPosition-1] = True
        print("gen")
        print(appleList)

    #Eating apple
    appleXCounter = 0
    appleYCounter = 0
    for i in appleList:
        appleXCounter = 0
        while appleXCounter < 17:
            for j in appleList[appleXCounter]:
                if j:
                    if appleList[snakeHeadYPosition-1][snakeHeadXPosition-2]:
                        appleList[appleYCounter][appleXCounter] = False
                        score += 1
                        numberOfApplesInGame -= 1

                appleXCounter += 1
        appleYCounter += 1

    pygame.display.flip()



pygame.display.quit()