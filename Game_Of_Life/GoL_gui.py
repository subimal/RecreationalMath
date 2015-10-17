import Tkinter as tk
import ttk
import os
import pygame as pg
from GoL import *

rootapp=tk.Tk()


GoL_Frame=tk.Frame(rootapp, width = disp_N, height = disp_N)
GoL_Frame.pack()

button1 = tk.Button(rootapp, text="GoL!! :)")
button1.pack()

os.environ['SDL_WINDOWID'] = str(GoL_Frame.winfo_id())

rootapp.update()

pg.display.init()
screen = pg.display.set_mode((disp_N, disp_N))
os.environ['SDL_WINDOWID'] = str(GoL_Frame.winfo_id())

# initialize pygame
#pg.init()

# set the pygame screen
#screen = pg.display.set_mode([GoL.disp_N, GoL.disp_N])



GoL_Frame.width=disp_N
GoL_Frame.height=disp_N
GoL_Frame.pack()
rootapp.update()

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
    rootapp.update()

