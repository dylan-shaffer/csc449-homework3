import numpy as np 
import matplotlib.pyplot as plt 
import math
from dataObject import *


class Grid(object):

    def __init__(self, size):
        self.main_grid = [[None for y in range(size)] for x in range(size)]
        self.size = size
        self.data = []

        for i in range(0, size):
            found = False
            while (not found):
                x = np.random.randint(0, size)
                y = np.random.randint(0, size)

                if self.main_grid[x][y] is None:
                    colr = "bo"
                    if (i % 2) == 0:
                        colr = "ro"

                    self.main_grid[x][y] = DataObject(x, y, colr)
                    self.data.append(self.main_grid[x][y])
                    found = True


    def is_cell_empty(self, x, y):
        if self.main_grid[x][y] is None:
            return True
        else:
            return False


    def move_data(self, x_start, y_start, x_final, y_final):
        if self.is_cell_empty(x_final, y_final):
            if (x_start != x_final) and (y_start != y_final):
                self.main_grid[x_final][y_final] = self.main_grid[x_start][y_start]
                self.main_grid[x_start][y_start] = None


    def get_data_item(self, x, y):
        return self.main_grid[x][y]

    
    def set_data_item(self, x, y, dt):
        self.main_grid[x][y] = dt


    def get_prob(self, x, y, n):
        x_s = x - n
        y_s = y - n
        total = 0.0
        side = (n * 2) + 1

        for i in range(side):
            xi = (x_s + i) % self.size
            for j in range(side):
                yj = (y_s + j) % self.size
                if j != x and i != y:
                    dist = self.get_distance(x, y, xi, yj)
                    total += dist
        
        prob = total / ((side * side) - 1)
        prob = prob / 100.0

        return prob


    def get_distance(self, xs, ys, xf, yf):
        xdif = math.pow((xf-xs), 2)
        ydif = math.pow((yf-ys), 2)
        zs = 15
        zf = 15

        if not self.is_cell_empty(xs, ys):
            zs = self.main_grid[xs][ys].zpos
        
        if not self.is_cell_empty(xf, yf):
            zs = self.main_grid[xf][yf].zpos

        zdif = math.pow((zf-zs), 2)

        sumd = xdif + ydif + zdif
        dist = math.sqrt(sumd)

        return dist

    
    def get_count(self):
        rc = 0
        bc = 0

        for i in range(self.size):
            for j in range(self.size):
                if self.main_grid[i][j] is not None:
                    c = self.main_grid[i][j].color
                    
                    if c == "ro":
                        rc += 1
                    elif c == "bo":
                        bc += 1

        print("Red: " + str(rc))
        print("Blue: " + str(bc))


    def plot_grid(self):
        plt.axis([0, self.size, 0, self.size])

        for x in range(0, self.size):
            for y in range(0, self.size):
                if not self.is_cell_empty(x, y):
                    dpt = self.main_grid[x][y]
                    plt.plot([x], [y], dpt.color)

        plt.show()

