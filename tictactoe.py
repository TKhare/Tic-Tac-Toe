import pygame
import sys
import random
import time
# from pygame.locals import *
# from settings import *

#Initializing pygame and checking for errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print('%d errors occured: exiting...',check_errors[1])
    sys.exit()
else:
    print('Successful Initialization!')

#Setting up window and caption
DISPLAYSURF_x = 600
DISPLAYSURF_y = 600
DISPLAYSURF = pygame.display.set_mode((DISPLAYSURF_x,DISPLAYSURF_y))
pygame.display.set_caption('Tic Tac Toe')
positions = [None, None, None, None, None, None, None, None, None]
empty_board = pygame.image.load('board.png')
playerflag=True
lastposition=False
player_1 = 1
player_2 = 2
BLACK = (0,0,0)
player_1_x = pygame.image.load('player_1_x.png')
player_2_o = pygame.image.load('player_2_o.png')
def winning(number):
        #displays 'stamina'
        Font1 = pygame.font.SysFont('monaco', 24)
        winSurface = Font1.render('Player {0} Wins'.format(number), True, BLACK)
        winRect = winSurface.get_rect()
        winRect.midtop = (300, 1)
        DISPLAYSURF.blit(winSurface,winRect)
def check_winning():
    if positions[0]==positions[1]==positions[2]:
        if positions[0]==1:
            winning(player_1)
        if positions[0]==2:
            winning(player_2)
    if positions[3]==positions[4]==positions[5]:
        if positions[3]==1:
            winning(player_1)
        if positions[3]==2:
            winning(player_2)
    if positions[6]==positions[7]==positions[8]:
        if positions[6]==1:
            winning(player_1)
        if positions[6]==2:
            winning(player_2)
    if positions[0] == positions[4]==positions[8]:
        if positions[0]==1:
            winning(player_1)
        if positions[0]==2:
            winning(player_2)
    if positions[2] == positions[4]== positions[6]:
        if positions[2]==1:
            winning(player_1)
        if positions[2]==2:
            winning(player_2)
    if positions[0] == positions[3] == positions[6]:
        if positions[0]==1:
            winning(player_1)
        if positions[0]==2:
            winning(player_2)
    if positions[1] == positions[4] == positions[7]:
        if positions[1]==1:
            winning(player_1)
        if positions[1]==2:
            winning(player_2)
    if positions[2]== positions[5] == positions[8]:
        if positions[2]==1:
            winning(player_1)
        if positions[2]==2:
            winning(player_2)
#Creating background board
jk = 1
DISPLAYSURF.fill([0,0,0])
DISPLAYSURF.blit(empty_board, [0, 0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y)= pygame.mouse.get_pos()
            if playerflag == True:
                if jk == 1:
                #if lastposition == False:
                    if x < 200 and y < 200 and positions[0] == None:
                        positions[0] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (10,10))
                    if x < 400 and y < 200 and x > 200 and positions[1] == None:
                        positions[1] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (210,10))
                    if x < 600 and y < 200 and x > 400 and positions[2] == None:
                        positions[2] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (410,10))
                    if x < 200 and y < 400 and y > 200 and positions[3] == None:
                        positions[3] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (10,210))
                    if x < 400 and y < 400 and x > 200 and y > 200 and positions[4] == None:
                        positions[4] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (210,210))
                    if x > 400 and y < 400 and y > 200 and positions[5] == None:
                        positions[5] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (410,210))
                    if x < 200 and y > 400 and positions[6] == None:
                        positions[6] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (10,410))
                    if x < 400 and y > 400 and x > 200 and positions[7] == None:
                        positions[7] = 1
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (210,410))
                    if x > 400 and y > 400 and positions[8] == None:
                        positions[8] = 1 
                        playerflag = False
                        DISPLAYSURF.blit(player_1_x, (410,410))

                    lastpostion = True

            else:
                #if lastposition == True:
                if jk == 1:
                    if x < 200 and y < 200 and positions[0] == None:
                        positions[0] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (10,10))   
                    if x < 400 and y < 200 and x > 200 and positions[1] == None:
                        positions[1] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (210,10))
                    if x < 600 and y < 200 and x > 400 and positions[2] == None:
                        positions[2] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (410,10))
                    if x < 200 and y < 400 and y > 200 and positions[3] == None:
                        positions[3] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (10,210))
                    if x < 400 and y < 400 and x > 200 and y > 200 and positions[4] == None:
                        positions[4] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (210,210))
                    if x > 400 and y < 400 and y > 200 and positions[5] == None:
                        positions[5] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (410,210))
                    if x < 200 and y > 400 and positions[6] == None:
                        positions[6] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (10,410))
                    if x < 400 and y > 400 and x > 200 and positions[7] == None:
                        positions[7] = 2
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (210,410))
                    if x > 400 and y > 400 and positions[8] == None:
                        positions[8] = 2 
                        playerflag = True
                        DISPLAYSURF.blit(player_2_o, (410,410))
                    lastposition = False
            print positions    
    #for place in positions:
        #if place == 1:
            #draw image 1
        #if place == 2:
            #draw image 2
    check_winning()

    pygame.display.flip()

