"""
Program to run game of life in a loop, and get values for equilibrium time
Histogram is then obtained from these equilibrium values

"""

import sys
import time
import random
import numpy as np

from typing import no_type_check
import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from methods_gol import rand_init, check, equilibrium_check, rand_init, plot_lattice

##############   MAIN FUNCTION   #######################

# Number of timesteps
nstep = 5000              

# Input
if(len(sys.argv) != 2):
   print ("Usage python game_of_life.py no_of_simulations")
   sys.exit()

# Number of histogram times
no_of_simulations = int(sys.argv[1]) 

# Number of sites
lx = 50
ly = lx
N = lx*ly

# Set up files
EQ_times = open("EQ_times.txt","w")

# Set up lists to store values of equilibrium times
t_list = []

# To calculate time elapsed
start = time.time()

# Loop through number of times required for histogram
for loops in range(0,no_of_simulations):

    print(loops)

    # Initialise lattice
    lattice = rand_init(lx,ly).copy()

    # Lattice to store all the changes made 
    lattice2 = lattice.copy()

    # List of number of active sites
    no = []
    no.append(np.sum(lattice))

    # Set up plot
    fig = plt.figure()

    # Plot first time
    plot_lattice(lattice)

    # Start timestep            
    for n in range(nstep):

        # Looping through lx*ly iterations
        for i in range(lx):
            for j in range(ly):
                lattice2[i,j] = check(lattice,i,j,lx,ly)
        
        # Copy lattice2 to lattice
        lattice = lattice2.copy()

        # Number of active sites 
        no.append(np.sum(lattice))
        
        # Plot every timestep
        plot_lattice(lattice)

        # Equilibrium Check
        if len(no) > 20:
            if(equilibrium_check(no) == True):
                break
    
    # Timestep at which equilibrium was attained
    t = n - 9
    t_list.append(t)
    EQ_times.write('%d\n' %(t))

# Close file
EQ_times.close()

# Time elapsed
print("Time Elapsed = {:.2f}s".format(time.time()-start))
print(t_list)





