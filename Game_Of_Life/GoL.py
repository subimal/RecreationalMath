#############################################################################################################
# Conway's game of life (GoL)                                                                               #
#                                                                                                           #
#   rule_1 : Any live cell with fewer than two live neighbours dies, as if caused by under-population.      #
#   rule_2 : Any live cell with two or three live neighbours lives on to the next generation.               #
#   rule_3 : Any live cell with more than three live neighbours dies, as if by overcrowding.                #
#   rule_4 : Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.   #
#############################################################################################################

#################################
# import the required libraries
#################################
import numpy as np
import pygame as pg
import pygame.surfarray as sa
from time import sleep


# GoL array size NxN
N=300

# pygame display resolution disp_N x disp_N
disp_N = 600 


# initialize the GoL grid
a=np.zeros([N+2,N+2])

# choose the initial populated grid size

# uncomment the line below to use the full grid
#xmin,xmax,ymin,ymax = 1,N,1,N

# set the population to be initially restricted to the central region of the grid
xmin,xmax,ymin,ymax = N/4,3*N/4,N/4,3*N/4

# randomize the initial population
a[xmin:xmax,ymin:ymax]=(np.random.random([xmax-xmin,ymax-ymin])>.5)*1.0

x,y=np.meshgrid(range(1,N+1),range(1,N+1))

def gol_show_grid_evolution(screen, delay=0):
    '''The GoL grid is displayed by this function.'''
    su=sa.make_surface(a[1:N,1:N])
    su_new=pg.transform.scale(su, (disp_N, disp_N))
    screen.blit(su_new,(0,0))
    pg.display.update()
    if delay != 0:
        sleep(delay)


def gol_iterate(a):
    '''Input:
                Variable    Description                 Type
                a           The GoL grid.               Numpy array

        Output:
                a           The iterated GoL grid.      Numpy array
        
        Takes the GoL grid through to the next iteration and returns the GoL grid.
    '''
    nb=a[x+1,y]+a[x+1,y+1]+a[x,y+1]+a[x-1,y+1]+a[x-1,y]+a[x-1,y-1]+a[x,y-1]+a[x+1,y-1]
    live_cell = (a[x,y]==1.0)*1.0
    dead_cell = (a[x,y]==0.0)*1.0
        
    rule_1 = (nb<2)*0.0
    rule_2 = (nb==2)*1.0 + (nb==3)*1.0
    rule_3 = (nb>3.0)*0.0
    rule_4 = (nb==3.0)*1.0

    a[x,y] = live_cell*(rule_1 + rule_2 + rule_3 ) + dead_cell*(rule_4)
    return a




if __name__=='__main__':

    # initialize pygame
    pg.init()

    # set the pygame screen
    screen = pg.display.set_mode([disp_N, disp_N])

    # iterate the GoL grid forever
    while True:
        a=gol_iterate(a)

        # set the boundaries as dead cells
        a[0,:]=0
        a[:,0]=0
        a[N+1,:]=0
        a[:,N+1]=0
    
        # display the evolved grid
        gol_show_grid_evolution(screen)

