from Logic.Tetris import Tetris
from Logic.Piece import Piece

if __name__ == '__main__':
    game = Tetris()
    game.run()
    b: Piece = Piece(0)
    print(b.position)

