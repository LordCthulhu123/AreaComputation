from typing import Callable
from dataclasses import dataclass 
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Point:
    """
        Implementa uma noção de ponto do plano alternativa ao usado de tuples.
        São implementadas a adição e multiplicação por escalar tradicionais.
        Eu poderia ter usado números complexos ao invés disso, mas eu sou um imbecil.
        Eu fiz isso só porque eu queria usar .x e .y
    """
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
    """
        Define a divisão de um retângulo em diversas partes.
    """
    def __init__(self, x0: float, x1: float, y0: float, y1: float,
                num_div_x: int, num_div_y: int) -> None:
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
        """
            Define indexação do Grid por meio de pares ordenados.
        """
        return self.data[key[0]][key[1]]

    def __iter__(self):
        """
            O define como iterável.
        """
        self.it_row, self.it_column = 0, 0
        return self 
    
    def __next__(self):
        """
            Faz a iteração pegando ponto a ponto e linha a linha.
        """
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
        """
            Retorna a área de cada retângulo do Grid.
        """
        return self.base * self.altura


def in_unit_circle(p: Point) -> bool:
    if p.x**2 + p.y**2 <= 1:
        return True
    else: 
        return False 

def Calculate_area_and_show(is_in: Callable[..., bool],
                            x0=-2, x1=2, y0=-2, y1=2,
                            num_div_x=20, num_div_y=20, **configs) -> float:
    
    fig, axs = plt.subplots(1)

    internal_grid = Grid(float(x0), float(x1), float(y0), float(y1), int(num_div_x), int(num_div_y))

    n_points_inside = 0
    for point in internal_grid:
        if in_unit_circle(point): 
            n_points_inside += 1 
            axs.scatter(point.x, point.y, color="b")
        else:
            axs.scatter(point.x, point.y, color="k")
            pass

    if "aditional_ploting" in configs:
        configs["aditional_ploting"](fig, axs)

    axs.set_aspect('equal')
    plt.show()
    return (n_points_inside/(num_div_x * num_div_y))*((x1 - x0)*(y1 - y0))


a = Calculate_area_and_show(in_unit_circle, **{"aditional_ploting": lambda f, a: a.plot(
                        np.cos(np.linspace(0, 2*np.pi, 100)), np.sin(np.linspace(0, 2*np.pi, 100)))})

print(a)