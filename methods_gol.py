
import random
import numpy as np

from typing import no_type_check
import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
File with all the methods used for the game of life simulation

"""


def beehive(lattice,lx,ly):

    i = int(lx/2)
    j = int(ly/2)

    lattice[i,j+1] = 1
    lattice[i+1,j] = 1
    lattice[i+1,j-1] = 1
    lattice[i,j-2] = 1
    lattice[i-1,j-1] = 1 
    lattice[i-1,j] = 1

    return lattice

def glider(lattice,lx,ly):
    # Glider
    i = int(lx/2)
    j = int(ly/2)

    lattice[i,j-1] = 1
    lattice[i+1,j] = 1
    lattice[i+1,j-1] = 1
    lattice[i,j+1] = 1
    lattice[i-1,j-1] = 1

    return lattice

def blinker(lattice,lx,ly):
    # Blinker

    i = int(lx/2)
    j = int(ly/2)

    lattice[i+1,j] = 1
    lattice[i-1,j] = 1
    lattice[i][j] = 1

    return lattice

def rand_init(lattice, lx,ly):
    """
    Initialises a lx*ly lattice with random initial conditions
    (Equal probability of S,I and R)
    Takes in lx and ly
    Returns lattice
    
    """

    # Random
    for i in range(lx):
        for j in range(ly):
            r=random.random()
            if(r<0.5):
                lattice[i,j] = 0           # 0 implies dead cell
            else:
                lattice[i,j] = 1           # 1 implies live cell

    return lattice

def check(lattice,i,j,lx,ly):

    lN = lattice[i,(j+1)%ly]               # North
    lNE = lattice[(i+1)%lx,(j+1)%ly]       # North East
    lE = lattice[(i+1)%lx,j]               # East
    lSE = lattice[(i+1)%lx,(j-1)%ly]       # South East
    lS = lattice[i,(j-1)%ly]               # South 
    lSW = lattice[(i-1)%lx,(j-1)%ly]       # South West
    lW = lattice[(i-1)%lx,j]               # West
    lNW = lattice[(i-1)%lx,(j+1)%ly]       # North West
    
    l_sum = lN + lNE + lE + lSE + lS + lSW + lW + lNW


    if lattice[i,j] == 1:
        # Live to Dead
        if (l_sum == 2) or (l_sum == 3):
            return 1       

        # Live to Live
        else:
            return 0   
    else:                                                                                                                                                                                
        # Dead to Live
        if l_sum == 3:
            return 1

        # Dead to Dead
        else:
            return 0

def equilibrium_check(no):
    # List of last 10 entries
    last_ten = no[-10:]

    # Absolute value of difference between consecutive elements
    diff = [x - last_ten[i-1] for i, x in enumerate(last_ten)][1:]
    diff = np.abs(diff)

    # if there is no difference between last 10 elements, equilibrium
    if np.sum(diff) == 0:
        return True
    else:
        return False
        
def CoM(lattice,lx,ly):

    # Indices of the alive cells
    glider_cells = np.nonzero(lattice)

    x_com = 0
    y_com = 0
    n = np.sum(lattice)
    for i in range(lx):
        for j in range(ly):
            x_com += i*lattice[i][j]
            y_com += j*lattice[i][j]
    
    x_com = x_com/n 
    y_com = y_com/n 


    # If glider is near the edge, CoM location is 0
    for i in range(0, len(glider_cells)):
        for j in range(0, len(glider_cells[0])):
            index = glider_cells[i][j]
            if index == 0 or index == lx or index == ly:
                x_com = 0
                y_com = 0

    return x_com,y_com

def plot_lattice(lattice):
    """
    Function to plot the lattice using imshow()
    """
    plt.cla()
    im = plt.imshow(lattice.T, animated=True, origin='lower')
    plt.draw()
    plt.pause(0.0001)