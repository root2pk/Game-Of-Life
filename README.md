# Game-Of-Life
Simulation of Conway's game of life model for cellular automation



game_of_life.py simulates game of life and visualises it. Usage " python game_of_life.py N ", where N is the side length of the square lattice to be simulated (N X N)
Select which initial conditions to use when prompted. For glider simulations, specify number of steps to simulate(keep below 50 to calculate speed properly)

game_of_life_loop.py simulates game of life multiple times to obtain values of equilibrium time

histogram_plotter.py plots historgram from "EQ_times.txt" 
Usage "histogram_plotter.py bins"

methods_gol.py contains all the methods used for game of life simulation
