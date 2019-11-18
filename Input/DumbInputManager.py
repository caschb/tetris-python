from Logic.Tetris import Tetris


class DumbInputManager:

    def __init__(self, game: Tetris):
        self.game: Tetris = game

    def main_loop(self):
        while not self.game.scoreboard.game_over:
            self.game.move_left()
            self.game.move_right()
            self.game.rotate()
