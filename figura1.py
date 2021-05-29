import numpy as np
import matplotlib.pyplot as plt 
import Metodo1

a, b = 2, 2
n = 20

grid = Metodo1.Grid(x0=-a, x1=a, y0=-a, y1=a, num_div_x=n, num_div_y=n)

fig, axs = plt.subplots(1)

for point in grid:
    axs.plot(point.x, point.y, "o", c="blue", markersize=1)
    if (point.x**2 + point.y**2) <= 1:
        x = np.linspace(point.x - a/n, point.x + a/n, 10)
        y_up, y_down = (point.y + b/n) * np.ones(10), (point.y - b/n) * np.ones(10)
        axs.fill_between(x, y_down, y_up, color="plum")
        # print(point)

for i in range(0, n + 1):
    axs.plot(np.linspace(-a, a, 100), (-b + i * ((2*b)/n))*np.ones(100), "k")

for j in range(0, n + 1):
    axs.plot((-a + j * ((2*a)/n))*np.ones(100), np.linspace(-b, b, 100), "k")

angles = np.linspace(0, 2*np.pi, 1000)
axs.plot(np.cos(angles), np.sin(angles))

axs.set_aspect('equal')
axs.set_ylim(-3, 3)
axs.set_xlim(-3, 3)
plt.show()