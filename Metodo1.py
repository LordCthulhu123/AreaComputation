from dataclasses import dataclass 
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class Point:
    x: float 
    y: float

    def __add__(self, b):
        if type(b) == type(self):
            return Point(self.x + b.x, self.y + b.y)
        elif type(b) == float:
            return Point(self.x + b, self.y + b)
        else:
            try:
                self.__add__(float(b))
            except ValueError:
                raise ValueError("Non Implented")

    def __rmul__(self, b):
        if type(b) == float:
            return Point(b * self.x, b * self.y) 


class Grid:
    def __init__(self, x0, x1, y0, y1, num_div_x, num_div_y):
        self.data = []

        passo_x, passo_y = (x1 - x0) / num_div_x, (y1 - y0) / num_div_y
        self.base, self.altura = passo_x, passo_y
        self.div_x, self.div_y = num_div_x, num_div_y

        for i in range(0, num_div_y):
            pos_y = y0 + (0.5 + i) * passo_y
            line = []
            for j in range(0, num_div_x):
                line.append(Point(x0 + (0.5 + j) * passo_x, pos_y))
            self.data.append(line)
        
        return 

    def __getitem__(self, key):
        return self.data[key[0]][key[1]]

    def __iter__(self):
        self.it_row, self.it_column = 0, 0
        return self 
    
    def __next__(self):
        if self.it_row < self.div_y:
            p = self.data[self.it_row][self.it_column]

            self.it_column += 1

            if self.it_column == self.div_x:
                self.it_row += 1
                self.it_column = 0
            
            return p
        else: 
            raise StopIteration 

    def get_area(self):
        return self.base * self.altura


def in_unit_circle(p: Point) -> bool:
    if p.x**2 + p.y**2 <= 1:
        return True
    else: 
        return False 


n = 20
coiso = Grid(-2, 2, -2, 2, n, n)

fig, axs = plt.subplots(1)

n_points_inside = 0
for point in coiso:
    if in_unit_circle(point): 
        n_points_inside += 1 
        axs.scatter(point.x, point.y, color="b")
    else:
        axs.scatter(point.x, point.y, color="k")
        pass

angles = np.linspace(0, 2*np.pi, 1000)
axs.plot(np.cos(angles), np.sin(angles))

axs.set_aspect('equal')

print((n_points_inside/(n**2))*16)
plt.show()