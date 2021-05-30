from moviepy.editor import VideoClip                         # Serve para fazer o vídeo
from moviepy.video.io.bindings import mplfig_to_npimage 

import numpy as np 
import matplotlib.pyplot as plt
import random as rnd
import time 


def in_unit_circle(x: float, y: float) -> bool:
    if x**2 + y**2 <= 1:
        return True
    else: 
        return False 

n, m =  0, 30
fig, axs = plt.subplots(1)

a, b = 0, 1
n_points_inside = 0


def make_frame(t):
    global n_points_inside, n, a, b, fig, axs
    rnd.seed(time.time())
    
    for _ in range(0, m):
        x, y = rnd.uniform(a, b), rnd.uniform(a, b)

        if in_unit_circle(x, y): 
            n_points_inside += 1 
            axs.plot(x, y, "bo", markersize=0.5)
        else:
            axs.plot(x, y, "ko", markersize=0.5)

    n += m
    area = 4 * (n_points_inside/n) * ((b - a)**2) 
    axs.set_title(r"Calculando $\pi$ " + 
                    " n = {}, $\pi$ = {}".format(n, str(area)[:5]))

    return mplfig_to_npimage(fig)

angles = np.linspace(0, 0.5*np.pi, 1000)
axs.plot(np.cos(angles), np.sin(angles))

axs.set_aspect('equal')


animation = VideoClip(make_frame, duration=10) 

animation.write_gif(path + r'\AreaComputation\media\MetodoProbabilistico.gif', fps=20)  