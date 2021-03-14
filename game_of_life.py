"""
Program to simulate game of life for an lx*ly lattice
Takes in N, which is the side length of the square lattice

4 initial conditions are possible
1) Random
2) Beehive
3) Glider
4) Blinker

Plots Average active sites as a function of time 
Plots centre of mass position for glider and calculates glider speed

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

from methods_gol import beehive, glider, blinker, rand_init, check, equilibrium_check, CoM, plot_lattice

##############   MAIN FUNCTION   #######################

nstep = 10000              # Number of timesteps

# # Input

if(len(sys.argv) != 2):
   print ("Usage python game_of_life.py N")
   sys.exit()

# Number of sites
lx=int(sys.argv[1]) 
ly = lx
N = lx*ly

# To calculate time elapsed
start = time.time()

###################################    INITIAL CONDITIONS       ###################################

# Mode = 1 for random,2 for beehive, 3 for glider,4 for blinker

mode = int(input("Select Initial conditions\n1) Random\n2) Beehive\n3) Glider\n4) Blinker\n"))
if mode != 1 and mode !=2 and mode !=3 and mode !=4:
    print("Select correct mode")
    sys.exit()

# Initialise sites 
lattice = np.zeros((lx,ly),dtype = int)

# Select inital configuration
if mode == 1:
    lattice = rand_init(lattice,lx,ly).copy()
elif mode == 2:
    lattice = beehive(lattice,lx,ly).copy()
elif mode == 3:
    lattice = glider(lattice,lx,ly).copy()
    nstep = int(input("Number of Steps?\n"))
else:
    lattice = blinker(lattice,lx,ly).copy()

# Lattice to store all the changes made 
lattice2 = lattice.copy()

############################## Initialising lists to store data   ###############################

# Number of active sites
no = []
no.append(np.sum(lattice))

# Lists to store centre of mass position
x_com_list = []
y_com_list = []

# Set up plot
fig = plt.figure()

# Plot first time
plot_lattice(lattice)

# Start timestep            
for n in range(nstep):

    # Looping through lx*ly iterations
    for i in range(lx):
        for j in range(ly):
            lattice2[i,j] = int(check(lattice,i,j,lx,ly))
    
    # Copy lattice2 to lattice
    lattice = lattice2.copy()

    # Number of active sites 
    no.append(np.sum(lattice))
    
    # Plot every timestep
    plot_lattice(lattice)

    # Keep track of the timestep
    if n % 100 == 0:
        print(n)

    # If in glider mode, calculate positions of CoM
    if mode == 3:
        x_com,y_com = CoM(lattice,lx,ly)

        x_com_list.append(x_com)
        y_com_list.append(y_com)


plt.close()

# Print time elapsed
print("Time Elapsed = {:.2f}s".format(time.time()-start))

# Plot number of active sites
tim =  np.linspace(0,n,num = len(no))
plt.plot(tim,no)
plt.xlabel('Timestep')
plt.ylabel('Number of Active sites')
plt.show()


# Plot CoM charactersitic if in Glider mode
if mode ==3:
    # Plot COM vs time for glider

    t = np.linspace(0,n,num = len(x_com_list))

    m, b = np.polyfit(t, x_com_list, 1)
    vx = m
    print(m)
    plt.scatter(t,x_com_list,marker='x')
    plt.plot(t,m*t + b,'r')
    plt.title('X coordinate of CoM vs. timestep')
    plt.xlabel('Timestep')
    plt.ylabel('x-coordinate of Centre of Mass')
    plt.show()

    m, b = np.polyfit(t, y_com_list, 1)
    vy = m

    plt.scatter(t,y_com_list,marker='x')
    plt.plot(t,m*t + b,'r')
    plt.title('Y coordinate of CoM vs. timestep')
    plt.xlabel('Timestep')
    plt.ylabel('y-coordinate of Centre of Mass')
    plt.show()

    # Velocity calculation

    vel = np.sqrt(vx**2 + vy**2)
    print('vx = %0.3f sites per timestep\nvy = %0.3f sites per timestep\nspeed = %0.3f sites per timestep' %(vx,vy,vel))



