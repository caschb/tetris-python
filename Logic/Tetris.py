from Logic.Constants import Constants
from Logic.Piece import Piece
from Logic.Direction import Direction
from copy import deepcopy
import random


class Tetris:

    def __init__(self):
        random.seed()

        self.grid = [[Constants.EMPTY_SPACE
                      for _ in range(Constants.COLUMNS)]
                     for _ in range(Constants.ROWS)]
        self._init_grid()

        self.falling_piece = Piece()
        self.next_piece = Piece(random.randrange(0, Piece.SHAPE_NUM))
        self.falling_piece_position = [-1, -1]
        self._select_shape()

    def _init_grid(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if row == len(self.grid) - 1 or col == 0 or col == len(self.grid[0]) - 1:
                    self.grid[row][col] = Constants.BORDER_SPACE

    def _print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print("")

    def _select_shape(self):
        self.falling_piece_position = [1, 5]
        self.falling_piece.set_piece(self.next_piece.shape_type)
        self.next_piece.set_piece(random.randrange(0, Piece.SHAPE_NUM))

    def _can_rotate(self) -> bool:
        if self.falling_piece.shape_type == Piece.SHAPE_NAMES['Square']:
            return False

        pos = deepcopy(self.falling_piece.position)
        for row in pos:
            row[0], row[1] = row[1], -1 * row[0]

        for p in pos:
            new_col = self.falling_piece_position[0] + p[0]
            new_row = self.falling_piece_position[1] + p[1]
            if self.grid[new_col][new_row] != Constants.EMPTY_SPACE:
                return False
        return True

    def _rotate(self):
        if self.falling_piece.shape_type != Piece.SHAPE_NAMES['Square']:
            for row in self.falling_piece.position:
                row[0], row[1] = row[1], -1 * row[0]

    def _can_move(self, direction: Direction) -> bool:
        for row in self.falling_piece.position:
            new_col = self.falling_piece_position[0] + direction.my_direction[0] + row[0]
            new_row = self.falling_piece_position[1] + direction.my_direction[1] + row[1]
            if self.grid[new_col][new_row] != Constants.EMPTY_SPACE:
                return False
        return True

    def _move(self, direction: Direction):
        self.falling_piece_position[0] += direction.my_direction[0]
        self.falling_piece_position[1] += direction.my_direction[1]

    def run(self):
        print("under construction")
        self._print_grid()
