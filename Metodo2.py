 from typing import Callable
import random as rnd
import time, sys


def Metodo(is_in: Callable[..., bool], x0: float,
            x1: float, y0: float, y1: float, number_of_seeds: int, points_per_seed: int) -> float:
    """
    Implementa o cálculo de área por meio método.
    """
    n_points_inside, n, m = 0, number_of_seeds, points_per_seed

    for _ in range(0, n):
        # A cada m pontos, eu troco a seed de geração de pontos.
        rnd.seed(time.time())
        
        for _ in range(0, m):
            # Obtenhos a coordenadas do ponto de forma aleatória
            x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)

            if is_in(x, y):
                # Caso esteja na área desejada, inclementa-se a variável. 
                n_points_inside += 1 
            else:
                pass

    # Finalmente, a área é calculada de forma simples:
    area = (n_points_inside/(n*m)) * ((y1 - y0) * (x1 - x0)) 
    return area

if len(sys.argv) > 1:
    def unit_circle(x, y):
        if x**2 + y**2 <= 1:
            return True
        else:
            return False

    out = Metodo(unit_circle, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                              int(sys.argv[5]), int(sys.argv[6]))

    exit(4 * out)