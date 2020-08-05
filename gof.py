

import sys, pygame
import random
import time
pygame.init()

size = width, height = 600, 600
resolution = 20

row, col = width // resolution , height // resolution

speed = [2, 2]
black = 0, 0, 0
white = 200,200,200

screen = pygame.display.set_mode(size,0,32)
screen.fill(white)

def make_grid(row, col):
    return [  [ random.choice( [0,1] )  for _ in range(col)] for _ in range(row)]





start_grid = make_grid(row, col)
count = 0
while 1:
    time.sleep(0.3)
    count += 1
    for x in range(row):
        for y in range(col):
            rect = pygame.Rect(x*resolution, y*resolution, resolution-1, resolution-1)

            if start_grid[x][y] == 0 :
                pygame.draw.rect(screen, black, rect )
            else :
                pygame.draw.rect(screen, white, rect )

    # start_grid = something+new ..


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
                    try:
                        sum += start_grid[i + k][j + l]
                    except Exception as e:
                        pass
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
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
