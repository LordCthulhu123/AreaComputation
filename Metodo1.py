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
        """
        Esta função define a adição usual de pontos considerados como vetores fixos.
        Ela também define a adição de um ponto com um escalar por a + (x, y) = (x + a, y + a)
        """
        if type(b) == type(self):
            return Point(self.x + b.x, self.y + b.y)
        elif type(b) == float:
            return Point(self.x + b, self.y + b)
        else:
            # Se não for um outro ponto ou um float, vê se é possível transormar em float.
            try:
                self.__add__(float(b))
            except ValueError:
                # Se não é possível transformar em float, eu não implemento mesmo. 
                # Esse caso não é de interesse.
                raise ValueError("Non Implemented")

    def __rmul__(self, b):
        """
        Esta função define a multiplicação por escalar usual para pontos considerados como vetotes fixos.
        """
        if type(b) == float:
            # Caso seja um float, retorna um ponto.
            return Point(b * self.x, b * self.y) 
        else:
            # Faz o mesmo que na função acima.
            try:
                self.__rmul__(float(b))
            except ValueError:
                raise ValueError("Non Implement")


class Grid:
    """
        Define a divisão de um retângulo em diversas partes. Ele vai guardar os centros de cada um dos retângulos.
    """
    def __init__(self, x0: float, x1: float, y0: float, y1: float,
                num_div_x: int, num_div_y: int) -> None:
        self.data = [] # Container para os pontos 
        self.number_of_points = 0

        # Vamos pegar os tamanhos dos retângulos:
        passo_x, passo_y = (x1 - x0) / num_div_x, (y1 - y0) / num_div_y
        self.base, self.altura = passo_x, passo_y
        self.div_x, self.div_y = num_div_x, num_div_y

        for i in range(0, num_div_y):
            # percorremos o eixo y, formando linha a linha.
            pos_y = y0 + (0.5 + i) * passo_y
            line = []
            for j in range(0, num_div_x):
                # Em cada linha, percorremos as colunas do grid.
                line.append(Point(x0 + (0.5 + j) * passo_x, pos_y)) # Adicionamos o ponto respectivo.
                self.number_of_points += 1 
            self.data.append(line)
        
        return 

    def __getitem__(self, key):
        """
            Define indexação do Grid por meio de pares ordenados.

                Grid[i][j] é o elemento na linha i e coluna j (vai de baixo para cima, esquerda para a direita)
        """
        return self.data[key[0]][key[1]]

    def __iter__(self):
        """
            O define como iterável para aplicação de laço for (onde podemos obter todos os pontos).
        """
        self.it_row, self.it_column = 0, 0
        return self 
    
    def __next__(self):
        """
            Faz a iteração pegando ponto a ponto e linha a linha.
        """
        if self.it_row < self.div_y:
            # Vai percorrendo a linha e depois a coluna
            p = self.data[self.it_row][self.it_column]

            self.it_column += 1

            if self.it_column == self.div_x:
                self.it_row += 1
                self.it_column = 0
            
            # Retorna o ponto respectivo.
            return p
        else: 
            # Quando terminar a iteração de todos os pontos, simplesmente terminamos o loop
            raise StopIteration 

    def get_area(self):
        """
            Retorna a área de cada retângulo do Grid.
        """
        return self.base * self.altura


def Calculate_area(is_in: Callable[..., bool],
                    x0=-2, x1=2, y0=-2, y1=2,
                    num_div_x=20, num_div_y=20) -> float:
    """
        Esta função faz o cálculo da quantidade de retângulos dentro da área relevante. 
        O parâmetro is_in é uma função que recebe um ponto e me retorna um bool que diz se ele está ou não na 
    região de relevância. Os outros são parâmetros do grid.
    """

    internal_grid = Grid(float(x0), float(x1), float(y0), float(y1), int(num_div_x), int(num_div_y))
    
    n_points_inside = 0
    for point in internal_grid:
        # Para cada ponto; se o centro dele está dentro da área relevante, eu conto mais um. 
        # Se não, eu simplesmente vou para o próximo.
        if is_in(point): 
            n_points_inside += 1 
        else:
            pass

    # A área é o produto da quantidade de pontos dentro da área 
    return n_points_inside* internal_grid.get_area()

def Calculate_area_and_show(is_in: Callable[..., bool],
                            x0=-2, x1=2, y0=-2, y1=2,
                            num_div_x=20, num_div_y=20, **configs) -> float:
    """
    Faz o mesmo que a função acima, mas também plota uma visualização do ocorrido.
    """
    
    fig, axs = plt.subplots(1)

    internal_grid = Grid(float(x0), float(x1), float(y0), float(y1), int(num_div_x), int(num_div_y))

    n_points_inside = 0
    for point in internal_grid:
        if is_in(point): 
            n_points_inside += 1 
            axs.plot(point.x, point.y, "o", color="b") # Marca um ponto azul caso o ponto esteja fora da região
        else:
            axs.plot(point.x, point.y, "o", color="k") # Marca um ponto preto caso o ponto esteja fora da região
            pass

    if "aditional_ploting" in configs:
        # Eu posso passar uma função como argumento para plotar mais coisa
        configs["aditional_ploting"](fig, axs)

    axs.set_aspect('equal')
    plt.show()

    return n_points_inside* internal_grid.get_area()

