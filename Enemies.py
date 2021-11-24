import pyxel


class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 48, 0, self.w, self.h)


class Koopa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 16
        self.h = 25

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 32, self.w, self.h)
