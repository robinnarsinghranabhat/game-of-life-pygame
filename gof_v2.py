

import sys, pygame
import random
import time
import numpy as np
pygame.init()

size = width, height = 800, 800
resolution = 10

row, col = width // resolution , height // resolution

speed = [2, 2]
black = 0, 0, 0
white = 200,200,200

screen = pygame.display.set_mode(size,0,32)
screen.fill(white)

def make_grid(row, col):
    return [  [ random.choice( [0] )  for _ in range(col)] for _ in range(row)]


start_grid = make_grid(row, col)
count = 0
import time

def transformer(grid,x,y):

    r,c = grid.shape
    global start_grid
    for i in range(r):
        for j in range(c):
            temp_x = (i + x + col) % col
            temp_y = (j + y + row) % row

            try:
                start_grid[ temp_x ][temp_y] = grid[i][j]
            except:
                import pdb; pdb.set_trace()

def glider(x,y):
    my_grid = np.array( [[0,1,0],[0,0,1],[1,1,1]] )
    return transformer(my_grid,x,y)


def pulsar(x,y):
    X = np.zeros((17, 17))
    X[2, 4:7] = 1
    X[4:7, 7] = 1
    X += X.T
    X += X[:, ::-1]
    X += X[::-1, :]
    return transformer(X,x-8,y-8)

def glider_gun(x,y,ind  = 3):
    glider_gun = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    X = np.zeros((50, 70))
    X[1:10,1:37] = glider_gun

    transformer(X,x-5 ,y - 18 )


##
ind_color = { 0 : (0,0,0) , 1 : (255,255,255) , 2 : (255, 0,0), 3 : (255, 255,0)   }


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = pygame.mouse.get_pos()
            pos_x , pos_y = pos_x // resolution , pos_y // resolution
            glider(pos_x,pos_y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_x , pos_y = pos_x // resolution , pos_y // resolution
                pulsar(pos_x,pos_y)

            if event.key == pygame.K_w:
                pos_x, pos_y = pygame.mouse.get_pos()
                pos_x , pos_y = pos_x // resolution , pos_y // resolution
                glider_gun(pos_x,pos_y)


            if event.key == pygame.K_r:
                start_grid = make_grid(row,col)




    for x in range(row):
        for y in range(col):

            rect = pygame.Rect(x*resolution , y*resolution , resolution, resolution)
            pygame.draw.rect(screen, ind_color[  start_grid[x][y]  ] , rect )


    new_grid = [  [ 0  for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            ## look around neighbours ...
            cell_info = start_grid[i][j]
            sum = 0
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if k == 0 and l == 0:
                        continue
                    # sum += start_grid[i + k][j + l]
                    temp_x = (i + k + col) % col
                    temp_y = (j + l + row) % row

                    if start_grid[ temp_x ][ temp_y ] != 0:
                        sum += 1
            # print( x,y )
            if  cell_info == 1 and ( int(sum) not in [3,2] ):
                new_grid[i][j] = 0
            elif cell_info == 0 and sum == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = cell_info

    # import pdb; pdb.set_trace()
    start_grid = new_grid
    # screen.fill(black)
    # screen.blit(ball, ballrect)
    pygame.display.update()
