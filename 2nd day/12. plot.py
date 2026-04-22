import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([10,20,70,200])
ypoints = np.array([20,30,150,200])

#plot line with markers
plt.plot(xpoints, ypoints, marker='o')

#add labels and titles
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("simple line plot")

#show grid
plt.grid()

#display graph
plt.show()