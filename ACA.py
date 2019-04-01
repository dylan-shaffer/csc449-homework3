import matplotlib.pyplot as plt
import numpy as np

from grid import Grid
from ant import Ant

grid_size = 200
aca_grid = Grid(grid_size)
ants = []

for i in range(500):
    x = np.random.randint(0, grid_size)
    y = np.random.randint(0, grid_size)

    a = Ant(x, y, grid_size)
    ants.append(a)

ant_count = len(ants)
aca_grid.plot_grid()

for i in range(50001):
    for j in range(ant_count):
        ant = ants[j]
        x = ant.xpos
        y = ant.ypos
        target = 0.15
        prob = 1.0

        if not ant.is_loaded() and not aca_grid.is_cell_empty(x, y):
            prob = aca_grid.get_prob(x, y, 7)
            if prob > target:
                ant.data = aca_grid.get_data_item(x, y)

        elif ant.is_loaded() and aca_grid.is_cell_empty(x, y):
            prob = aca_grid.get_prob(x, y, 7)
            if prob < target:
                ant.data = None
                
        ant.move_random()

        if ant.is_loaded():
            aca_grid.move_data(x, y, ant.xpos, ant.ypos)
            
        ants[j] = ant

    if (i % 10000) == 0:
        print(i)
        aca_grid.plot_grid()


