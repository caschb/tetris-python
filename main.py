from Logic.Tetris import Tetris
from UI.TextUI import TextUI
from UI.GraphicUI import GraphicUI
from Input.DumbInputManager import DumbInputManager
from Input.ManualInputManager import ManualInputManager
import threading
import time

if __name__ == '__main__':
    # printer: TextUI = TextUI()
    printer: GraphicUI = GraphicUI()
    game = Tetris(printer)
    game.run()
    # input_manager = DumbInputManager(game)
    # input_manager.main_loop()
    input_manager = ManualInputManager(game)
    input_manager.main_loop()
