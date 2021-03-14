import sys
import numpy as np
import matplotlib.pyplot as plt

# Input
if(len(sys.argv) != 2):
   print ("Usage python histogram_plotter.py bins")
   sys.exit()

# Number of bins
bin = int(sys.argv[1]) 

# List of equilibrium times
t = np.loadtxt("EQ_times.txt")

# Remove all anomalous entries
t = [element for element in t if element < 3000]

# Plot histogram
plt.hist(t,bins = bin, density = False)
plt.title('Histogram of equilibrium times')
plt.xlabel(' Equilibrium Times ')
plt.ylabel(' Count')
plt.show()