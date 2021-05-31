import numpy as np
import matplotlib.pyplot as plt
import Metodo1
import warnings

def func(p: Metodo1.Point):
    global x
    if p.x > 1 and p.x < x:
        if p.y >= 0 and p.y < 1/p.x:
            return True
        else: 
            return False
    else: 
        return False

x = 3

def ad(f, a: plt.Axes):
    warnings.filterwarnings('ignore')
    a.plot(np.linspace(-1, 5, 100), np.zeros(100), "k")
    a.plot(np.zeros(100), np.linspace(-1, 5, 100), "k")

    a.plot(np.linspace(0, 5, 1000), 1/np.linspace(0, 5, 1000))

    a.set_xlim(-1, 5)
    a.set_ylim(-1, 3)
    warnings.filterwarnings('default')


area = Metodo1.Calculate_area_and_show(func, x0=1, x1=x, y0=0, y1=1, **{"aditional_ploting": ad, "markersize": 1})
print("ln ({})".format(str(x)) + " = " + str(area))