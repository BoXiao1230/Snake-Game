# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:29:43 2019

@author: xiaob
"""
#%% SNAKE GAMES
import pygame
import sys
import random

#This module contains various constants used by pygame
from pygame.locals import*

#Define color variables
#FOOD
redColor = pygame.Color(255,0,0)
#BACKGROUND
blackColor = pygame.Color(0,0,0)
#SNAKE
whiteColor = pygame.Color(255,255,255)

#Define a function to end the game
def gameOver():
    pygame.quit()
    sys.exit()
    
# Define a main function as the entrance of the program
def main():
    #initialize all imported pygame modules
    pygame.init()
    
    #define a variable to control the speed
    fpsClock = pygame.time.Clock() #create a new Clock object that can be used to track an amount of time. It also procides several functions to help control game's framereate.
    
    #develop a display layer for the pygame
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("SNAKE")
    
    #initialize the snake's position
    snakePosition = [100,100]
    
    #initialize the snake's length: num of elements in the list indicate the length of the snake 
    snakeBody = [[100,100],[80,100],[60,100]] 
    
    #initialize the target's position
    targetPosition = [300,300]
    
    #label to indicate whether the target is eaten by the snake
    targetflag = 1 # means the target is intact
    
    #initialize the moving direction for the snake
    direction = 'right'
    
    #define a variable for the direction controlled by gamers.
    changeDirection = direction
    
    while True:
        for event in pygame.event.get(): #get events from the queue
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                    
        # change the direction:    
        if changeDirection == 'left' and direction != 'right':
            direction = changeDirection
        if changeDirection == 'right' and direction != 'left':
            direction = changeDirection    
        if changeDirection == 'up' and direction != 'down':
            direction = changeDirection    
        if changeDirection == 'down' and direction != 'up':
            direction = changeDirection
            
        # moving the snake head based on the direction
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20        
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        
        # adding snake's body
        snakeBody.insert(0,list(snakePosition))
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()
        
        if targetflag == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            targetPosition = [int(x*20),int(y*20)]
            targetflag = 1
            
        playSurface.fill(blackColor)
        
        for position in snakeBody:
            #
            pygame.draw.rect(playSurface,whiteColor, pygame.Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface,redColor, pygame.Rect(targetPosition[0], targetPosition[1], 20, 20))
        
        pygame.display.flip() #Update the full display Surface to the screen
        
        
        # Determine whether we should end the game.
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver()
        # Control the game speed
        fpsClock.tick(5)
        
if __name__ == '__main__':
    main()
