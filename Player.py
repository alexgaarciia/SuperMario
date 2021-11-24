import pyxel


class Mario:
    def __init__(self, x, y):
        self.w = 12
        self.h = 16
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 19, 0, self.w, self.h)


class BigMario:
    def __init__(self, x, y):
        self.w = 16
        self.h = 32
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, self.w, self.h)

class StarMario:
    def __init__(self, x, y):
        self.w = 16
        self.h = 32
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 48, 16, self.w, self.h)