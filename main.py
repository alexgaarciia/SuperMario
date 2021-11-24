import pyxel
import Player
import Enemies
import MapAndBlocks


class Game:
    def __init__(self):
        pyxel.init(256, 256, scale=8, caption="Super Mario Bros", fps=60)
        pyxel.load("assets/resources.pyxres")

        self.map = MapAndBlocks.Map()

        self.player = Player.Mario(10, 208)
        self.player2 = Player.BigMario(170, 192)
        self.player3 = Player.StarMario(190, 192)

        self.qblock = MapAndBlocks.QuestionBlock(30, 208)
        self.sblock = MapAndBlocks.StrongBlock(50, 208)
        self.bblock = MapAndBlocks.BrickBlock(70, 208)
        self.pipe = MapAndBlocks.Pipe(90, 192)

        self.goomba = Enemies.Goomba(130, 208)
        self.koopa = Enemies.Koopa(150, 199)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        self.player.draw()
        self.player2.draw()
        self.player3.draw()
        self.qblock.draw()
        self.sblock.draw()
        self.bblock.draw()
        self.pipe.draw()
        self.goomba.draw()
        self.koopa.draw()


Game()