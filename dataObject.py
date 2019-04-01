class DataObject(object):

    color = ""
    xpos = 0
    ypos = 0
    zpos = 0

    def __init__(self, x, y, c):
        self.xpos = x
        self.ypos = y
        self.color = c

        if self.color == "bo":
            self.zpos = 30
        elif self.color == "ro":
            self.zpos = 0


    def update_pos(self, x, y):
        self.xpos = x
        self.ypos = y

    