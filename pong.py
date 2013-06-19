#pong game ver. Alpha 0.01
#Alec Matthews

import pygame, sys, random
from pygame.locals import*


def ballDirection():
     direction = random.randint(0,1)
     return direction

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ball = {'rect':pygame.Rect(390, 190, 20, 20),'dir':None}
paddlePlayer= pygame.Rect(50, 120, 20, 150)
paddleComp = pygame.Rect(700, 120, 20, 150)

moveUp = False
moveDown = False

#ball*
LEFT = 4
RIGHT = 6
UPLEFT = 7
DOWNLEFT = 1
UPRIGHT = 9
DOWNRIGHT = 3

MOVESPEED = 6

direction = ballDirection()

if direction == 1:
    ballLeft = True
elif direction == 0:
    ballLeft = False

if ballLeft == True:
          ball['dir'] = LEFT
elif ballLeft == False:
          ball['dir'] = RIGHT

while True:
     
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
         if event.type == KEYDOWN:
             if event.type == K_UP or event.key == ord('w'):
                 moveUp = True
                 moveDown = False
             if event.type == K_DOWN or event.key == ord('s'):
                 moveUp = False
                 moveDown = True

         if event.type == KEYUP:
             if event.key == K_ESCAPE:
                 pygame.quit()
                 sys.exit()
             if event.key == K_UP or event.key == ord('w'):
                 moveUp = False
             if event.key == K_DOWN or event.key == ord('s'):
                 moveDown = False
                
     windowSurface.fill(BLACK)
    
     if moveDown and paddlePlayer.bottom < WINDOWHEIGHT:
         paddlePlayer.top += MOVESPEED
     if moveUp and paddlePlayer.top > 0:
         paddlePlayer.top -= MOVESPEED
        
     
     if ball['rect'].colliderect(paddlePlayer):
          ball['dir'] = RIGHT

     if ball['rect'].colliderect(paddleComp):
          ball['dir'] = LEFT
          
     if ball['dir'] == LEFT:
          ball['rect'].left -= MOVESPEED
     if ball['dir'] == RIGHT:
          ball['rect'].left += MOVESPEED


     
     


       

     pygame.draw.rect(windowSurface, WHITE, paddlePlayer)
     pygame.draw.rect(windowSurface, WHITE, paddleComp)
     pygame.draw.rect(windowSurface, WHITE, ball['rect'])

     pygame.display.update()
     mainClock.tick(40)
