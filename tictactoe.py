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
DISPLAYSURF_x = 900
DISPLAYSURF_y = 900
DISPLAYSURF = pygame.display.set_mode((DISPLAYSURF_x,DISPLAYSURF_y))
pygame.display.set_caption('Tic Tac Toe')
positions = [None, None, None, None, None, None, None, None, None]
empty_board = pygame.image.load('board.png')
playerflag=True
lastposition=False
player_1 = 1
plater_2 = 2
BLACK = (0,0,0)
def winning(number):
        #displays 'stamina'
        Font1 = pygame.font.SysFont('monaco', 24)
        winSurface = Font1.render('Stamina: {0}%'.format(number), True, BLACK)
        winRect = winSurface.get_rect()
        winRect.midtop = (450, 10)
        DISPLAYSURF.blit(stamSurface,stamRect)
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
while True:
    DISPLAYSURF.fill([0,0,0])
    DISPLAYSURF.blit(empty_board, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y)= pygame.mouse.get_pos()
            if playerflag == True:
                if lastposition == False:
                    if x < 300 and y < 300 and positions[0] == None:
                        positions[0] = 1
                        playerflag = False
                    if x < 600 and y < 300 and x > 300 and positions[1] == None:
                        positions[1] = 1
                        playerflag = False
                    if x < 900 and y < 300 and x > 600 and positions[2] == None:
                        positions[2] = 1
                        playerflag = False
                    if x < 300 and y < 600 and y > 300 and positions[3] == None:
                            positions[3] = 1
                            playerflag = False
                    if x < 600 and y < 600 and x > 300 and y > 300 and positions[4] == None:
                        positions[4] = 1
                        playerflag = False
                    if x > 600 and y < 600 and y > 300 and positions[5] == None:
                        positions[5] = 1
                        playerflag = False
                    if x < 300 and y > 600 and positions[6] == None:
                        positions[6] = 1
                        playerflag = False
                    if x < 600 and y > 600 and x > 300 and positions[7] == None:
                        positions[7] = 1
                        playerflag = False
                    if x > 600 and y > 600 and positions[8] == None:
                        positions[8] = 1 
                        playerflag = False
                    lastpostion = True

            else:
                if lastposition == True:
                    if x < 300 and y < 300 and positions[0] == None:
                        positions[0] = 2
                        playerflag = True   
                    if x < 600 and y < 300 and x > 300 and positions[1] == None:
                        positions[1] = 2
                        playerflag = True
                    if x < 900 and y < 300 and x > 600 and positions[2] == None:
                        positions[2] = 2
                        playerflag = True
                    if x < 300 and y < 600 and y > 300 and positions[3] == None:
                        positions[3] = 2
                        playerflag = True
                    if x < 600 and y < 600 and x > 300 and y > 300 and positions[4] == None:
                        positions[4] = 2
                        playerflag = True
                    if x > 600 and y < 600 and y > 300 and positions[5] == None:
                        positions[5] = 2
                        playerflag = True
                    if x < 300 and y > 600 and positions[6] == None:
                        positions[6] = 2
                        playerflag = True
                    if x < 600 and y > 600 and x > 300 and positions[7] == None:
                        positions[7] = 2
                        playerflag = True
                    if x > 600 and y > 600 and positions[8] == None:
                        positions[8] = 2 
                        playerflag = True
                    lastposition = False
            print positions()    

    pygame.display.flip()

