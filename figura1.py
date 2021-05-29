import numpy as np
import matplotlib.pyplot as plt 
import Metodo1

grid = Metodo1.Grid(x0=-2, x1=2, y0=-2, y1=2, num_div_x=10, num_div_y=10)

fig, axs = plt.subplots(1)

for point in grid:
    axs.plot(point.x, point.y, "o", c="blue", markersize=1)

for i in range(0, 11):
    axs.plot(np.linspace(-2, 2, 100), (-2 + i * (4/10))*np.ones(100), "k")

for j in range(0, 11):
    axs.plot((-2 + j * (4/10))*np.ones(100), np.linspace(-2, 2, 100), "k")

angles = np.linspace(0, 2*np.pi, 1000)
axs.plot(np.cos(angles), np.sin(angles))

axs.set_aspect('equal')
axs.set_ylim(-3, 3)
axs.set_xlim(-3, 3)
plt.show()