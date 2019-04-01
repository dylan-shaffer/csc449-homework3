import numpy as np 


class Ant(object):

    data = None
    xpos = 0
    ypos = 0

    def __init__(self, x, y, size):
        self.xpos = x
        self.ypos = y
        self.max_size = size
        self.data = None


    def move_random(self):
        seed1 = np.random.rand()
        seed2 = np.random.rand()
        movX = 0
        movY = 0

        if seed1 < 0.5:
            movX = -1
        else:
            movX = 1
        
        if seed2 < 0.5:
            movY = 1
        else:
            movY = -1

        self.xpos = abs((self.xpos + movX) % self.max_size)
        self.ypos = abs((self.ypos + movY) % self.max_size)


    def is_loaded(self):
        if self.data is None:
            return False
        else:
            return True