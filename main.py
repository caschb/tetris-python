from Logic.Tetris import Tetris
from UI.TextUI import TextUI
from UI.GraphicUI import GraphicUI

if __name__ == '__main__':
    printer: TextUI = TextUI()
    graphic_printer: GraphicUI = GraphicUI()
    game = Tetris(graphic_printer)
    game.run()
