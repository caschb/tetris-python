from Logic.Constants import Constants
from Logic.Piece import Piece
from Logic.Direction import Direction
from Logic.Scoreboard import Scoreboard
from copy import deepcopy
from time import sleep
import random
import threading


class Tetris:

    def __init__(self, printer=None):
        random.seed()

        self.grid = [[Constants.EMPTY_SPACE
                      for _ in range(Constants.COLUMNS)]
                     for _ in range(Constants.ROWS)]
        self._init_grid()

        self.falling_piece = Piece()
        self.next_piece = Piece(random.randrange(0, Piece.SHAPE_NUM))
        self.falling_piece_position = [-1, -1]
        self._select_shape()

        self.scoreboard = Scoreboard()

        self.printer = printer
        self.game_thread = threading.Thread(target=self._run)

    def _init_grid(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if row == len(self.grid) - 1 or col == 0 or col == len(self.grid[0]) - 1:
                    self.grid[row][col] = Constants.BORDER_SPACE

    def _print_grid(self):
        if self.printer:
            self.printer.print_grid(self.grid, self.falling_piece, self.falling_piece_position)

    def _select_shape(self):
        self.falling_piece_position = [1, 5]
        self.falling_piece.set_piece(self.next_piece.shape_type)
        self.next_piece.set_piece(random.randrange(0, Piece.SHAPE_NUM))

        print(f'Piece number: {self.falling_piece.shape_type}')

    def _can_rotate(self) -> bool:
        if self.falling_piece.shape_type == Piece.SHAPE_NAMES['Square']:
            return False

        pos = deepcopy(self.falling_piece.position)
        for row in pos:
            row[0], row[1] = row[1], -1 * row[0]

        for p in pos:
            new_row = self.falling_piece_position[0] + p[0]
            new_col = self.falling_piece_position[1] + p[1]
            if self.grid[new_row][new_col] != Constants.EMPTY_SPACE:
                return False
        return True

    def _rotate(self):
        if self.falling_piece.shape_type != Piece.SHAPE_NAMES['Square']:
            for row in self.falling_piece.position:
                row[0], row[1] = row[1], -1 * row[0]

    def _can_move(self, direction: Direction) -> bool:
        for row in self.falling_piece.position:
            new_row = self.falling_piece_position[0] + direction.my_direction[0] + row[0]
            new_col = self.falling_piece_position[1] + direction.my_direction[1] + row[1]
            if self.grid[new_row][new_col] != Constants.EMPTY_SPACE:
                return False
        return True

    def _move(self, direction: Direction):
        self.falling_piece_position[0] += direction.my_direction[0]
        self.falling_piece_position[1] += direction.my_direction[1]

    def _shape_has_landed(self):
        self._add_shape()
        if self.falling_piece_position[0] < 2:
            self.scoreboard.game_over = True
        else:
            self.scoreboard.add_lines(self._remove_lines())
        self._select_shape()

    def run(self):
        self.game_thread.start()

    def _run(self):
        print(f'Height : {len(self.grid)}, Width: {len(self.grid[0])}')
        while not self.scoreboard.game_over:
            sleep(self.scoreboard.get_speed()/1000)
            if self._can_move(Direction(Direction.DIRECTION_NAMES['Down'])):
                self._move(Direction(Direction.DIRECTION_NAMES['Down']))
            else:
                self._shape_has_landed()
            self._print_grid()
            print(f'Falling piece position: {self.falling_piece_position[0]}, {self.falling_piece_position[1]}')
            print(f'Level: {self.scoreboard.level}')
            print("")

    def _add_shape(self):
        for row in self.falling_piece.position:
            self.grid[self.falling_piece_position[0] + row[0]][self.falling_piece_position[1] + row[1]] = \
                Constants.FILLED_SPACE

    def _remove_line(self, line: int):
        for col in range(Constants.COLUMNS):
            self.grid[line][col] = Constants.EMPTY_SPACE

        for col in range(Constants.COLUMNS):
            for row in reversed(range(1, line + 1)):
                self.grid[row][col] = self.grid[row - 1][col]

    def _remove_lines(self) -> int:
        count = 0
        for row in range(Constants.ROWS - 1):
            for col in range(1, Constants.COLUMNS - 1):
                if self.grid[row][col] == Constants.EMPTY_SPACE:
                    break
            else:
                count += 1
                self._remove_line(row)
        return count

    def move(self, direction: str) -> bool:
        my_direction = Direction(Direction.DIRECTION_NAMES[direction])
        if self._can_move(my_direction):
            self._move(my_direction)
            self._print_grid()
            return True
        return False

    def move_left(self) -> bool:
        return self.move("Left")

    def move_right(self) -> bool:
        return self.move("Right")

    def drop_piece(self):
        my_direction: Direction = Direction(Direction.DIRECTION_NAMES["Down"])
        while self._can_move(my_direction):
            self._move(my_direction)
            self._print_grid()
        self._shape_has_landed()

    def rotate(self) -> bool:
        if self._can_rotate():
            self._rotate()
            self._print_grid()
            return True
        return False
