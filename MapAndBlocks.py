import pyxel

class Map:
    def __init__(self, u = 0, v = 0):
        self.tm = 0
        self.u = u
        self.v = v
        self.w = 80
        self.h = 64

    def draw(self):
        pyxel.bltm(0, 0, self.tm, self.u, self.v, self.w, self.h)

class QuestionBlock:
    def __init__(self, x, y, u=16, v=48):
        self.u = u
        self.v = v
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h)


class BrickBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 16, self.w, self.h)

class StrongBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 64, self.w, self.h)

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 16, 0, self.w, self.h)
