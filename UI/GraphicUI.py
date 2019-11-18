from Logic.Constants import Constants
from typing import List
import pygame as pg


class GraphicUI:

    WHITE: pg.Color = pg.Color(255, 255, 255)
    BLACK: pg.Color = pg.Color(0, 0, 0)
    RED: pg.Color = pg.Color(255, 0, 0)
    GREEN: pg.Color = pg.Color(0, 255, 0)
    BLUE: pg.Color = pg.Color(0, 0, 255)

    COLORS: List[pg.Color] = [RED, GREEN, BLUE]

    DIMENSIONS = (640, 640)

    BLOCK_SIZE = 30

    def __init__(self):
        pg.display.init()
        self.display_surface: pg.Surface = pg.display.set_mode(GraphicUI.DIMENSIONS)
        pg.display.update()

    def fill_square(self, color, coordinate):
        self.display_surface.fill(color=color,
                                  rect=pg.Rect(GraphicUI.BLOCK_SIZE * coordinate[0],
                                               GraphicUI.BLOCK_SIZE * coordinate[1],
                                               GraphicUI.BLOCK_SIZE,
                                               GraphicUI.BLOCK_SIZE))

    def print_grid(self, grid, falling_piece, falling_piece_position):
        printed = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for piece_row in falling_piece.position:
                    if row == falling_piece_position[0] + piece_row[0] and \
                            col == falling_piece_position[1] + piece_row[1]:
                        self.fill_square(GraphicUI.RED, (col, row))
                        printed = True
                if not printed:
                    if grid[row][col] == Constants.EMPTY_SPACE:
                        self.fill_square(GraphicUI.BLACK, (col, row))
                    else:
                        self.fill_square(GraphicUI.WHITE, (col, row))
                else:
                    printed = False
        pg.display.update()
